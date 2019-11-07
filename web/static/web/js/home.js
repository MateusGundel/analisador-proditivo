var app = angular.module('myApp', []);
app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
})

app.controller('myCtrl', function ($scope, $http) {
    // $scope.listItem = [{id: 0, esquerda: '', direita: ''}];
    $scope.listItem = [{id: 0, esquerda: "E", direita: "TE'"}, {id: 1, esquerda: "E'", direita: "+TE' | e"}, {id: 2, esquerda: "T", direita: "a"}];
    $scope.finalResult = "";
    $scope.isFinalResult = false;
    $scope.addItem = function () {
        $scope.listItem.push({id: $scope.listItem[$scope.listItem.length - 1]['id'] + 1, esquerda: '', direita: ''});
    }

    $scope.removeItem = function (id) {
        if ($scope.listItem.length > 1) {
            $scope.listItem.forEach(function (element, index) {
                if (element['id'] === id) {
                    console.log(index);
                    console.log(element['id']);
                    $scope.listItem.splice(index, 1)
                    console.log($scope.listItem)
                }
            });
        }
    }

    $scope.generate = function () {
        $.blockUI({message: 'Please Wait'});
        console.log($scope.listItem)
        $http({
            method: "POST",
            url: '/analisar/',
            data: {
                'gramatica': $scope.listItem
            },
            headers: {
                'Content-Type': undefined
            }
        }).then(function successCallback(response) {
                $scope.finalResult = JSON.parse(JSON.stringify(response.data));
                console.log($scope.finalResult)
                $scope.isFinalResult = true;
            }, function errorCallback(response) {
                console.log(response);
            });
        $.unblockUI();
    }
});