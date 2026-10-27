// Theme toggle, mobile nav, abstract/bibtex toggles, and the image viewer.
(function () {
  var root = document.documentElement;

  function storedTheme() {
    try { return localStorage.getItem("theme"); } catch (e) { return null; }
  }
  function setTheme(t) {
    root.setAttribute("data-theme", t);
    try { localStorage.setItem("theme", t); } catch (e) {}
  }
  var initial = storedTheme();
  if (initial) root.setAttribute("data-theme", initial);

  document.addEventListener("DOMContentLoaded", function () {
    var btn = document.querySelector(".theme-toggle");
    if (btn) {
      btn.addEventListener("click", function () {
        var current = root.getAttribute("data-theme");
        if (!current) {
          current = window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
        }
        setTheme(current === "dark" ? "light" : "dark");
      });
    }

    var navBtn = document.querySelector(".nav-toggle");
    var nav = document.querySelector(".nav-links");
    if (navBtn && nav) {
      navBtn.addEventListener("click", function () {
        var open = nav.classList.toggle("open");
        navBtn.setAttribute("aria-expanded", open ? "true" : "false");
      });
    }

    document.querySelectorAll("[data-toggle]").forEach(function (b) {
      b.addEventListener("click", function () {
        var target = document.getElementById(b.getAttribute("data-toggle"));
        if (!target) return;
        var li = b.closest("li");
        if (li) {
          li.querySelectorAll(".abstract, .bibtex").forEach(function (el) {
            if (el !== target) el.classList.remove("open");
          });
        }
        target.classList.toggle("open");
      });
    });

    // Click a figure, poster, or photo to see it full size.
    var images = document.querySelectorAll(".figure img, .pub-thumb, .gallery img");
    if (images.length) {
      var box = document.createElement("div");
      box.className = "lightbox";
      box.setAttribute("role", "dialog");
      box.setAttribute("aria-modal", "true");
      box.innerHTML = '<button class="lb-close" aria-label="Close">&times;</button><img alt=""><div class="lb-caption"></div>';
      document.body.appendChild(box);
      var boxImg = box.querySelector("img");
      var boxCap = box.querySelector(".lb-caption");
      var close = function () {
        box.classList.remove("open");
        document.body.style.overflow = "";
      };
      box.addEventListener("click", function (e) {
        if (e.target.tagName !== "A") close();
      });
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape") close();
      });
      images.forEach(function (img) {
        img.classList.add("zoomable");
        img.addEventListener("click", function () {
          var fig = img.closest("figure, .figure");
          var cap = fig && fig.querySelector("figcaption");
          boxImg.src = img.currentSrc || img.src;
          boxImg.alt = img.alt;
          boxCap.innerHTML = cap ? cap.innerHTML : img.alt;
          box.classList.add("open");
          document.body.style.overflow = "hidden";
        });
      });
    }
  });
})();
