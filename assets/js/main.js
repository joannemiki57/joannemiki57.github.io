// Theme toggle, mobile nav, abstract/bibtex toggles, life graph, and the image viewer.
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

    // Life graph on the about page.
    document.querySelectorAll(".journey").forEach(function (box) {
      var data = JSON.parse(box.querySelector(".jg-data").textContent);
      var pts = box.querySelectorAll(".jg-pt");
      var card = box.querySelector(".jg-card");
      var el = function (c) { return card.querySelector(c); };
      var cur = parseInt(box.getAttribute("data-start"), 10) || 0;
      function show(i) {
        cur = (i + data.length) % data.length;
        var d = data[cur];
        el(".jg-date").textContent = d.date + (d.place && d.place !== "?" ? " · " + d.place : "");
        el(".jg-kind").textContent = d.kind;
        el(".jg-title").textContent = d.title;
        el(".jg-text").textContent = d.text;
        el(".jg-count").textContent = (cur + 1) + " / " + data.length;
        card.classList.toggle("twist", d.kind === "plot twist");
        card.classList.toggle("turn", d.kind === "turning point");
        pts.forEach(function (p, k) { p.classList.toggle("active", k === cur); });
      }
      pts.forEach(function (p, k) {
        p.addEventListener("click", function () { show(k); });
        p.addEventListener("mouseenter", function () { if (window.matchMedia("(hover: hover)").matches) show(k); });
      });
      el(".jg-prev").addEventListener("click", function () { show(cur - 1); });
      el(".jg-next-btn").addEventListener("click", function () { show(cur + 1); });
      box.addEventListener("keydown", function (e) {
        if (e.key === "ArrowLeft") { show(cur - 1); e.preventDefault(); }
        if (e.key === "ArrowRight") { show(cur + 1); e.preventDefault(); }
      });
      show(cur);

      // Draw the curve once it scrolls into view.
      var line = box.querySelector(".jg-line");
      var still = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      if (line && line.getTotalLength && !still && "IntersectionObserver" in window) {
        var len = line.getTotalLength();
        line.style.strokeDasharray = len;
        line.style.strokeDashoffset = len;
        var io = new IntersectionObserver(function (entries) {
          if (!entries[0].isIntersecting) return;
          line.style.transition = "stroke-dashoffset 1.6s ease-out";
          line.style.strokeDashoffset = 0;
          io.disconnect();
        }, { threshold: 0.35 });
        io.observe(box);
      }
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
