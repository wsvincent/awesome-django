/* Enhance the shared README without changing its GitHub presentation. */
(function () {
  function enhanceDirectory() {
    var article = document.querySelector(".md-content__inner");
    if (!article || article.dataset.directoryReady) return;
    var contents = article.querySelector("#contents");
    if (!contents) return;
    article.dataset.directoryReady = "true";

    var toc = contents.nextElementSibling;
    var firstHeading = toc && toc.nextElementSibling;
    while (firstHeading && firstHeading.tagName !== "H2") {
      firstHeading = firstHeading.nextElementSibling;
    }
    if (!firstHeading) return;

    var controls = document.createElement("div");
    controls.className = "awesome-django-controls";
    controls.id = "contents";
    controls.innerHTML =
      '<div class="awesome-django-filter"><label for="directory-filter">Filter packages and resources</label>' +
    '<div class="awesome-django-filter__input"><input id="directory-filter" type="search" placeholder="Search names and descriptions…" aria-controls="directory-results">' +
    '<button type="button" id="directory-clear">Clear</button></div></div>' +
    '<div class="awesome-django-jump"><label for="directory-category">Jump to category</label>' +
    '<select id="directory-category"><option value="">Choose a category…</option></select></div>' +
    '<p class="awesome-django-result-count" role="status" aria-live="polite" aria-atomic="true"></p>';
    contents.replaceWith(controls);
    if (toc && toc.tagName === "UL") toc.remove();
    new ResizeObserver(function () {
      article.style.setProperty("--directory-controls-height", controls.getBoundingClientRect().height + "px");
    }).observe(controls);

    var contribution = document.createElement("p");
    contribution.className = "awesome-django-contribute";
    var link = document.createElement("a");
    link.href = "https://github.com/wsvincent/awesome-django/blob/main/.github/pull_request_template.md";
    link.textContent = "Suggest a project";
    contribution.append(link, " — read the submission criteria before opening a pull request.");
    article.querySelector("blockquote").after(contribution);
    article.querySelectorAll(":scope > p").forEach(function (p) {
      if (!p.textContent.trim() && p.querySelector("br")) p.classList.add("awesome-django-spacer");
    });

    var results = document.createElement("div");
    results.id = "directory-results";
    firstHeading.before(results);
    var group;
    var section;
    var node = firstHeading;
    while (node) {
      var next = node.nextSibling;
      if (node.nodeType === 1 && node.tagName === "H2") {
        group = document.createElement("section");
        group.className = "awesome-django-group";
        group.setAttribute("aria-labelledby", node.id);
        results.append(group);
        section = group;
      } else if (node.nodeType === 1 && node.tagName === "H3") {
        section = document.createElement("section");
        section.className = "awesome-django-category";
        section.setAttribute("aria-labelledby", node.id);
        group.append(section);
      }
      section.append(node);
      node = next;
    }

    var entries = Array.from(results.querySelectorAll("li"));
    var categories = Array.from(results.querySelectorAll("section"));
    var select = controls.querySelector("select");
    var counts = {};
    results.querySelectorAll("h2, h3").forEach(function (heading) {
      var label = heading.cloneNode(true);
      label.querySelectorAll(".headerlink").forEach(function (a) { a.remove(); });
      var count = heading.parentElement.querySelectorAll("li").length;
      counts[heading.id] = count;
      var option = document.createElement("option");
      option.value = heading.id;
      option.textContent = (heading.tagName === "H3" ? "　" : "") + label.textContent.trim() + " (" + count + ")";
      select.append(option);
    });

    var input = controls.querySelector("input");
    var status = controls.querySelector("[role=status]");
    var empty = document.createElement("p");
    empty.textContent = "No matching entries. Try another term or clear the filter.";
    empty.hidden = true;
    results.after(empty);
    function filter() {
      var terms = input.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
      var visible = 0;
      entries.forEach(function (entry) {
        var text = entry.textContent.toLowerCase();
        entry.hidden = !terms.every(function (term) { return text.includes(term); });
        if (!entry.hidden) visible++;
      });
      categories.forEach(function (category) {
        category.hidden = !Array.from(category.querySelectorAll("li")).some(function (entry) { return !entry.hidden; });
      });
      status.textContent = terms.length ? visible + " of " + entries.length + " entries match" : entries.length + " packages and resources";
      empty.hidden = visible !== 0;
    }
    input.addEventListener("input", filter);
    controls.querySelector("button").addEventListener("click", function () {
      input.value = "";
      filter();
      input.focus();
    });
    select.addEventListener("change", function () {
      if (!select.value) return;
      input.value = "";
      filter();
      var target = document.getElementById(select.value);
      window.location.hash = select.value;
      target.setAttribute("tabindex", "-1");
      target.focus({ preventScroll: true });
      target.scrollIntoView();
    });

    var disclosures = [];
    document.querySelectorAll('[data-md-component="toc"] a.md-nav__link').forEach(function (a) {
      var id = a.hash.slice(1);
      if (id === "contents") {
        a.closest("li").remove();
        return;
      }
      if (counts[id] === undefined) return;
      var badge = document.createElement("span");
      badge.className = "awesome-django-nav-count";
      badge.textContent = counts[id];
      badge.setAttribute("aria-label", counts[id] + " entries");
      a.append(badge);
      var nav = a.parentElement.querySelector(":scope > nav");
      if (!nav) return;
      var button = document.createElement("button");
      button.type = "button";
      button.className = "awesome-django-nav-toggle";
      button.textContent = "⌄";
      button.setAttribute("aria-label", "Toggle " + nav.getAttribute("aria-label") + " categories");
      nav.id = "directory-nav-" + id;
      button.setAttribute("aria-controls", nav.id);
      function setExpanded(expanded) {
        nav.hidden = !expanded;
        button.setAttribute("aria-expanded", String(expanded));
      }
      setExpanded(id === "third-party-packages");
      button.addEventListener("click", function () { setExpanded(nav.hidden); });
      a.after(button);
      a.parentElement.classList.add("awesome-django-nav-group");
      disclosures.push({ nav: nav, expand: function () { setExpanded(true); } });
    });
    function revealAnchor() {
      var id;
      try { id = decodeURIComponent(window.location.hash.slice(1)); } catch (_) { return; }
      var target = document.getElementById(id);
      if (target && results.contains(target) && input.value) {
        input.value = "";
        filter();
      }
      disclosures.forEach(function (item) {
        if (Array.from(item.nav.querySelectorAll("a")).some(function (a) { return a.hash === "#" + id; })) item.expand();
      });
    }
    window.addEventListener("hashchange", revealAnchor);
    filter();
    revealAnchor();

    var picture = article.querySelector("picture");
    if (picture) {
      var logo = picture.querySelector("img");
      var source = picture.querySelector("source");
      var light = logo.getAttribute("src");
      var dark = source.getAttribute("srcset");
      source.remove();
      logo.alt = "Django";
      function syncLogo() {
        var scheme = document.querySelector("[data-md-color-scheme]");
        logo.src = scheme && scheme.getAttribute("data-md-color-scheme") === "slate" ? dark : light;
      }
      syncLogo();
      new MutationObserver(syncLogo).observe(document.documentElement, {
        attributes: true, subtree: true, attributeFilter: ["data-md-color-scheme"],
      });
    }
  }
  if (typeof document$ !== "undefined") document$.subscribe(enhanceDirectory);
  else if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", enhanceDirectory);
  else enhanceDirectory();
})();
