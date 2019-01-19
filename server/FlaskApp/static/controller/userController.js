angular.module('routerApp').controller('userPageController', ['$rootScope', '$scope', 'apiService', function ($rootScope, $scope, apiService) {

    let init = function () {
        $scope.showList = {};
        $scope.myList = [];
        getUserRecipe();
    };


    $scope.showDinnerList = function (dinnerRow) {
        console.log(dinnerRow);
        dinnerRow.foods.forEach(dinner => {
            if (dinner && dinner.recipe && typeof(dinner.recipe) === "string"){
                dinner.recipe = dinner.recipe.split('.')
            }
        });
        $scope.showList = dinnerRow;


    };

    $scope.removeItem = function (key) {
        console.log(key);
        let toDelete = $scope.myList[key];
        apiService.deleteDinner({
            'meal_id': toDelete.meal_id,
            'user_id': $rootScope.user.id
        })
            .then((res) => {
                if ($scope.myList.length == 1) {
                    $scope.myList = [];
                    $scope.showList = {};
                } else {
                    $scope.showList = {};
                    getUserRecipe();
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


    init();


}]);