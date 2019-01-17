angular.module('routerApp', ['ui.router', 'ui.bootstrap', 'apiServiceModule'])
    .config(['$stateProvider', '$urlRouterProvider', '$locationProvider', function ($stateProvider, $urlRouterProvider) {

        $stateProvider
            .state('home', {
                url: 'home',
                templateUrl: './static/template/homePage.html',
                controller: 'mainController'
            })
            .state('login', {
                url: '/login',
                templateUrl: './static/template/login.html',
                controller: 'loginController'
            })
            .state('search', {
                url: '/search',
                templateUrl: './static/template/searchPage.html',
                controller: 'searchController'
            })
            .state('userPage', {
                url: '/userPage',
                templateUrl: './static/template/userPage.html',
                controller: "userPageController"
            })
            .state('myRecipe', {
                url:'/myRecipe',
                templateUrl :'./static/template/myRecipe.html',
                controller:'myRecipeController'
            });

        $urlRouterProvider.otherwise('/home');

    }])


    .run(function ($rootScope , $state, $uibModal) {
        $rootScope.isLoading = false;
        $rootScope.isConnected = false;
        console.log($state);

        $rootScope.isLogin = function(){
            let localUser = $rootScope.getLocaleStorage('user');
            if (localUser && localUser.id){
                $rootScope.isConnected = true;
                $rootScope.user = localUser;
                $state.go('search', {}, {location:'replace'});
            }
        };



        $rootScope.saveToLocaleStorage = function(key, value){
            window.localStorage[key] = JSON.stringify(value);

        };

        $rootScope.getLocaleStorage = function(key){
            return window.localStorage[key] || null;
        };

        $rootScope.deleteLocalStorage = function(key){
            if ($rootScope.getLocaleStorage(key)){
                delete window.localStorage[key];
            }
        };


        if ($rootScope.getLocaleStorage('user')) {
            $rootScope.isConnected = true;
            $rootScope.user = JSON.parse($rootScope.getLocaleStorage('user'));
            $state.go('search', {} ,{location:'replace'})
        } else {
            $state.go('home', {}, {location:'replace'})
        }

        $rootScope.logOut = function(){
            $rootScope.deleteLocalStorage('user');
            $rootScope.isConnected = false;
            $state.go('home', {}, {location:'replace'});
        };

        $rootScope.alert = function (type ,errMsg){
            $uibModal.open({
                templateUrl: './static/template/modals/alertModal.html',
                controller: 'alertModalController',
                resolve: {
                    params: function () {
                        return  {
                            type:type,
                            errMsg:errMsg
                        }
                    }
                },
                windowClass: 'app-modal-window'
            });
        }


    })
    .controller('NameModalCtrl', function( $scope, $uibModalInstance){
        $scope.ok = function () {
            $uibModalInstance.close($scope.name);
        };

        $scope.cancel = function () {
            $uibModalInstance.dismiss('cancel');
        };

        $scope.name =  "";

    });
