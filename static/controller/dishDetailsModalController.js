angular.module('routerApp').controller('dishDetailsModalController', ['$scope','$uibModalInstance' ,'params', function($scope, $uibModalInstance, params){

    let init = function (){
        $scope.name = params && params.name || '';
        $scope.peopleCount = params && params.peopleCount || 0;
        $scope.calories = params && params.calories || 0;
        $scope.cookingTime = params && params.cookingTime || 0;
        $scope.recipe = params && params.recipe || '';

    };


    $scope.ok = function () {
        $uibModalInstance.close($scope.dish);
    };

    $scope.cancel = function () {
        $uibModalInstance.dismiss('cancel');
    };


    init();
}]);