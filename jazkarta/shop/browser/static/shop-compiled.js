require(["jquery"],function(a){var b=a(body).data("portal-url");a(document).on("click",".jaz-shop-add",function(c){c.preventDefault();var d=a(this).attr("data-uid");a.post(b+"/shopping-cart",{add:d},function(b){a(".jaz-shop-cart-wrapper").replaceWith(b)},"html")})}),define("/Users/davisagli/Work/jazkarta.com/src/jazkarta.shop/jazkarta/shop/browser/static/shop.js",function(){});
//# sourceMappingURL=shop-compiled.js.map