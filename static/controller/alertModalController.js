angular.module('routerApp').controller('alertModalController', ['$scope','$uibModalInstance', 'params', function($scope, $uibModalInstance, params){
    let init = function(){
        $scope.errMsg = params && params.errMsg || "";
        $scope.isSuccess = !!(params && params.type !== "fail");
    };

    $scope.ok = function () {
        $uibModalInstance.close($scope.dish);
    };




    init();
}]);
