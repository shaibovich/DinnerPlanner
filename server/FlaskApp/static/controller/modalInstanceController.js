angular.module('routerApp').controller('ModalInstanceCtrl', ['$scope', '$uibModalInstance', 'params', 'apiService', function ($scope, $uibModalInstance, params, apiService) {
    $scope.ok = function () {
        let ingList = [];
        debugger;
        $scope.ingredients.forEach((ing)=>{
           if (ing && ing.count){
               ingList.push(ing);
           }
        });
        $scope.dish.ingredients = ingList;
        $uibModalInstance.close($scope.dish);
    };

    $scope.cancel = function () {
        $uibModalInstance.dismiss('cancel');
    };


    console.log(params);

    let markIngredients = function (list) {
        list && $scope.ingredients.forEach(function (ing) {
            if (list.indexOf(ing.name) > -1) {
                ing.count = list.get(ing.name).count;
            }
        })
    };

    let init = function () {
        $scope.title = params && params.isEdit ? "Edit Recipe" : "Adding New Recipe";

        $scope.ingredients = [];

        $scope.dish = {
            name: params && params.name || "",
            calories: params && params.calories || 0,
            photoLink: params && params.link || "",
            peopleCount: params && params.peopleCount || 0,
            recipe: params && params.recipe || "",
            ingredients: params && params.ingredients || {},
            cookingTime: params && params.cookingTime || 0

        };

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
    };


    $scope.onIngredientsChange = function (key, value) {
        console.log(key, value);
        if (value.checked) {
            $scope.dish.ingredients[key] = value;
        } else {
            $scope.dish.ingredients[key] = {};
            delete $scope.dish.ingredients[key];
        }
    };

    $scope.validationAddRecipe = function (form){
        return form.$valid;
    };

    init();


}]);