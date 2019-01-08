angular.module('apiServiceModule', []).service('apiService', ['$http', '$q', function ($http, $q) {
    this.login = function (user) {
        let res;
        console.log(user);
        let req = {
            method: 'POST',
            url: 'url',
            param: user
        };

        let promise = $q.defer();
        setTimeout(function () {
            if (user && user.password && user.password === "123456") {
                promise.resolve(user);
            } else {
                promise.reject("Invalid Email / Password");
            }

        }, 1000);
        return promise.promise;

    };

    this.signup = function (user) {
        let promise = $q.defer();
        setTimeout(function () {
            if (user && user.password && user.password === "123456") {
                promise.resolve(user);
            } else {
                promise.reject("Invalid Email / Password");
            }

        }, 1000);
        return promise.promise;
    };

    this.searchRecipes = function (req) {
        let promise = $q.defer();
        setTimeout(function () {
            promise.resolve("");
        }, 1000);
        return promise.promise;

    };

    this.saveDinner = function (req) {
        let promise = $q.defer();
        setTimeout(function () {
            promise.resolve();
        }, 1000)
        return promise.promise;
    };

    this.addRecipe = function (req) {
        let promise = $q.defer();
        setTimeout(function () {
            promise.resolve(foodExample);
        }, 1000);
        return promise.promise;
    };

    this.deleteRecipe = function (req) {
        let promise = $q.defer();
        setTimeout(function () {
            promise.resolve();
        }, 1000);
        return promise.promise;
    };

    let foodExample ={
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

    };
}]);