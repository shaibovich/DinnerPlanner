angular.module('routerApp').controller('ModalInstanceCtrl', ['$scope', '$uibModalInstance', 'params', 'apiService', function ($scope, $uibModalInstance, params, apiService) {
    $scope.ok = function () {
        let ingList = [];
        $scope.newIng = "";
        $scope.ingredients.forEach((ing) => {
            if (ing && ing.count) {
                ingList.push(ing);
            }
        });
        $scope.dish.ingredients = ingList;
        $uibModalInstance.close($scope.dish);
    };

    $scope.cancel = function () {
        $uibModalInstance.dismiss('cancel');
    };

    $scope.addIng = function () {
        apiService.addIngredient({name: $scope.newIng})
            .then(res => {
                $scope.newIng = "";
                $scope.ingredients.push(res);
            })
            .catch(err => {
                $scope.newIng = "";
                console.error(err);
            })
    };


    let markIngredients = function () {
        $scope.ingredients.forEach(function (ing) {
            if (ing && ing.count) {
                if (!$scope.dish.ingredients.length) {
                    $scope.dish.ingredients.push(ing);
                } else {
                    let check;
                    $scope.dish.ingredients.forEach(function (changeIng) {
                        check = ing.id === changeIng.id;
                        if (check && ing.count !== changeIng.count) {
                            changeIng.count = ing.count;
                        }
                    });
                    if (!check) {
                        $scope.dish.ingredients.push(ing);
                    }
                }

            }
        })
    };

    let markIngredientsResponse = function () {
        $scope.dish.ingredients.forEach(function (ing) {
            if (ing && ing.count) {
                $scope.ingredients.forEach(function (changeIng) {
                    if (ing.id === changeIng.id) {
                        changeIng.count = ing.count;
                    }
                })
            }
        })
    };

    let init = function () {
        $scope.isEdit = !!(params && params.isEdit);
        $scope.title = $scope.isEdit ? "Edit Recipe" : "Adding New Recipe";
        $scope.ingredients = [];
        $scope.searchForIng = "";
        $scope.dish = {
            name: params && params.name || "",
            calories: params && params.calories || 0,
            photoLink: params && params.link || "",
            peopleCount: params && params.peopleCount || 0,
            recipe: params && params.recipe || "",
            ingredients: params && params.ingredients || [],
            cookingTime: params && params.cookingTime || 0

        };


    };

    $scope.getIngredients = function () {
        markIngredients();
        apiService.getIngredients()
            .then(function (res) {
                $scope.ingredients = res;
                if ($scope.dish.ingredients && Object.keys($scope.dish.ingredients).length) {
                    markIngredientsResponse();
                }
            })
            .catch(function (err) {
                $scope.ingredients = [];
            });
    };

    $scope.searchIngredientByName = function () {
        markIngredients();
        let req = {
            params: {
                name: this.searchForIng
            }
        };
        apiService.getIngredients(req)
            .then(function (res) {
                $scope.ingredients = res;
                markIngredientsResponse();

            })
            .catch(function (err) {
                console.log(err);
                $scope.ingredients = [];
            })
    };


    $scope.validationAddRecipe = function (form) {
        return form.$valid;
    };

    init();


}]);