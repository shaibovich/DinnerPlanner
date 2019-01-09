angular.module('routerApp').controller('loginController', ['$rootScope' , '$scope', '$state', '$q','apiService',function ($rootScope, $scope, $state, $q, apiService) {

    let init = function () {
        $scope.user = {
            email: "",
            password: "",
            user: "",
            rememberMe: false
        };
        $scope.loginLayout = false;
    };


    $scope.continue = function () {
        console.log($scope.user);
        $rootScope.isLoading = true;
        apiService.login($scope.user)
            .then(function response(res){
                $rootScope.saveToLocaleStorage('user', res);
                $rootScope.isConnected = true;
                $rootScope.setCookie($scope.user.email);
                $rootScope.isLoading = false;
                $state.go('search', $scope.user, {location: 'replace'});
            }, function (err){
                $scope.errMsg = err;
                $rootScope.isConnected = false;
                $rootScope.isLoading = false;
            });
    };

    $scope.signUp = function () {
        console.log($scope.user);
        $rootScope.isLoading = true;
        apiService.signup($scope.user)
            .then(function (res){
                $rootScope.isConnected = true;
                $rootScope.isLoading = false;
                $state.go('search', $scope.user, {location: 'replace'})
            }, function(err){
                $scope.errMsg = err;
                $rootScope.isLoading = false;
                $rootScope.isConnected = false;
            });

    };


    $scope.changeLayout = function () {
        $scope.loginLayout = !$scope.loginLayout;
    };

    $scope.isLogin = function() {
        return $scope.loginLayout;
    };

    $scope.validationLogin = function(form){
        return form.$valid;
    };


    init();


}]);



