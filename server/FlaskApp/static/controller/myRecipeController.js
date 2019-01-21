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
                getMyRecipes();
                $rootScope.alert("success");
            }, (err) => {
                $rootScope.alert("fail", err);
            });
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
            let req = {
                user_id: $rootScope.user.id,
                dish_id: $scope.showRecipe.id

            };
            apiService.deleteRecipe(req)
                .then((res) => {
                    getMyRecipes();
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
                        recipe : $scope.showRecipe.recipe,
                        cookingTime:$scope.showRecipe.cookingTime,
                        isEdit: true
                    }
                }
            },
            size: 'lg'
        });
        uibModal.result.then(function (res) {
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
                    return {user:$scope.user}
                }
            },
            size: 'lg'
        });
        uibModal.result.then(function (res) {
            res.user = $rootScope.user.id;
            apiService.addRecipe(res)
                .then((res) => {
                    $rootScope.alert('success')
                }, (err) => {
                    $rootScope.alert("fail", err);
                });
        })

    };


    init();
}]);
