(function() {
    'use strict';

    var requirejsOptions = {
        baseUrl: '++theme++sdswas/',
        optimize: 'none',
    }

    if (typeof exports !== 'undefined' && typeof module !== 'undefined') {
        module.exports = requirejsOptions;
    }
    if (typeof requirejs !== 'undefined' && requirejs.config) {
        requirejs.config(requirejsOptions);
    }

    requirejs([
        'main-min',
    ], function($, _bootstrap) {
        (function($) {
            var menu = $(".menu-container");
            menu.find(".menu-btn").removeClass("menu-btn-selected");
            menu.find("#products-btn .menu-btn").addClass("menu-btn-selected");

        })(jQuery);
    });
}());