angular.module('routerApp').controller('searchController', ['$rootScope', '$scope', '$stateParams', '$uibModal', '$q', 'apiService', function ($rootScope, $scope, $stateParams, $uibModal, $q, apiService) {
    console.log(apiService);
    let init = function () {
        $scope.isLoading = false;
        $scope.chooseDish = false;
        $scope.user = $stateParams.user || {email: "", password: "", name: ""};
        $scope.search = {
            filter: {
                withIngredient: [],
                withoutIngredient: [],
                cookingTime: {
                    max: '',
                    min: ''
                },
                calories: {
                    max: '',
                    min: ''
                }

            },
            text: ""
        };
        $scope.withoutIngredient = [];
        $scope.withIngredient = [];
        apiService.getIngredients()
            .then(function (ingredients) {
                $scope.withIngredient = ingredients;
                $scope.withoutIngredient = angular.copy(ingredients);

            })
            .catch(function (err) {
                console.error("ERROR, not ing with" + err);
            });
        $scope.searchResult = [];
        $scope.myList = {};
    }


    $scope.onIngredientsFilterChange = function (key, value, type) {
        let filter = type === 'with' ? $scope.search.filter.withIngredient : $scope.search.filter.withoutIngredient;
        let index = filter.indexOf(value.id);
        if (index === -1) {
            filter.push(value.id);
        } else {
            let first = filter.slice(0, index);
            let second = filter.slice(index + 1, filter.length);

            type === 'with' ? $scope.search.filter.withIngredient = first.concat(second) : $scope.search.filter.withoutIngredient = first.concat(second);
        }

    };


    $scope.startSearch = function () {
        $scope.isLoading = true;
        $scope.search.user = $rootScope.user.id;
        apiService.searchRecipes($scope.search)
            .then(function (res) {
                $scope.searchResult = res;
                $scope.isLoading = false;
            })
            .catch(function (err) {
                $scope.isLoading = false;
                $rootScope.alert("fail", err);
            });


    };

    let clearMyList = function () {
        $scope.recpies.forEach((recipe) => {
            recipe.done = false;
        });
        $scope.myList = [];
    };

    $scope.onChangeRecepie = function (value, isImg) {
        if (isImg) {
            if (value.done) {
                delete $scope.myList[value.name];
                value.done = false;
                $scope.chooseDish = Object.keys($scope.myList).length;
            } else {
                value.done = true;
                $scope.myList[value.name] = value;
                $scope.chooseDish = true;

            }
        } else {
            if (value.done) {
                $scope.myList[value.name] = value;
                $scope.chooseDish = true;
            } else {
                delete $scope.myList[value.name];
                $scope.chooseDish = Object.keys($scope.myList).length;
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
            let requestDinnerList = [];
            Object.values($scope.myList).forEach((obj) => {
                requestDinnerList.push(obj.id)
            });
            apiService.saveDinner({
                name: name,
                dinnerList: requestDinnerList,
                user: $rootScope.user.id
            }).then(() => {
                clearMyList();
                $rootScope.alert("success");
            }, (err) => {
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
            res.user = $rootScope.user.id;
            apiService.addRecipe(res)
                .then((res) => {
                    $rootScope.alert("success");
                }, (err) => {
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
        $uibModal.open({
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

    // $scope.viewby = 10;
    // $scope.totalItems = 0;
    // $scope.currentPage = 4;
    // $scope.itemsPerPage = $scope.viewby;
    // $scope.maxSize = 5; //Number of pager buttons to show
    //
    // $scope.setPage = function (pageNo) {
    //     $scope.currentPage = pageNo;
    // };
    //
    // $scope.pageChanged = function() {
    //     console.log('Page changed to: ' + $scope.currentPage);
    // };
    //
    // $scope.setItemsPerPage = function(num) {
    //     $scope.itemsPerPage = num;
    //     $scope.currentPage = 1; //reset to first page
    // }


    init();


}]);




