angular.module('routerApp').controller('searchController', ['$rootScope', '$scope', '$stateParams', '$uibModal', '$q', 'apiService', function ($rootScope, $scope, $stateParams, $uibModal, $q, apiService) {
    console.log(apiService);
    let init = function () {
        $scope.isLoading = false;
        $scope.chooseDish = false;
        $scope.errMsg = null;
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


    let validateSearch = function () {

        if (!$scope.search.text) {
            $scope.errMsg = "Search field must be filled with at least 3 letters and only letters"
        } else if ($scope.search.text.length < 3) {
            $scope.errMsg = "Search field must be filled with at least 3 letters and only letters"
        } else {
            $scope.errMsg = null;
        }


    };

    $scope.startSearch = function () {
        validateSearch();
        $scope.isLoading = true;
        $scope.search.user = $rootScope.user.id;
        if (checkRangeFilters($scope.search.filter) && !$scope.errMsg) {
            apiService.searchRecipes($scope.search)
                .then(function (res) {
                    $scope.searchResult = res;
                    $scope.isLoading = false;
                })
                .catch(function (err) {
                    $scope.isLoading = false;
                    $rootScope.alert("fail", err);
                });
        } else {
            $scope.isLoading = false;
        }
    };

    let checkRangeFilters = function (filter) {
        if (!checkMinAndMaxFilter(filter.calories)) {
            $scope.errMsg = "Maximum value cannot be smaller than minimum";
            return false;
        }
        if (!checkMinAndMaxFilter(filter.cookingTime)) {
            $scope.errMsg = "Maximum value cannot be smaller than minimum";
            return false;
        }
        return true;

    };

    let checkMinAndMaxFilter = function (filter) {
        filter.max = filter.max == null ? '' : filter.max;
        filter.min = filter.min == null ? '' : filter.min;
        if (filter.max === '' || filter.min === '') {
            return true;
        } else {
            return filter.min < filter.max;
        }

    };

    let clearMyList = function () {
        Object.values($scope.myList, recipe => {
            recipe.done = false;
        });
        $scope.myList = {};
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
            if (!res.isChange){
                return;
            }
            res.dish.user = $rootScope.user.id;
            apiService.addRecipe(res.dish)
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




