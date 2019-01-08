angular.module('routerApp').controller('ModalInstanceCtrl', ['$scope', '$uibModalInstance', 'params', function($scope, $uibModalInstance, params){
    $scope.ok = function () {
        $uibModalInstance.close($scope.dish);
    };

    $scope.cancel = function () {
        $uibModalInstance.dismiss('cancel');
    };

    // $scope.dish = params;
    console.log(params);

    let markIngredients = function(list){

        list && $scope.ingredients.forEach(function(ing){
            if (list.indexOf(ing.name) > -1){
                ing.checked = true;
            }
        })
    };

    let init = function(){
        $scope.title = params && params.isEdit ? "Edit Recipe" : "Adding New Recipe";

        // get ingredients list
        $scope.ingredients = [

            {
                name: 'salt',
                checked : false
            },
            {
                name: 'paper',
                checked : false
            },
            {
                name: 'eggs',
                checked : false
            },
            {
                name: 'orange',
                checked : false
            }
        ];

        $scope.dish = {
            name : params && params.name || "",
            calories:  params && params.calories || 0,
            link : params && params.link || "",
            peopleCount: params && params.peopleCount || 0,
            details : params && params.details || "",
            ingredients : params && params.ingredients ||  {}

        };

        if ($scope.dish.ingredients && Object.keys($scope.dish.ingredients).length){
            let ingName = $scope.dish.ingredients.forEach(function(ing){
                return ing.name;
            });
            markIngredients(ingName);
        }

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

    init();







}]);