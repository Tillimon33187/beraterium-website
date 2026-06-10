(function () {
  "use strict";

  function fileProtocolHref(href) {
    if (!href || href.charAt(0) === "#") return href;
    if (/^(https?:|mailto:|tel:)/i.test(href)) return href;

    var hash = "";
    var query = "";
    var path = href;
    var hashAt = path.indexOf("#");
    if (hashAt !== -1) {
      hash = path.slice(hashAt);
      path = path.slice(0, hashAt);
    }
    var queryAt = path.indexOf("?");
    if (queryAt !== -1) {
      query = path.slice(queryAt);
      path = path.slice(0, queryAt);
    }

    if (/\.html$/i.test(path)) return href;
    if (path === "." || path === "./") path = "./index.html";
    else if (path === ".." || path === "../") path = "../index.html";
    else if (path.slice(-1) === "/") path = path + "index.html";
    else if (!/\.[a-zA-Z0-9]{2,8}$/.test(path)) path = path.replace(/\/?$/, "/") + "index.html";

    return path + query + hash;
  }

  function initFileProtocolLinks() {
    if (location.protocol !== "file:") return;

    document.addEventListener("click", function (e) {
      var link = e.target.closest("a[href]");
      if (!link) return;
      if (link.classList.contains("site-header__parent-link") && !window.matchMedia("(min-width: 1024px)").matches) {
        return;
      }
      var href = link.getAttribute("href");
      if (!href) return;
      var rewritten = fileProtocolHref(href);
      if (rewritten === href) return;
      e.preventDefault();
      location.href = new URL(rewritten, location.href).href;
    }, true);
  }

  function revealHashTargetContent(target) {
    if (!target) return;
    target.querySelectorAll(".brt-fade-up, .brt-stagger > *").forEach(function (el) {
      el.classList.add("is-visible");
      el.style.transitionDelay = "0ms";
    });
  }

  function scrollToTeamSection(section) {
    if (!section) return;

    revealHashTargetContent(section);

    var header = document.querySelector(".site-header");
    var headerH = header ? header.getBoundingClientRect().height : 84;
    var scrollTarget = section.querySelector(".brt-split__media") || section;
    var gap = 32;
    var offset = headerH + gap;
    var rectTop = scrollTarget.getBoundingClientRect().top;
    var y = rectTop + window.pageYOffset - offset;
    window.scrollTo(0, Math.max(0, y));
  }

  function scrollToAnchorHash() {
    var hash = location.hash;
    if (!hash || hash.length < 2) return;
    var target = document.getElementById(decodeURIComponent(hash.slice(1)));
    if (!target) return;
    scrollToTeamSection(target);
  }

  function scheduleAnchorScroll() {
    scrollToAnchorHash();
    requestAnimationFrame(function () {
      scrollToAnchorHash();
      requestAnimationFrame(scrollToAnchorHash);
    });
  }

  function scheduleTeamSectionScroll(section) {
    requestAnimationFrame(function () {
      scrollToTeamSection(section);
      requestAnimationFrame(function () {
        scrollToTeamSection(section);
      });
    });
  }

  function getHomeTeamScrollY(section) {
    var scrollTarget = section.querySelector(".brt-section__header") || section;
    var header = document.querySelector(".site-header");
    var headerH = header ? header.getBoundingClientRect().height : 84;
    var gap = 32;
    return Math.max(0, scrollTarget.getBoundingClientRect().top + window.pageYOffset - (headerH + gap));
  }

  function scrollToHomeTeamSectionInstant(section) {
    if (!section) return;
    revealHashTargetContent(section);
    window.scrollTo(0, getHomeTeamScrollY(section));
  }

  function initHomeTeamToggle() {
    document.querySelectorAll(".brt-home-team__toggle").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var list = document.getElementById("home-team-cards");
        if (!list) return;
        var more = list.querySelectorAll(".brt-home-team__card--more");
        if (!more.length) return;
        var section = list.closest("section");
        var expanded = btn.getAttribute("aria-expanded") === "true";
        var next = !expanded;
        btn.setAttribute("aria-expanded", next ? "true" : "false");
        btn.textContent = next
          ? btn.getAttribute("data-less-label") || "Weniger anzeigen"
          : btn.getAttribute("data-more-label") || "Mehr anzeigen";
        if (next) {
          more.forEach(function (card) {
            card.hidden = false;
          });
          more[0].scrollIntoView({ behavior: "smooth", block: "nearest" });
        } else {
          scrollToHomeTeamSectionInstant(section);
          more.forEach(function (card) {
            card.hidden = true;
          });
          scrollToHomeTeamSectionInstant(section);
          requestAnimationFrame(function () {
            scrollToHomeTeamSectionInstant(section);
          });
        }
      });
    });
  }

  function initTeamBioToggle() {
    document.querySelectorAll(".brt-team-bio__toggle").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var bio = btn.closest(".brt-team-bio");
        if (!bio) return;
        var more = bio.querySelector(".brt-team-bio__more");
        if (!more) return;
        var section = bio.closest("section[id]");
        var expanded = btn.getAttribute("aria-expanded") === "true";
        var next = !expanded;
        more.hidden = !next;
        btn.setAttribute("aria-expanded", next ? "true" : "false");
        btn.textContent = next
          ? btn.getAttribute("data-less-label") || "Weniger anzeigen"
          : btn.getAttribute("data-more-label") || "Mehr anzeigen";
        if (!next) {
          scheduleTeamSectionScroll(section);
        }
      });
    });
  }

  function initBerateriumSite() {
    initHomeTeamToggle();
    initTeamBioToggle();

    if (location.hash) {
      if ("scrollRestoration" in history) history.scrollRestoration = "manual";
      window.scrollTo(0, 0);
    }

    var root = document.querySelector(".brt");
    var header = document.querySelector(".site-header");
    var navToggle = document.querySelector(".site-header__toggle");
    var nav = document.querySelector("#site-nav");
    var prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var menuMq = window.matchMedia("(min-width: 1024px)");
    var isInnerPage = document.body.classList.contains("brt-page--inner");

    function updateHeaderState() {
      if (!header) return;
      if (isInnerPage) {
        header.classList.add("site-header--solid");
        return;
      }
      var shouldBeSolid = window.scrollY > 20 || (nav && nav.classList.contains("is-open"));
      header.classList.toggle("site-header--solid", shouldBeSolid);
    }

    if (navToggle && nav) {
      function closeMobileNav() {
        navToggle.setAttribute("aria-expanded", "false");
        nav.classList.remove("is-open");
        document.body.classList.remove("is-nav-open");
        if (header) header.classList.remove("site-header--menu-open");
        document.querySelectorAll(".site-header__item--has-menu.is-submenu-open").forEach(function (item) {
          item.classList.remove("is-submenu-open");
          var link = item.querySelector(".site-header__parent-link");
          if (link) link.setAttribute("aria-expanded", "false");
        });
        updateHeaderState();
      }

      function toggleMobileSubmenu(item, link) {
        if (!item.classList.contains("is-submenu-open")) {
          document.querySelectorAll(".site-header__item--has-menu.is-submenu-open").forEach(function (openItem) {
            if (openItem === item) return;
            openItem.classList.remove("is-submenu-open");
            var openLink = openItem.querySelector(".site-header__parent-link");
            if (openLink) openLink.setAttribute("aria-expanded", "false");
          });
          item.classList.add("is-submenu-open");
          link.setAttribute("aria-expanded", "true");
        } else {
          item.classList.remove("is-submenu-open");
          link.setAttribute("aria-expanded", "false");
        }
      }

      navToggle.addEventListener("click", function () {
        var expanded = navToggle.getAttribute("aria-expanded") === "true";
        navToggle.setAttribute("aria-expanded", expanded ? "false" : "true");
        nav.classList.toggle("is-open", !expanded);
        document.body.classList.toggle("is-nav-open", !expanded);
        if (header) header.classList.toggle("site-header--menu-open", !expanded);
        if (expanded) {
          document.querySelectorAll(".site-header__item--has-menu.is-submenu-open").forEach(function (item) {
            item.classList.remove("is-submenu-open");
            var link = item.querySelector(".site-header__parent-link");
            if (link) link.setAttribute("aria-expanded", "false");
          });
        }
        updateHeaderState();
      });

      nav.addEventListener("click", function (e) {
        if (menuMq.matches) return;
        var link = e.target.closest("a[href]");
        if (!link || !nav.contains(link)) return;

        if (link.classList.contains("site-header__parent-link")) {
          e.preventDefault();
          e.stopPropagation();
          var item = link.closest(".site-header__item--has-menu");
          if (!item) return;
          toggleMobileSubmenu(item, link);
          return;
        }

        closeMobileNav();
      }, true);

      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape" && nav.classList.contains("is-open")) closeMobileNav();
      });

      menuMq.addEventListener("change", function () {
        if (menuMq.matches) closeMobileNav();
      });
    }

    document.querySelectorAll(".site-header__item--has-menu").forEach(function (item) {
      var link = item.querySelector(".site-header__parent-link");
      if (!link) return;

      function syncDesktopExpanded() {
        if (!menuMq.matches) return;
        var hovered = item.matches(":hover") || item.matches(":focus-within");
        link.setAttribute("aria-expanded", hovered ? "true" : "false");
      }

      item.addEventListener("mouseenter", syncDesktopExpanded);
      item.addEventListener("mouseleave", syncDesktopExpanded);
      item.addEventListener("focusin", syncDesktopExpanded);
      item.addEventListener("focusout", syncDesktopExpanded);
    });

    window.addEventListener("scroll", updateHeaderState, { passive: true });
    updateHeaderState();

    if (location.hash) {
      scheduleAnchorScroll();
      window.addEventListener("load", scheduleAnchorScroll);
    }
    window.addEventListener("hashchange", scheduleAnchorScroll);

    if (!root) return;

    root.querySelectorAll(".brt-legal, .brt-hero .brt-fade-up").forEach(function (el) {
      el.classList.add("is-visible");
    });

    function reveal(entries, observer) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        if (entry.target.classList.contains("brt-stagger")) {
          Array.prototype.forEach.call(entry.target.children, function (child, i) {
            child.style.transitionDelay = i * 80 + "ms";
            child.classList.add("is-visible");
          });
        }
        if (entry.target.querySelector(".brt-stagger")) {
          var stagger = entry.target.querySelector(".brt-stagger");
          Array.prototype.forEach.call(stagger.children, function (child, i) {
            child.style.transitionDelay = i * 80 + "ms";
            child.classList.add("is-visible");
          });
        }
        observer.unobserve(entry.target);
      });
    }

    if (!prefersReduced && "IntersectionObserver" in window) {
      var io = new IntersectionObserver(reveal, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });
      root.querySelectorAll(".brt-fade-up, .brt-stagger").forEach(function (el) {
        if (el.closest(".brt-hero")) return;
        io.observe(el);
      });
      root.querySelectorAll(".brt-stagger > *").forEach(function (el) {
        if (el.closest(".brt-hero")) return;
        io.observe(el);
      });
    } else {
      root.querySelectorAll(".brt-fade-up, .brt-stagger > *").forEach(function (el) {
        el.classList.add("is-visible");
      });
    }

    if (!prefersReduced) {
      root.querySelectorAll("[data-count]").forEach(function (el) {
        var target = parseInt(el.getAttribute("data-count"), 10);
        var suffix = el.getAttribute("data-suffix") || "";
        if (isNaN(target)) return;

        var counted = false;
        function animateCount() {
          if (counted) return;
          counted = true;
          var start = performance.now();
          var duration = 1200;
          function tick(now) {
            var p = Math.min((now - start) / duration, 1);
            el.textContent = Math.round(target * p) + suffix;
            if (p < 1) requestAnimationFrame(tick);
          }
          requestAnimationFrame(tick);
        }

        if ("IntersectionObserver" in window) {
          var statIo = new IntersectionObserver(function (entries, obs) {
            if (entries[0].isIntersecting) {
              animateCount();
              obs.disconnect();
            }
          }, { threshold: 0.5 });
          statIo.observe(el);
        }
      });
    }

    var filters = document.querySelector(".brt-blog-filters");
    var grid = document.getElementById("blog-grid-list");
    if (filters && grid) {
      filters.addEventListener("click", function (e) {
        var link = e.target.closest("a[data-filter]");
        if (!link) return;
        e.preventDefault();
        var filter = link.getAttribute("data-filter");
        filters.querySelectorAll("a").forEach(function (a) {
          a.classList.toggle("is-active", a === link);
        });
        grid.querySelectorAll("[data-category]").forEach(function (card) {
          var cat = card.getAttribute("data-category");
          card.hidden = !(filter === "alle" || cat === filter);
        });
      });
    }

    initArticleToc();
  }

  function initArticleToc() {
    var toc = document.querySelector("[data-article-toc]");
    if (!toc) return;

    var links = toc.querySelectorAll('a[href^="#"]');
    if (!links.length) return;

    var headings = [];
    links.forEach(function (link) {
      var id = link.getAttribute("href").slice(1);
      var el = document.getElementById(id);
      if (el) headings.push({ link: link, el: el });
    });
    if (!headings.length) return;

    function setActive(activeLink) {
      links.forEach(function (link) {
        link.classList.toggle("is-active", link === activeLink);
      });
    }

    if ("IntersectionObserver" in window) {
      var visible = new Map();
      var observer = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) visible.set(entry.target, entry.intersectionRatio);
            else visible.delete(entry.target);
          });
          if (!visible.size) return;
          var best = null;
          var bestRatio = -1;
          visible.forEach(function (ratio, el) {
            if (ratio >= bestRatio) {
              bestRatio = ratio;
              best = el;
            }
          });
          if (!best) return;
          headings.forEach(function (item) {
            if (item.el === best) setActive(item.link);
          });
        },
        { rootMargin: "-20% 0px -55% 0px", threshold: [0, 0.25, 0.5, 0.75, 1] }
      );
      headings.forEach(function (item) {
        observer.observe(item.el);
      });
    }

    links.forEach(function (link) {
      link.addEventListener("click", function (e) {
        var id = link.getAttribute("href").slice(1);
        var target = document.getElementById(id);
        if (!target) return;
        e.preventDefault();
        var header = document.querySelector(".site-header");
        var offset = (header ? header.getBoundingClientRect().height : 84) + 24;
        var y = target.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top: Math.max(0, y), behavior: "smooth" });
        setActive(link);
      });
    });
  }

  initFileProtocolLinks();

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initBerateriumSite);
  } else {
    initBerateriumSite();
  }
})();
