angular.module('routerApp').controller('userPageController', ['$rootScope','$scope', function($rootScope, $scope){
    $scope.showList = {};
    console.log('here');
    $scope.myList = [
        {
            name: 'dinner',
            foods : [
                {
                    name:'Hamburger',
                    desc:'testing desc',
                    img :'',
                    ingredients : [
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
                    cookingTime:30,
                    peopleCount:4,
                    calories:320,
                    newRecipe :[
                        'In a bowl, mix ground beef, egg, onion, bread crumbs, Worcestershire, garlic, 1/2 teaspoon salt, and 1/4 teaspoon pepper until well blended. Divide mixture into four equal portions and shape each into a patty about 4 inches wide.',
                        'Lay burgers on an oiled barbecue grill over a solid bed of hot coals or high heat on a gas grill (you can hold your hand at grill level only 2 to 3 seconds); close lid on gas grill. Cook burgers, turning once, until browned on both sides and no longer pink inside (cut to test), 7 to 8 minutes total. Remove from grill.\n',
                        'Lay buns, cut side down, on grill and cook until lightly toasted, 30 seconds to 1 minute.',
                        'Spread mayonnaise and ketchup on bun bottoms. Add lettuce, tomato, burger, onion, and salt and pepper to taste. Set bun tops in place.'
                    ],
                    recipe:'Step 1\n' +
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
                    name:'Hamburger',
                    desc:'testing desc',
                    img :'',
                    cookingTime:30,
                    peopleCount:4,
                    calories:320,
                    newRecipe :[
                        'In a bowl, mix ground beef, egg, onion, bread crumbs, Worcestershire, garlic, 1/2 teaspoon salt, and 1/4 teaspoon pepper until well blended. Divide mixture into four equal portions and shape each into a patty about 4 inches wide.',
                        'Lay burgers on an oiled barbecue grill over a solid bed of hot coals or high heat on a gas grill (you can hold your hand at grill level only 2 to 3 seconds); close lid on gas grill. Cook burgers, turning once, until browned on both sides and no longer pink inside (cut to test), 7 to 8 minutes total. Remove from grill.\n',
                        'Lay buns, cut side down, on grill and cook until lightly toasted, 30 seconds to 1 minute.',
                        'Spread mayonnaise and ketchup on bun bottoms. Add lettuce, tomato, burger, onion, and salt and pepper to taste. Set bun tops in place.'
                    ],
                    recipe:'Step 1\n' +
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
            ],
            ingredients : [
                {
                    name:"salt",
                    count:2
                },
                {
                    name:'sugar',
                    count:10
                },
                {
                    name:'paper',
                    count:20
                }
            ]
        }
    ];

    $scope.ingredients = [
        {
            name:"salt",
            count:2
        },
        {
            name:'sugar',
            count:10
        },
        {
            name:'paper',
            count:20
        }
    ]

    $scope.showDinnerList = function (dinnerRow) {
        $scope.showList = dinnerRow;
        calculateShoppingList(dinnerRow)
    };

    $scope.removeItem = function(key){
        // need to remove key, add sure validation
    };

    let calculateShoppingList = function(dinner){
        debugger;
        let tempList = {};
        dinner.foods.forEach(function(food){
            console.log(food);
            food && food.ingredients && food.ingredients.forEach(function(ing){
                if (tempList[ing.name]){
                    tempList[ing.name].count += ing.count;
                } else {
                    tempList[ing.name] = {
                        name:ing.name,
                        count:ing.count
                    }

                }

            })
        });

        // $scope.ingredients = tempList.forEach(function(ing){
        //     return {
        //         name: ing.name,
        //         count:ing.count
        //     }
        // })
        // console.log($scope.ingredients);
        // for


    }

}]);