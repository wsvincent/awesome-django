/*
 * Anchor compatibility with the old Jekyll (kramdown) site.
 *
 * Python-Markdown and kramdown agree on 59 of the 61 heading anchors. These
 * two differ, so old bookmarks and external deep links are redirected here.
 */
var LEGACY_ANCHORS = {
  "awesome-django-": "awesome-django",
  "templates-1": "templates_1",
};

function resolveLegacyAnchor() {
  var hash = decodeURIComponent(window.location.hash.replace(/^#/, ""));
  if (!hash) return;

  var target = LEGACY_ANCHORS[hash];
  if (!target) return;

  var el = document.getElementById(target);
  if (!el) return;

  el.scrollIntoView();
  history.replaceState(null, "", "#" + target);
}

window.addEventListener("DOMContentLoaded", resolveLegacyAnchor);
window.addEventListener("hashchange", resolveLegacyAnchor);
