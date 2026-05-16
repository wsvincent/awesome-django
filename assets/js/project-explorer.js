(() => {
  const script = document.currentScript;
  const projectsUrl = script?.dataset?.projectsUrl || '/assets/awesome-django-projects.json';
  const state = {
    projects: [],
    projectByUrl: new Map(),
    items: [],
    originalOrder: new WeakMap(),
  };

  const normalizeUrl = (url) => {
    try {
      const parsed = new URL(url, window.location.origin);
      parsed.hash = '';
      parsed.search = '';
      return parsed.href.replace(/\/$/, '').toLowerCase();
    } catch (_error) {
      return String(url || '').replace(/\/$/, '').toLowerCase();
    }
  };

  const formatNumber = (value) => {
    if (value === null || value === undefined) return null;
    return new Intl.NumberFormat('en', { notation: value >= 10000 ? 'compact' : 'standard' }).format(value);
  };

  const daysAgo = (dateValue) => {
    if (!dateValue) return null;
    const date = new Date(dateValue);
    if (Number.isNaN(date.getTime())) return null;
    return Math.floor((Date.now() - date.getTime()) / 86400000);
  };

  const formatRelativeDate = (dateValue) => {
    const days = daysAgo(dateValue);
    if (days === null) return null;
    if (days < 1) return 'today';
    if (days < 31) return `${days}d ago`;
    if (days < 365) return `${Math.round(days / 30)}mo ago`;
    return `${Math.round(days / 365)}y ago`;
  };

  const findInsertionPoint = () => {
    const headings = [...document.querySelectorAll('main h2, .main-content h2, h2')];
    return headings.find((heading) => heading.id === 'third-party-packages' || heading.textContent.trim() === 'Third-Party Packages');
  };

  const createExplorer = (data) => {
    const categories = [...new Set(data.projects.map((project) => project.category).filter(Boolean))].sort((a, b) => a.localeCompare(b));
    const panel = document.createElement('section');
    panel.className = 'awesome-django-explorer';
    panel.setAttribute('aria-labelledby', 'awesome-django-explorer-title');
    panel.innerHTML = `
      <h2 id="awesome-django-explorer-title">Explore Awesome Django</h2>
      <p class="awesome-django-explorer__intro">
        Search, filter, and sort the curated list. GitHub projects include stars, forks, creation date, and latest commit data where available.
      </p>
      <div class="awesome-django-explorer__controls">
        <div class="awesome-django-explorer__field">
          <label for="awesome-django-search">Search projects</label>
          <input id="awesome-django-search" type="search" placeholder="Try “admin”, “async”, “wagtail”…" autocomplete="off" />
        </div>
        <div class="awesome-django-explorer__field">
          <label for="awesome-django-category">Category</label>
          <select id="awesome-django-category">
            <option value="">All categories</option>
            ${categories.map((category) => `<option value="${category.replace(/"/g, '&quot;')}">${category}</option>`).join('')}
          </select>
        </div>
        <div class="awesome-django-explorer__field">
          <label for="awesome-django-sort">Sort within sections</label>
          <select id="awesome-django-sort">
            <option value="original">Original curation order</option>
            <option value="stars">Most GitHub stars</option>
            <option value="recent">Latest commit</option>
            <option value="created">Newest repositories</option>
            <option value="name">Name A-Z</option>
          </select>
        </div>
        <div class="awesome-django-explorer__field">
          <label for="awesome-django-min-stars">Minimum stars</label>
          <input id="awesome-django-min-stars" type="number" inputmode="numeric" min="0" step="100" placeholder="0" />
        </div>
        <label class="awesome-django-explorer__checkbox">
          <input id="awesome-django-github-only" type="checkbox" /> GitHub projects only
        </label>
        <label class="awesome-django-explorer__checkbox">
          <input id="awesome-django-active-only" type="checkbox" /> Active in last year
        </label>
      </div>
      <p id="awesome-django-status" class="awesome-django-explorer__status" aria-live="polite"></p>
    `;
    return panel;
  };

  const decorateItem = (item, project) => {
    if (!project || item.querySelector('.awesome-django-meta')) return;
    const meta = document.createElement('span');
    meta.className = 'awesome-django-meta';

    const details = [];
    if (project.stars !== null && project.stars !== undefined) details.push(`★ ${formatNumber(project.stars)}`);
    if (project.forks !== null && project.forks !== undefined) details.push(`⑂ ${formatNumber(project.forks)}`);
    if (project.latest_commit) details.push(`commit ${formatRelativeDate(project.latest_commit)}`);
    if (project.created_at) details.push(`since ${new Date(project.created_at).getFullYear()}`);
    if (project.archived) details.push('archived');

    meta.innerHTML = details.slice(0, 5).map((detail) => `<span class="awesome-django-meta__item">${detail}</span>`).join('');
    if (meta.children.length) item.appendChild(meta);
  };

  const collectItems = () => {
    const items = [...document.querySelectorAll('li')]
      .map((li) => {
        const link = li.querySelector('a[href]');
        if (!link) return null;
        const project = state.projectByUrl.get(normalizeUrl(link.href));
        if (!project) return null;
        return { li, link, project, text: `${project.name} ${project.description} ${project.category} ${(project.topics || []).join(' ')}`.toLowerCase() };
      })
      .filter(Boolean);

    items.forEach((entry, index) => {
      state.originalOrder.set(entry.li, index);
      decorateItem(entry.li, entry.project);
    });

    state.items = items;
  };

  const hideEmptyLists = () => {
    const lists = [...new Set(state.items.map((entry) => entry.li.parentElement))].filter(Boolean);
    lists.forEach((list) => {
      const visibleItems = [...list.children].filter((child) => child.matches('li') && !child.classList.contains('awesome-django-hidden'));
      list.classList.toggle('awesome-django-hidden', visibleItems.length === 0);

      const previous = list.previousElementSibling;
      if (previous && /^H[23]$/.test(previous.tagName)) {
        previous.classList.toggle('awesome-django-hidden', visibleItems.length === 0);
      }
    });
  };

  const sortLists = (sortValue) => {
    const lists = [...new Set(state.items.map((entry) => entry.li.parentElement))].filter(Boolean);
    const byElement = new Map(state.items.map((entry) => [entry.li, entry]));

    lists.forEach((list) => {
      const children = [...list.children];
      const sortable = children.filter((child) => byElement.has(child));
      const staticChildren = children.filter((child) => !byElement.has(child));

      sortable.sort((a, b) => {
        const left = byElement.get(a).project;
        const right = byElement.get(b).project;
        if (sortValue === 'stars') return (right.stars || -1) - (left.stars || -1);
        if (sortValue === 'recent') return new Date(right.latest_commit || 0) - new Date(left.latest_commit || 0);
        if (sortValue === 'created') return new Date(right.created_at || 0) - new Date(left.created_at || 0);
        if (sortValue === 'name') return left.name.localeCompare(right.name);
        return state.originalOrder.get(a) - state.originalOrder.get(b);
      });

      [...sortable, ...staticChildren].forEach((child) => list.appendChild(child));
    });
  };

  const applyFilters = () => {
    const query = document.getElementById('awesome-django-search').value.trim().toLowerCase();
    const category = document.getElementById('awesome-django-category').value;
    const sortValue = document.getElementById('awesome-django-sort').value;
    const minStars = Number(document.getElementById('awesome-django-min-stars').value || 0);
    const githubOnly = document.getElementById('awesome-django-github-only').checked;
    const activeOnly = document.getElementById('awesome-django-active-only').checked;

    sortLists(sortValue);

    let visible = 0;
    state.items.forEach(({ li, project, text }) => {
      const activeDays = daysAgo(project.latest_commit || project.pushed_at);
      const matches = (!query || text.includes(query))
        && (!category || project.category === category)
        && (!githubOnly || project.is_github)
        && (!minStars || (project.stars || 0) >= minStars)
        && (!activeOnly || (activeDays !== null && activeDays <= 365));

      li.classList.toggle('awesome-django-hidden', !matches);
      if (matches) visible += 1;
    });

    hideEmptyLists();
    const enriched = state.projects.filter((project) => project.stars !== null && project.stars !== undefined).length;
    document.getElementById('awesome-django-status').textContent = `${visible} of ${state.items.length} entries shown · ${enriched} with GitHub metrics · data refreshed ${new Date(state.generatedAt).toLocaleDateString()}`;
  };

  const init = async () => {
    const insertionPoint = findInsertionPoint();
    if (!insertionPoint) return;

    let data;
    try {
      const response = await fetch(projectsUrl, { cache: 'force-cache' });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      data = await response.json();
    } catch (error) {
      console.warn('Awesome Django explorer could not load project data:', error);
      return;
    }

    state.projects = data.projects || [];
    state.generatedAt = data.generated_at;
    state.projectByUrl = new Map();
    state.projects.forEach((project) => {
      state.projectByUrl.set(normalizeUrl(project.url), project);
      (project.previous_urls || []).forEach((url) => state.projectByUrl.set(normalizeUrl(url), project));
    });

    const explorer = createExplorer(data);
    insertionPoint.parentElement.insertBefore(explorer, insertionPoint);
    collectItems();

    explorer.addEventListener('input', applyFilters);
    explorer.addEventListener('change', applyFilters);
    applyFilters();
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
