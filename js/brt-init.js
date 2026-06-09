(function () {
  "use strict";

  var cssLink = document.querySelector("link[data-brt-css]");

  if (cssLink) {
    cssLink.addEventListener("error", function () {
      document.documentElement.classList.add("brt-css-fallback-mode");
    });
  }

  window.addEventListener("DOMContentLoaded", function () {
    var targetH1 = document.querySelector(".brt-h1");

    if (targetH1 && window.getComputedStyle(targetH1).fontSize === "32px") {
      document.documentElement.classList.add("brt-css-fallback-mode");
    }
  });
})();
