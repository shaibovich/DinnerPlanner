angular.module('routerApp').controller('userPageController', ['$rootScope', '$scope', 'apiService', function ($rootScope, $scope, apiService) {

    let init = function () {
        $scope.showList = {};
        $scope.myList = [];
        getUserRecipe();
    };


    $scope.showDinnerList = function (dinnerRow) {
        $scope.showList = dinnerRow;
        calculateShoppingList(dinnerRow)
    };

    $scope.removeItem = function (key) {
        // need to remove key, add sure validation
        console.log(key);
        let toDelete = $scope.myList[key];
        apiService.deleteDinner({
            'meal_id': toDelete.meal_id,
            'user_id': $rootScope.user.id
        })
            .then((res) => {
                if ($scope.myList.length==1){
                    $scope.myList = [];
                    $scope.showList = {};
                } else {
                    $scope.myList = $scope.myList.slice(key)
                }

            })
            .catch((err) => {
                console.error(err);
            })

    };

    let getUserRecipe = function () {
        apiService.getMyDinners($rootScope.user.id)

            .then((res) => {
                $scope.myList = res;
                console.log(res);
            })
            .catch((err) => {
                console.error(err);
                $scope.myList = [];
            })
    };


    let calculateShoppingList = function (dinner) {
        let tempList = {};
        dinner.foods.forEach(function (food) {
            console.log(food);
            food && food.ingredients && food.ingredients.forEach(function (ing) {
                if (tempList[ing.name]) {
                    tempList[ing.name].count += ing.count;
                } else {
                    tempList[ing.name] = {
                        name: ing.name,
                        count: ing.count
                    }

                }

            })
        });
    };

    init();


}]);