angular.module('apiServiceModule', []).service('apiService', ['$http', '$q', function ($http, $q) {
    this.login = function (user) {
        let promise = $q.defer();
        $http.post('/login', user).then(function (res) {
            console.log('finish');
            promise.resolve(res && res.data);
        })
            .catch(function (err) {
                debugger;
                console.log('err');
                promise.reject(err && err.data && err.data.err);
            });
        return promise.promise;

    };

    this.signup = function (user) {
        let promise = $q.defer();
        $http.post('/signup', user)
            .then((res) => {
                promise.resolve(res && res.data);
            })
            .catch((err) => {
                promise.reject(err && err.data && err.data.err);
            });

        return promise.promise;
    };

    this.searchRecipes = function (req) {
        let promise = $q.defer();
        $http.post('/searchDish', req)
            .then((res) => {
                promise.resolve(res && res.data || []);
            })
            .catch((err) => {
                promise.reject(err && err.data && err.data.err);
            });

        return promise.promise;

    };

    this.saveDinner = function (req) {
        let promise = $q.defer();
        $http.post('/addMeal', req)
            .then((res) => {
                promise.resolve(res && res.data || {})
            })
            .catch((err) => {
                promise.reject(err && err.data && err.data.err);
            });
        return promise.promise;
    };

    this.deleteDinner = function (req) {
        let promise = $q.defer();
        $http.delete('/deleteMeal', {
            params: req
        })
            .then((res) => {
                promise.resolve(res && res.data || {});
            })
            .catch((err) => {
                promise.reject(err && err.data && err.data.err);
            })
        return promise.promise;
    };

    this.getMyDinners = function (req) {
        let promise = $q.defer();
        $http.get('/getMyMeal', {
            params: {user_id: req}
        })
            .then((res) => {
                promise.resolve(res && res.data);
            })
            .catch((err) => {
                promise.reject(err && err.data && err.data.err);
            });
        return promise.promise;
    };


    this.addRecipe = function (req) {
        let promise = $q.defer();
        $http.post('/addDish', req)
            .then((res) => {
                promise.resolve(req)
            })
            .catch((err) => {
                promise.reject(err && err.data && err.data.err);
            });
        return promise.promise;
    };

    this.addIngredient = function(req){
        let promise = $q.defer();
        $http.post('/addIngredient', req)
            .then(res=>{
                promise.resolve(res && res.data);
            })
            .catch(err=>{
                promise.reject(err && err.data && err.data.err);
            });
        return promise.promise;
    };

    this.editRecipe = function (req) {
        let promise = $q.defer();

        $http.put('/addEditRecipe', req)
            .then(res => {
                promise.resolve(res && res.data);
            })
            .catch(err => {
                promise.reject(err && err.data && err.data.err);
            })

        return promise.promise;
    };

    this.deleteRecipe = function (req) {
        let promise = $q.defer();
        $http.delete('/deleteRecipe', {params: req})
            .then((res) => {
                promise.resolve(res);
            })
            .catch((err) => {
                promise.reject(err && err.data && err.data.err);
            });
        return promise.promise;
    };

    this.getIngredients = function (req) {
        let promise = $q.defer();
        $http.get('/getIngredients', req)
            .then((res) => {
                promise.resolve((res && res.data) || [])
            })
            .catch((err) => {
                promise.reject(err && err.data && err.data.err);
            });

        return promise.promise;
    };


    this.getMyRecipes = function (req) {
        let promise = $q.defer();
        $http.get('/getMyRecipes', {
            params: {user_id: req}
        })
            .then(res => {
                promise.resolve(res && res.data);
            })
            .catch(err => {
                promise.reject(err && err.data && err.data.err);
            });
        return promise.promise;
    };


}]);
