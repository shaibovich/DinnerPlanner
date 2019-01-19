angular.module('routerApp').controller('myRecipeController', ['$rootScope', '$scope', '$stateParams', '$uibModal', 'apiService', function ($rootScope, $scope, $stateParams, $uibModal, apiService) {

    let init = function () {
        $scope.myRecipe = [];
        $scope.showRecipe = null;
        getMyRecipes();
    };

    let addEditRecipeCallback = function (res) {
        console.log(res);
        apiService.editRecipe(res)
            .then((res) => {
                $scope.myRecipe.push(res);
                $rootScope.alert("success");

            }, (err) => {
                $rootScope.alert("fail", err);
            });
    };


    let removeRecipe = function (recipeRes) {
        let tempList = [];
        $scope.myRecipe.forEach((recipe) => {
            if (recipe && recipe.name === recipeRes.name) {
                tempList.push(recipe);
            }
        });
        $scope.myRecipe = tempList;
    };


    $scope.deleteRecipe = function () {
        let uibModal = $uibModal.open({
            templateUrl: './static/template/modals/deleteModal.html',
            controller: 'deleteModalController',
            resolve: {
                params: function () {
                    return {
                        name: $scope.showRecipe.name
                    }
                }
            }
        });
        uibModal.result.then(function (name) {
            console.log(name);
            apiService.deleteRecipe(name)
                .then((res) => {
                    removeRecipe($scope.showRecipe);
                    $scope.showRecipe = null;
                    $rootScope.alert("success");
                })
                .catch((err) => {
                    $rootScope.alert("fail", err);
                });
        })
    };

    let getMyRecipes = function () {
        apiService.getMyRecipes($rootScope.user.id)
            .then(res => {
                debugger;

                res.forEach(function (dish) {
                    if (dish.recipe) {
                        dish.recipe = dish.recipe.split('.');
                    }
                });
                $scope.myRecipe = res;
            })
            .catch(err => {
                $scope.myRecipe = {};
                console.error(err);
            });
    };


    $scope.editRecipe = function () {
        let uibModal = $uibModal.open({
            templateUrl: './static/template/modals/addRecipeModal.html',
            controller: 'ModalInstanceCtrl',
            resolve: {
                params: function () {
                    return {
                        name: $scope.showRecipe.name,
                        calories: $scope.showRecipe.calories,
                        link: $scope.showRecipe.photoLink,
                        peopleCount: $scope.showRecipe.peopleCount,
                        details: $scope.showRecipe.recipe,
                        ingredients: $scope.showRecipe.ingredients,
                        isEdit: true
                    }
                }
            },
            size: 'lg'
        });
        uibModal.result.then(function (res) {
            debugger;
            res.user = $rootScope.user.id;
            res.dish_id = $scope.showRecipe.id;
            addEditRecipeCallback(res);
        })


    };

    $scope.showUserRecipe = function (recipe) {
        $scope.showRecipe = recipe;
    };

    $scope.openAddRecipeModal = function () {
        let uibModal = $uibModal.open({
            templateUrl: './static/template/modals/addRecipeModal.html',
            controller: 'ModalInstanceCtrl',
            resolve: {
                params: function () {
                    return $scope.user
                }
            },
            size: 'lg'


        });

        uibModal.result.then(function (res) {
            // addEditRecipeCallback(res);
        })
    };


    init();
}]);
