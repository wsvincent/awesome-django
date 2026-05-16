# Contribution Guidelines

Contributions are welcome! Please note that Will and Jeff work on this as a benefit to the Django community. It is based on our own personal, biased thoughts.

If you disagree with choices made, you are welcome to fork this repo and create/maintain your own list of awesome Django resources if you disagree with choices I've made.

That said, we will review any and all contributions. Here's the process:

1. Make an individual pull request for each suggestion and include a reason why it is awesome.
2. To be fair, the order is first-come-first-serve so unless a section is alphabetical, add the item at the end.
3. If you think something belongs in the wrong category, or think there needs to be a new category, feel free to edit things too.

## Site explorer data

The website uses `assets/awesome-django-projects.json` to add search, filtering, sorting, and GitHub repository metadata to the rendered list.

No extra contributor step is required when adding projects to `README.md`: after a README change is merged to `main`, GitHub Actions refreshes the generated data file automatically and commits it back to the repository.

Maintainers can also refresh the data manually from the Actions tab, or locally with:

```shell
GITHUB_TOKEN=<token> uv run scripts/main.py export-site-data
```

The token is optional locally, but recommended to avoid GitHub API rate limits while fetching stars, forks, creation dates, and latest commit timestamps.
