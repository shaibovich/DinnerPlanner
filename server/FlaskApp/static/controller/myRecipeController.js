angular.module('routerApp').controller('myRecipeController', ['$rootScope', '$scope', '$stateParams', '$uibModal', 'apiService', function ($rootScope, $scope, $stateParams, $uibModal, apiService) {

    let init = function () {
        $scope.myRecipe = [
            {
                name: 'Hamburger',
                desc: 'testing desc',
                img: '',
                ingredients: [
                    {
                        name: 'salt',
                        count: 2,
                        type: "cups"
                    },
                    {
                        name: 'salt',
                        count: 2,
                        type: "cups"
                    },
                    {
                        name: 'salt',
                        count: 2,
                        type: "cups"
                    },
                    {
                        name: 'salt',
                        count: 2,
                        type: "cups"
                    }

                ],
                cookingTime: 30,
                peopleCount: 4,
                calories: 320,
                newRecipe: [
                    'In a bowl, mix ground beef, egg, onion, bread crumbs, Worcestershire, garlic, 1/2 teaspoon salt, and 1/4 teaspoon pepper until well blended. Divide mixture into four equal portions and shape each into a patty about 4 inches wide.',
                    'Lay burgers on an oiled barbecue grill over a solid bed of hot coals or high heat on a gas grill (you can hold your hand at grill level only 2 to 3 seconds); close lid on gas grill. Cook burgers, turning once, until browned on both sides and no longer pink inside (cut to test), 7 to 8 minutes total. Remove from grill.\n',
                    'Lay buns, cut side down, on grill and cook until lightly toasted, 30 seconds to 1 minute.',
                    'Spread mayonnaise and ketchup on bun bottoms. Add lettuce, tomato, burger, onion, and salt and pepper to taste. Set bun tops in place.'
                ],
                recipe: 'Step 1\n' +
                    'In a bowl, mix ground beef, egg, onion, bread crumbs, Worcestershire, garlic, 1/2 teaspoon salt, and 1/4 teaspoon pepper until well blended. Divide mixture into four equal portions and shape each into a patty about 4 inches wide.\n' +
                    '\n' +
                    'Step 2\n' +
                    'Lay burgers on an oiled barbecue grill over a solid bed of hot coals or high heat on a gas grill (you can hold your hand at grill level only 2 to 3 seconds); close lid on gas grill. Cook burgers, turning once, until browned on both sides and no longer pink inside (cut to test), 7 to 8 minutes total. Remove from grill.\n' +
                    '\n' +
                    'Step 3\n' +
                    'Lay buns, cut side down, on grill and cook until lightly toasted, 30 seconds to 1 minute.\n' +
                    '\n' +
                    'Step 4\n' +
                    'Spread mayonnaise and ketchup on bun bottoms. Add lettuce, tomato, burger, onion, and salt and pepper to taste. Set bun tops in place.',

            },
            {
                name: 'Hamburger',
                desc: 'testing desc',
                img: '',
                ingredients: [
                    {
                        name: 'salt',
                        count: 2,
                        type: "cups"
                    },
                    {
                        name: 'salt',
                        count: 2,
                        type: "cups"
                    },
                    {
                        name: 'salt',
                        count: 2,
                        type: "cups"
                    },
                    {
                        name: 'salt',
                        count: 2,
                        type: "cups"
                    }

                ],
                cookingTime: 30,
                peopleCount: 4,
                calories: 320,
                newRecipe: [
                    'In a bowl, mix ground beef, egg, onion, bread crumbs, Worcestershire, garlic, 1/2 teaspoon salt, and 1/4 teaspoon pepper until well blended. Divide mixture into four equal portions and shape each into a patty about 4 inches wide.',
                    'Lay burgers on an oiled barbecue grill over a solid bed of hot coals or high heat on a gas grill (you can hold your hand at grill level only 2 to 3 seconds); close lid on gas grill. Cook burgers, turning once, until browned on both sides and no longer pink inside (cut to test), 7 to 8 minutes total. Remove from grill.\n',
                    'Lay buns, cut side down, on grill and cook until lightly toasted, 30 seconds to 1 minute.',
                    'Spread mayonnaise and ketchup on bun bottoms. Add lettuce, tomato, burger, onion, and salt and pepper to taste. Set bun tops in place.'
                ],
                recipe: 'Step 1\n' +
                    'In a bowl, mix ground beef, egg, onion, bread crumbs, Worcestershire, garlic, 1/2 teaspoon salt, and 1/4 teaspoon pepper until well blended. Divide mixture into four equal portions and shape each into a patty about 4 inches wide.\n' +
                    '\n' +
                    'Step 2\n' +
                    'Lay burgers on an oiled barbecue grill over a solid bed of hot coals or high heat on a gas grill (you can hold your hand at grill level only 2 to 3 seconds); close lid on gas grill. Cook burgers, turning once, until browned on both sides and no longer pink inside (cut to test), 7 to 8 minutes total. Remove from grill.\n' +
                    '\n' +
                    'Step 3\n' +
                    'Lay buns, cut side down, on grill and cook until lightly toasted, 30 seconds to 1 minute.\n' +
                    '\n' +
                    'Step 4\n' +
                    'Spread mayonnaise and ketchup on bun bottoms. Add lettuce, tomato, burger, onion, and salt and pepper to taste. Set bun tops in place.',

            }

        ];
        $scope.showRecipe = null;
    };

    let addEditRecipeCallback = function(res){
        console.log(res);
        apiService.addRecipe(res)
            .then((res)=>{
                $scope.myRecipe.push(res);
                $rootScope.alert("success");

            }, (err)=>{
                $rootScope.alert("fail", err);
            });
    };




    let removeRecipe = function(recipeRes){
        let tempList = [];
        $scope.myRecipe.forEach((recipe)=>{
           if (recipe && recipe.name === recipeRes.name){
               tempList.push(recipe);
           }
        });
        $scope.myRecipe = tempList;
    };


    $scope.deleteRecipe = function () {
        let uibModal = $uibModal.open({
            templateUrl: './static/template/modals/deleteModal.html',
            controller: 'deleteModalController',
            resolve : {
                params : function (){
                    return {
                        name:$scope.showRecipe.name
                    }
                }
            }
        });
        uibModal.result.then(function (name) {
            console.log(name);
            apiService.deleteRecipe(name)
                .then((res)=>{
                    removeRecipe($scope.showRecipe);
                    $scope.showRecipe = null;
                    $rootScope.alert("success");
                })
                .catch((err)=>{
                    $rootScope.alert("fail", err);
                });
        })
    };

    let getMyRecipes = function() {
        apiService.getMyRecipes($rootScope.user.id)
            .then(res=>{
                console.log(res);
            })
            .catch(err=>{
               console.error(err);
            });
    };


    $scope.editRecipe = function () {
        let uibModal = $uibModal.open({
            templateUrl: './static/template/modals/addRecipeModal.html',
            controller: 'ModalInstanceCtrl',
            resolve: {
                params: function () {
                    return {
                        name:$scope.showRecipe.name,
                        calories:$scope.showRecipe.calories,
                        link:'',
                        peopleCount:$scope.showRecipe.peopleCount,
                        details:$scope.showRecipe.recipe,
                        ingredients:$scope.showRecipe.ingredients,
                        isEdit : true
                    }
                }
            },
            size: 'lg'
        });
        uibModal.result.then(function (res) {
            addEditRecipeCallback(res);
        })


    };

    $scope.showUserRecipe = function (recipe) {
        $scope.showRecipe = recipe;
    };

    $scope.openAddRecipeModal = function () {
        let uibModal = $uibModal.open({
            templateUrl: './static/template/modals/addRecipeModal.html',
            controller: 'ModalInstanceCtrl',
            resolve: {
                params: function () {
                    return $scope.user
                }
            },
            size: 'lg'


        });

        uibModal.result.then(function (res) {
            addEditRecipeCallback(res);
        })
    };


    init();
}]);
