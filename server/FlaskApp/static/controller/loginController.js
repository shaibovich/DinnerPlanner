angular.module('routerApp').controller('loginController', ['$rootScope', '$scope', '$state', '$q', 'apiService', function ($rootScope, $scope, $state, $q, apiService) {

    let init = function () {
        $scope.user = {
            email: "",
            password: "",
            user: ""

        };
        $scope.loginLayout = false;
    };


    $scope.continue = function () {
        console.log($scope.user);
        $rootScope.isLoading = true;
        apiService.login($scope.user)
            .then(function (res) {
                $rootScope.saveToLocaleStorage('user', res);
                $rootScope.isConnected = true;
                $rootScope.user = res;

                $rootScope.isLoading = false;
                $state.go('searchPage', $scope.user, {
                    location: 'replace', inherit: true
                });
            }, function (err) {
                $scope.errMsg = err;
                $rootScope.isConnected = false;
                $rootScope.isLoading = false;
            });
    };

    $scope.signUp = function () {
        console.log($scope.user);
        $rootScope.isLoading = true;
        apiService.signup($scope.user)
            .then(function (res) {
                $rootScope.isConnected = true;
                $rootScope.isLoading = false;
                $rootScope.user = res;
                $state.go('search', $scope.user, {
                    location: 'replace', inherit: true
                })
            }, function (err) {
                $scope.errMsg = 'User ' + err;
                $rootScope.isLoading = false;
                $rootScope.isConnected = false;
            });

    };


    $scope.changeLayout = function () {
        $scope.loginLayout = !$scope.loginLayout;
    };

    $scope.isLogin = function () {
        return $scope.loginLayout;
    };

    $scope.validationLogin = function (form) {
        return form.$valid;
    };


    init();


}]);



