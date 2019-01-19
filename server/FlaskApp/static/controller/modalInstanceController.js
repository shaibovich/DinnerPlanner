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

    $scope.addIng = function() {
        debugger;
        apiService.addIngredient({name:$scope.newIng})
            .then(res=>{
                $scope.newIng = "";
                $scope.ingredients.push(res);
            })
            .catch(err=>{
                $scope.newIng = "";
                console.error(err);
            })
    };


    let markIngredients = function (list) {
        list && $scope.ingredients.forEach(function (ing) {
            if (list.indexOf(ing.name) > -1) {
                ing.count = list.get(ing.name).count;
            }
        })
    };

    let init = function () {
        $scope.isEdit = !!(params && params.isEdit);
        $scope.title = $scope.isEdit ? "Edit Recipe" : "Adding New Recipe";
        $scope.ingredients = [];
        getIngredients();
        $scope.dish = {
            name: params && params.name || "",
            calories: params && params.calories || 0,
            photoLink: params && params.link || "",
            peopleCount: params && params.peopleCount || 0,
            recipe: params && params.recipe || "",
            ingredients: params && params.ingredients || {},
            cookingTime: params && params.cookingTime || 0

        };


    };

    let getIngredients = function (){
        apiService.getIngredients()
            .then(function (res) {
                $scope.ingredients = res;
                if ($scope.dish.ingredients && Object.keys($scope.dish.ingredients).length) {
                    let ingName = $scope.dish.ingredients.forEach(function (ing) {
                        return ing.name;
                    });
                    markIngredients(ingName);
                }
            })
            .catch(function (err) {
                $scope.ingredients = [];
            });
    }

    $scope.onIngredientsChange = function (key, value) {
        console.log(key, value);
        if (value.checked) {
            $scope.dish.ingredients[key] = value;
        } else {
            $scope.dish.ingredients[key] = {};
            delete $scope.dish.ingredients[key];
        }
    };

    $scope.validationAddRecipe = function (form) {
        return form.$valid;
    };

    init();


}]);