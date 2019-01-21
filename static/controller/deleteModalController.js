angular.module('routerApp').controller('deleteModalController', ['$scope', '$uibModalInstance', 'params', function($scope, $uibModalInstance, params){

    let init = function (){
        $scope.name = params && params.name || "";
    };

    init();

    $scope.ok = function () {
        $uibModalInstance.close($scope.name);
    };

    $scope.cancel = function () {
        $uibModalInstance.dismiss('cancel');
    };


}]);