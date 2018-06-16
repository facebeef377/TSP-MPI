var app = angular.module('app',["ngRoute"]);

app.controller('appController',function($rootScope, $scope, $http) {

    $scope.tasks = {};
    $scope.instances = {};
    $scope.history = {};

    $scope.initVars = function()
    {
        $scope.init_task();
    }

  $scope.init_task = function (){
    $scope.getData_tasks();
    for (var i = 1; i <= 33333; i++) {
      (function(i) {
        setTimeout(function() {
          $scope.getData_tasks();
        }, i * 5000);
      })(i);
    }
  }

  $scope.getData_tasks = function(){
        $http
        .get("/tsp/tasks/")
        .then(
            function(result)
            {
              $scope.tasks = result.data;
              //console.log("Tasks" + JSON.stringify(result.data));
            });
    }

    $scope.getData_history = function(){
          $http
          .get("/tsp/history/")
          .then(
              function(result)
              {
                $scope.history = result.data;
                //console.log("History" + JSON.stringify(result.data));
              });
      }

    $scope.getData_instances = function(){
          $http
          .get("/tsp/instances/")
          .then(
              function(result)
              {
                $scope.instances = result.data;
                //console.log("Instances" + JSON.stringify(result.data));
              });
      }

      $scope.new_instance = {
        owner_id: 1
      };
      $scope.add_instance = function(x)
        {
            console.log($scope.new_instance)
            $http
            .post("http://127.0.0.1:8000/tsp/instances/", $scope.new_instance)
    				.then(
    					function(result)
    					{
                console.log(result);
                $rootScope.showSuccessAlert("Dodano!");
    					});
        }


        $scope.new_task = {
          owner_id: 1,
          status: 0
        };
        $scope.add_task = function(x)
          {
              console.log($scope.new_task)
              $http
              .post("http://127.0.0.1:8000/tsp/tasks/", $scope.new_task)
      				.then(
      					function(result)
      					{
                  console.log(result);
                  $rootScope.showSuccessAlert("Dodano!");
      					});
          }

          $scope.makeTask = function(x){

          }

        //Alerty
        $rootScope.showSuccessAlert = function(text)
        {
            $(function () {
                 swal({
                    type: 'success',
                    title: text,
                    showConfirmButton: false,
                    timer: 1500
                })
            });
        }

        $rootScope.showInfoAlert = function(text)
        {
            $(function () {
                swal({
                    type: 'info',
                    title: text,
                    showConfirmButton: false,
                    timer: 1500
                })
            });
        }

        $rootScope.showErrorAlert = function(text)
        {
            $(function () {
             swal({
                 type: 'error',
                 title: text,
                 showConfirmButton: false,
                 timer: 1500
              })
             });
        }

});

app.config(function($routeProvider,$locationProvider) {
	$locationProvider.hashPrefix('');
	$routeProvider
  .when('/start', {
		templateUrl : 'http://127.0.0.1:8000/static/parts/start.html',
	})
  .when('/instances', {
		templateUrl : 'http://127.0.0.1:8000/static/parts/instances.html',
	})
  .when('/server', {
		templateUrl : 'http://127.0.0.1:8000/static/parts/server.html',
	})
  .when('/tasks', {
		templateUrl : 'http://127.0.0.1:8000/static/parts/tasks.html',
	})
  .when('/history', {
		templateUrl : 'http://127.0.0.1:8000/static/parts/history.html',
	})
  .when('/task_add', {
    templateUrl : 'http://127.0.0.1:8000/static/parts/task_add.html',
  })
  .when('/instance_add', {
    templateUrl : 'http://127.0.0.1:8000/static/parts/instance_add.html',
  })
	.otherwise({
		redirectTo : '/start'
	});
}

);

app.config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});
