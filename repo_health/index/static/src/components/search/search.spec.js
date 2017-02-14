describe('Search', () => {
  beforeEach(module('components.search'));

  describe('SearchController', () => {
    let $componentController;
    let controller;

    beforeEach(inject(($injector) => {
      $componentController = $injector.get('$componentController');
      controller = $componentController('search');
    }));

    describe('constructor', () => {
      it('should setup the controller', () => {
        expect(controller).toBeDefined;
      });
    });

    describe('getStats', () => {
      it('should return the stats', () => {
        //Add tests when function is implemented
      });
    });
  });
});