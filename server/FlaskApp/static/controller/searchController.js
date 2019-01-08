angular.module('routerApp').controller('searchController', ['$rootScope', '$scope', '$stateParams', '$uibModal', '$q', 'apiService', function ($rootScope, $scope, $stateParams, $uibModal, $q, apiService) {
    console.log(apiService);
    let init = function () {
        $scope.isLoading = false;
        $scope.user = $stateParams.user || {email: "", password: "", name: ""};
        $scope.search = {
            filter: {
                ingridents: []

            },
            text: ""
        };
        $scope.ingridents = [
            {
                name: 'milk'
            },
            {
                name: 'sugar'
            },
            {
                name: 'coffee'
            },
            {
                name: 'salt'
            },
            {
                name: 'papper'
            },
            {
                name: 'olive'
            }
        ];
        $scope.searchResult = [];
        $scope.recpies = [
            {
                name: 'Conchiglioni with Tofu Ricotta',
                cookingTime: 30,
                calories: 250,
                peopleCount: 4,
                photoLink: 'http://media-cache-ak0.pinimg.com/736x/1d/00/01/1d0001fa63225bff898025658a90bece.jpg',
                done: false
            },
            {
                name: 'Cauliflower Rice Sushi',
                cookingTime: 45,
                calories: 175,
                peopleCount: 2,
                photoLink: "https://anodetomungbeans.files.wordpress.com/2013/11/dsc_0330.jpg",
                done:false
            },
            {
                name: 'Chickpea Falafel',
                cookingTime: 75,
                calories: 85,
                peopleCount: 6,
                photoLink: "http://gourmandelle.com/wp-content/uploads/2013/10/Chiftelute-de-naut-Falafel-Chickpea-Patties-Recipe.jpg",
                done:false
            },
            {
                name: 'Conchiglioni with Tofu Ricotta',
                cookingTime: 30,
                calories: 250,
                peopleCount: 4,
                photoLink: 'http://media-cache-ak0.pinimg.com/736x/1d/00/01/1d0001fa63225bff898025658a90bece.jpg',
                done: false
            },
            {
                name: 'Conchiglioni with Tofu Ricotta',
                cookingTime: 30,
                calories: 250,
                peopleCount: 4,
                photoLink: 'http://media-cache-ak0.pinimg.com/736x/1d/00/01/1d0001fa63225bff898025658a90bece.jpg',
                done: false
            },
            {
                name: 'Conchiglioni with Tofu Ricotta',
                cookingTime: 30,
                calories: 250,
                peopleCount: 4,
                photoLink: 'http://media-cache-ak0.pinimg.com/736x/1d/00/01/1d0001fa63225bff898025658a90bece.jpg',
                done: false
            },
            {
                name: 'Conchiglioni with Tofu Ricotta',
                cookingTime: 30,
                calories: 250,
                peopleCount: 4,
                photoLink: 'http://media-cache-ak0.pinimg.com/736x/1d/00/01/1d0001fa63225bff898025658a90bece.jpg',
                done: false
            }
        ];
        $scope.myList = {};
    }


    $scope.onIngredientsFilterChange = function (key, value) {
        console.log(key, value);
    };


    $scope.startSearch = function () {
        $scope.isLoading = true;
        apiService.searchRecipes($scope.search)
            .then(function (res) {
                $scope.searchResult = $scope.recpies;
                $scope.isLoading = false;
            })
            .catch(function (err) {
                $scope.isLoading = false;
                $rootScope.alert("fail", err);
            });


    };

    let clearMyList = function(){
        $scope.recpies.forEach((recipe)=>{
            recipe.done = false;
        });
        $scope.myList = [];
    };

    $scope.onChangeRecepie = function (value, isImg) {
        if (isImg){
            if (value.done){
                delete $scope.myList[value.name];
                value.done = false;
            } else {
                value.done = true;
                $scope.myList[value.name] = value;

            }
        } else {
            if (value.done) {
                $scope.myList[value.name] = value;
            } else {
                delete $scope.myList[value.name];
            }
        }

    };

    $scope.saveList = function () {
        console.log($scope.myList);
        let uibModal = $uibModal.open({
            templateUrl: './static/template/modals/saveListModal.html',
            controller: 'NameModalCtrl'
        });
        uibModal.result.then(function (name) {
            console.log(name);
            apiService.saveDinner(name)
                .then(()=>{
                    clearMyList();
                    $rootScope.alert("success");
                }, (err)=>{
                    $rootScope.alert("fail", err);
                });
        })
    };



    $scope.openAddRecipeModal = function () {
        let uibModal = $uibModal.open({
            templateUrl: './static/template/modals/addRecipeModal.html',
            controller: 'ModalInstanceCtrl',
            resolve: {
                params: function () {
                    return {
                        user: $scope.user,
                        isEdit: false
                    }
                }
            },
            size: 'lg'


        });
        uibModal.result.then(function (res) {
            console.log(res);
            apiService.addRecipe(res)
                .then((res)=>{
                    $rootScope.alert("success");
                }, (err)=>{
                    $rootScope.alert("fail", err);
                });
        })

    };

    $scope.removeItem = function (key) {
        for (index in $scope.recpies) {
            if ($scope.recpies[index].name === key) {
                $scope.recpies[index].done = false;
                break;
            }
        }
        delete $scope.myList[$scope.recpies[index].name];
    };

    $scope.openDishModal = function (value) {
        let uibModal = $uibModal.open({
            templateUrl: './static/template/modals/dishDetailsModal.html',
            controller: 'dishDetailsModalController',
            resolve: {
                params: function () {
                    return {
                        name: value.name,
                        cookingTime: value.cookingTime,
                        calories: value.calories,
                        peopleCount: value.peopleCount
                    }
                }
            },
            windowClass: 'app-modal-window',
            size: 'lg'

        });
    };

    init();


}]);




