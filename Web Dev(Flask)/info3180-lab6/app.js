var app = angular.module('Shopping',['ui.bootstrap']);

app.controller('MainCtrl', function($scope){
	
	$scope.newitem = "";
	
	$scope.title = "My Shopping List";
	$scope.alertblank = { show: false, type:"Info", msg:"Info"};
	$scope.success_alert = { show: true, type: 'success', msg:"Successfully added!"};
	$scope.danger_alert = { show: true, type: 'danger', msg:"Enter an item"};
	$scope.products = ["Bacon", "Pancake Mix", "Orange Juice", "Green Tea"];
	$scope.alert = $scope.alertblank;
	$scope.addproduct = function(product){
		if (product == ""){
			$scope.alert = $scope.danger_alert;
		}else{
			$scope.products.push(product);
			
			$scope.newitem = "";
			
			$scope.alert = $scope.success_alert;

		}
		
		
	};
	
	$scope.removeItem = function (x) {
        $scope.products.splice(x, 1);
    } 
	
});