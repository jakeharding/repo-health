(function () {
    angular.module('app')
        .controller('HomeCtrl', Home)

    function Home () {
        var vm = this;
        vm.msg = "This rendered inside angular."
    }
})();