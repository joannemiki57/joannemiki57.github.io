// Theme toggle, mobile nav, and abstract/bibtex toggles.
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
  });
})();
