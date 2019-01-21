angular.module('routerApp').controller('ModalInstanceCtrl', ['$scope', '$uibModalInstance', 'params', 'apiService', function ($scope, $uibModalInstance, params, apiService) {

    let getNumberOfIngredient = function(){
        if (!$scope.ingredients){
            return 0;
        }
        if ($scope.ingredients && !$scope.ingredients.length){
            return 0;
        }
        let count = 0;
        $scope.ingredients.forEach(ing=>{
            if (ing.count){
                count++;
            }
        });
        return count;
    };


    let validateAddingNewRecipe = function () {
        if (!$scope.dish.name) {
            $scope.errMsg = "Dish name cannot be empty";
            return false;
        }
        if (!$scope.dish.cookingTime) {
            $scope.errMsg = "Dish cooking time cannot be empty";
            return false;
        }
        if (!$scope.dish.calories) {
            $scope.errMsg = "Dish calories time cannot be empty";
            return false;
        }
        if (!$scope.dish.peopleCount ) {
            $scope.errMsg = "Dish people count cannot be empty";
            return false;
        }
        if (!$scope.dish.recipe){
            $scope.errMsg = "Dish recipe cannot be empty";
            return false;
        }
        if (getNumberOfIngredient() < 3 && !$scope.isEdit) {
            $scope.errMsg = "Dish must contain at least 3 ingredients";
            return false;
        }
        return true;

    };

    $scope.ok = function () {
        if (!validateAddingNewRecipe()) return;
        let ingList = [];
        $scope.newIng = "";
        $scope.errMsg = null;
        $scope.ingredients.forEach((ing) => {
            if (ing && ing.count) {
                ingList.push(ing);
            }
        });
        $scope.dish.ingredients = ingList;
        $uibModalInstance.close({dish:$scope.dish, isChange: $scope.isChange});
    };


    $scope.cancel = function () {
        $uibModalInstance.dismiss('cancel');
    };

    $scope.addIng = function () {
        if (!$scope.newIng) {
            $scope.errMsg = "Ingredient name contains only letters"
        } else {
            $scope.errMsg = null;
            apiService.addIngredient({name: $scope.newIng})
                .then(res => {
                    $scope.newIng = "";
                    $scope.ingredients.push(res);
                })
                .catch(err => {
                    $scope.newIng = "";
                    $scope.errMsg = "Ingredient Is " + err;
                    console.error(err);
                })
        }

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
        $scope.isChange = false;
        $scope.title = $scope.isEdit ? "Edit Recipe" : "Adding New Recipe";
        $scope.ingredients = [];
        $scope.errMsg = null;
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
        if (!this.searchForIng) {
            $scope.errMsg = "Ingredient contains only letters";
            return;
        }
        $scope.errMsg = null;
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
        $scope.isChange = form.$dirty;
        return form.$valid ;
    };

    init();


}]);