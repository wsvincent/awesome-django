# Awesome Django [![Awesome](https://awesome.re/badge-flat.svg)](https://github.com/sindresorhus/awesome)

<a class="github-fork-ribbon right-top" href="https://github.com/wsvincent/awesome-django" data-ribbon="Fork me on GitHub" title="Fork me on GitHub">Fork me on GitHub</a>

> A curated list of awesome things related to Django. Maintained by [William Vincent](https://github.com/wsvincent) and [Jeff Triplett](https://github.com/jefftriplett).

<br>

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/django-logo-negative.svg">
  <img alt="Dark and Light mode version of the Django logo" src="./assets/django-logo-positive.svg">
</picture>
</div>

<br>

Please consider supporting Django by making a donation to the <a rel="sponsored" href="https://www.djangoproject.com/fundraising/">Django Software Foundation</a>,
sponsoring via <a rel="sponsored" href="https://github.com/sponsors/django">GitHub Sponsors</a>,
or buying <a rel="sponsored" href="https://django.threadless.com/">official merchandise</a>.


## Contents

<!--lint disable awesome-toc-->
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Third-Party Packages](#third-party-packages)
  - [Admin](#admin)
  - [APIs](#apis)
  - [Async](#async)
  - [Caching](#caching)
  - [Commands](#commands)
  - [Configuration](#configuration)
  - [Content Management Systems](#content-management-systems)
  - [Database Connectors](#database-connectors)
  - [ECommerce](#ecommerce)
  - [Editors](#editors)
  - [Files/Images](#filesimages)
  - [Forms](#forms)
  - [Full-stack frameworks](#full-stack-frameworks)
  - [General](#general)
  - [Logging](#logging)
  - [Model Fields](#model-fields)
  - [Models](#models)
  - [Performance](#performance)
  - [Search](#search)
  - [Search Engine Optimisation](#search-engine-optimisation)
  - [Security](#security)
  - [Static Assets](#static-assets)
  - [Task Queues](#task-queues)
  - [Templates](#templates)
  - [Testing](#testing)
  - [URLs](#urls)
  - [Users](#users)
  - [Views](#views)
- [Python Packages](#python-packages)
- [Resources](#resources)
  - [Official Resources](#official-resources)
  - [Educational](#educational)
  - [Community](#community)
  - [Conferences](#conferences)
  - [Job Boards](#job-boards)
  - [Newsletters](#newsletters)
  - [Podcasts](#podcasts)
  - [Books](#books)
- [Hosting](#hosting)
  - [PaaS (Platforms-as-a-Service)](#paas-platforms-as-a-service)
  - [IaaS (Infrastructure-as-a-Service)](#iaas-infrastructure-as-a-service)
- [Projects](#projects)
  - [Boilerplate](#boilerplate)
  - [Open Source Projects](#open-source-projects)
- [Django REST Framework](#django-rest-framework)
  - [DRF Resources](#drf-resources)
  - [DRF Tutorials](#drf-tutorials)
- [Wagtail](#wagtail)
  - [Wagtail Resources](#wagtail-resources)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!--lint enable awesome-toc-->

## Third-Party Packages

_For a complete listing of all available packages, see [Django Packages](https://djangopackages.org/)_

### Admin
- [django-grappelli](https://github.com/sehmaschine/django-grappelli) - A jazzy skin for the admin.
- [django-jazzmin](https://github.com/farridav/django-jazzmin) - Drop-in theme for django admin, that utilises AdminLTE 3 & Bootstrap 4 to make yo' admin look jazzy.
- [django-hijack](https://github.com/arteria/django-hijack) - Admins can log in and work on behalf of other users without having to know their credentials.
- [django-import-export](https://github.com/django-import-export/django-import-export) - Django application and library for importing and exporting data with admin integration.
- [django-admin-honeypot](https://github.com/dmpayton/django-admin-honeypot) - Configure a honeypot to see who's trying to hack your site.
- [django-loginas](https://github.com/skorokithakis/django-loginas) - "Log in as user" for the Django admin.
- [impostor](https://github.com/avallbona/Impostor) - Impostor is a Django application which allows staff members to login as a different user by using their own username and password.
- [django-impersonate](https://pypi.org/project/django-impersonate/) - Allow superusers to “impersonate” other non-superuser accounts.
- [django-admin-env-notice](https://github.com/dizballanze/django-admin-env-notice) - Visually distinguish environments in Django Admin, for example: `development`, `staging`, `production`.
- [django-admin-interface](https://github.com/fabiocaccamo/django-admin-interface) - Customize Admin by the admin itself(color, header. title,logo) and  popup windows replaced by modals.
- [django-material-admin](https://github.com/MaistrenkoAnton/django-material-admin) - Material design for django administration.
- [django-related-admin](https://github.com/PetrDlouhy/django-related-admin) - A helper library that allows you to write list_displays accross foreign key relationships.
- [django-semantic-admin](https://github.com/globophobe/django-semantic-admin) - Django Semantic UI admin theme.
- [django-jet-reboot](https://github.com/b1go/django-jet-reboot) - Django Jet is modern template for Django admin interface with improved functionality.
- [django-baton](https://github.com/otto-torino/django-baton) - A cool, modern and responsive django admin application based on bootstrap 5.
- [django-admin-sortable2](https://github.com/jrief/django-admin-sortable2) - Generic drag-and-drop ordering for objects in the Django admin interface.

### APIs
<!--lint disable double-link-->
- [django-rest-framework](https://github.com/encode/django-rest-framework) - Web APIs for Django.
- [django-cors-headers](https://github.com/adamchainz/django-cors-headers) - If your back-end and front-end are on different servers, you need this.
- [dj-rest-auth](https://github.com/jazzband/dj-rest-auth) - Authentication for Django Rest Framework.
- [django-rest-knox](https://github.com/James1345/django-rest-knox) - Authentication Module for django-rest-auth.
- [djoser](https://github.com/sunscrapers/djoser) - REST implementation of Django auth.
- [djaq](https://github.com/paul-wolf/djaq) - An instant remote API to Django models with a powerful query language.
- [django-rest-framework-simplejwt](https://github.com/davesque/django-rest-framework-simplejwt) - JSON web tokens for DRF.
- [django-webpack-loader](https://github.com/owais/django-webpack-loader) - Transparently use webpack with Django.
- [drf-yasg](https://github.com/axnsan12/drf-yasg) - Automated generation of real Swagger/OpenAPI 2.0 schemas from Django REST Framework code.
- [graphene-django](https://github.com/graphql-python/graphene-django) - GraphQL for Django.
- [graphene-django-filter](https://github.com/devind-team/graphene-django-filter) - Advanced filters implementing and/or/not operators in GraphQL for Django.
- [django-ninja](https://django-ninja.rest-framework.com/) - Django Ninja - Fast Django REST framework based on type annotations.
- [django-tastypie](https://github.com/django-tastypie/django-tastypie) - Creating delicious APIs for Django apps since 2010.
- [drf-spectacular](https://github.com/tfranzel/drf-spectacular) - Sane and flexible OpenAPI 3 schema generation for Django REST framework.
<!--lint enable double-link-->

### Async
- [channels](https://github.com/django/channels/) - Async support for Django.
- [starlette](https://github.com/encode/starlette) - ASGI framework.

### Caching
- [django-cachalot](https://github.com/noripyt/django-cachalot) - Caches your Django ORM queries and automatically invalidates them.
- [django-cacheops](https://github.com/Suor/django-cacheops) - A slick ORM cache with automatic granular event-driven invalidation.

### Commands
- [django-extensions](https://github.com/django-extensions/django-extensions/) - Custom management extensions, notably `runserver_plus` and `shell_plus`.
- [django-click](https://github.com/GaretJax/django-click) - Write Django management commands using the click CLI library.
- [django-dbbackup](https://github.com/django-dbbackup/django-dbbackup) - Management commands to help backup and restore your project database and media files.
- [django-liquidb](https://github.com/Gusakovskiy/django-liquidb) - Django application to simplify migration management and changes in states of db scheme.

### Configuration
<!--lint disable double-link-->
- [confidential](https://github.com/candidco/confidential) - Manage configs and secrets (with CLI support).
- [django-environ](https://github.com/joke2k/django-environ) - Environment variables.
- [django-split-settings](https://github.com/sobolevn/django-split-settings) - Organize multiple settings files.
- [django-constance](https://github.com/jazzband/django-constance) - A Django app for storing dynamic settings in pluggable backends (Redis and Django model backend built in) with an integration with the Django admin app.
- [django-configurations](https://github.com/jazzband/django-configurations) - eases Django project configuration by relying on the composability of Python classes and following principles of [the twelve-factor app](https://12factor.net/config).
- [dynaconf](https://www.dynaconf.com/django/) - Dynaconf loads django settings from multiple sources (multiple file formats, env vars, redis, vault, etcd), manages secrets, and allows for different merging strategies all following [the twelve-factor app](https://12factor.net/config).
- [django-extra-settings](https://github.com/fabiocaccamo/django-extra-settings) - Config and manage typed extra settings using just the django admin.
- [environs](https://github.com/sloria/environs) - Simplified environment variable parsing that comes with a [Django helper](https://github.com/sloria/environs#usage-with-django) that installs additional packages.
<!--lint enable double-link-->
- [django-classy-settings](https://github.com/funkybob/django-classy-settings) - Class based settings to keep your environments in order, with easy access to typed environment variables.

### Content Management Systems
<!--lint disable double-link-->
- [wagtail](https://github.com/wagtail/wagtail) - Popular Django content management system (CMS). See [awesome-wagtail](https://github.com/springload/awesome-wagtail) too.
- [mezzanine](https://github.com/stephenmcd/mezzanine) - CMS framework.
- [django-cms](https://github.com/divio/django-cms) - CMS for Django.
- [feincms](https://github.com/feincms/feincms) - An extensible Django-based CMS.
- [puput](https://github.com/APSL/puput) - Blog app features with Wagtail.
<!--lint enable double-link-->

### Database Connectors
- [djongo](https://github.com/doableware/djongo) - Django and MongoDB database connector.

### ECommerce
- [saleor](https://github.com/mirumee/saleor) - GraphQL-based Django E-Commerce Platform.
- [django-shop](https://github.com/awesto/django-shop) - Django-based shop system.
- [shuup](https://github.com/shuup/shuup) - Django E-Commerce Platform.
- [django-oscar](https://github.com/django-oscar/django-oscar) - Domain-driven e-commerce for Django.

### Editors
<!--lint ignore awesome-list-item-->
- [django-ckeditor](https://github.com/shaunsephton/django-ckeditor) - Django admin CKEditor integration.
- [django-markdownx](https://github.com/adi-/django-markdownx) - Comprehensive Markdown plugin built for Django.
- [django-markdown-editor](https://github.com/agusmakmun/django-markdown-editor) - Awesome Django Markdown Editor, supported for Bootstrap & Semantic-UI.
- [django-business-logic](https://github.com/dgk/django-business-logic) - Visual DSL framework for Django.
- [django-quill-editor](https://github.com/LeeHanYeong/django-quill-editor) - Makes Quill.js easy to use on Django Forms and admin sites.
- [django-summernote](https://github.com/summernote/django-summernote) - Summernote is a simple WYSIWYG editor.
- [django-tinymce](https://github.com/jazzband/django-tinymce) - TinyMCE integration for Django.
- [django-prose](https://github.com/withlogicco/django-prose) - A light weight editor to content creation.
- [django-ace](https://github.com/django-ace/django-ace) - ACE integration for Django.

### Files/Images
- [django-cleanup](https://github.com/un1t/django-cleanup) - Zero configuration file/image removal for local and remote files.
- [django-imagekit](https://github.com/matthewwithanm/django-imagekit) - Django app for processing images for thumbnail, black-and-white and sizes.
- [django-pictures](https://github.com/codingjoe/django-pictures) - Responsive cross-browser image library using modern codes like AVIF & WebP.
- [sorl-thumbnail](https://github.com/jazzband/sorl-thumbnail) - Thumbnails for Django.

### Forms
- [django-bleach](https://github.com/marksweb/django-bleach/) - Integrate bleach into forms and models. See `django-nh3` as an alternative.
- [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms/) - DRY Django forms.
- [django-floppyforms](https://github.com/jazzband/django-floppyforms) - Full control of form rendering.
- [django-formtools](https://github.com/jazzband/django-formtools) - For form previous and multi-step forms, previously part of Django until 1.8.
- [django-widget-tweaks](https://github.com/jazzband/django-widget-tweaks) - Tweak form field rendering in templates.
- [django-autocomplete-light](https://github.com/yourlabs/django-autocomplete-light) - Add autocompletion to forms.
- [django-shapeshifter](https://github.com/kennethlove/django-shapeshifter) - A class-based view to handle multiple forms in one view.

### Full-stack frameworks
- [ReactPy](https://github.com/reactive-python/reactpy) - It's React, but in Python. Insert dynamically rendered Python into Django templates using the [ReactPy-Django module](https://github.com/reactive-python/reactpy-django).
- [Reactor](https://github.com/edelvalle/reactor/) - Phoenix LiveView, but for Django.
- [Sockpuppet](https://sockpuppet.argpar.se/) - Build reactive applications with the Django tooling you already know and love.
- [Unicorn](https://www.django-unicorn.com/) - A reactive component framework that progressively enhances a normal Django view, makes AJAX calls in the background, and dynamically updates the DOM.
- [iommi](https://github.com/TriOptima/iommi) - Toolkit for development of CRUD applications without writing HTML or JavaScript.

### General
- [django-data-browser](https://github.com/tolomea/django-data-browser) - Interactive, user-friendly database explorer.
- [django-filter](https://github.com/carltongibson/django-filter) - Powerful filters based on Django QuerySets.
- [django-guardian](https://github.com/django-guardian/django-guardian) - Per object permissions in Django.
- [django-sql-explorer](https://github.com/groveco/django-sql-explorer) - Share data via SQL queries.
- [django-tables2](https://github.com/jieter/django-tables2) - HTML tables with pagination/sorting.
- [django-maintenance-mode](https://github.com/fabiocaccamo/django-maintenance-mode) - Shows a 503 error page when maintenance-mode is on.
- [django-freeze](https://github.com/fabiocaccamo/django-freeze) - Convert your dynamic django site to a static one with one line of code.
- [django-nh3](https://github.com/marksweb/django-nh3) - Django integration with for nh3 and is an alternative for django-bleach.
- [Weblate](https://github.com/WeblateOrg/weblate) - Weblate is a copylefted libre software web-based continuous localization system, used by over 2500 libre projects and companies in more than 165 countries.

### Logging
- [django-guid](https://github.com/JonasKs/django-guid) - Inject a GUID (Correlation-ID) into every log message in a Django request.
- [DRF-API-Logger](https://github.com/vishalanandl177/DRF-API-Logger) - An API Logger for your Django Rest Framework project.

### Model Fields
- [django-any-urlfield](https://github.com/edoburu/django-any-urlfield) - An improved URL selector to choose between internal models and external URLs.
- [django-colorfield](https://github.com/fabiocaccamo/django-colorfield) - Color field for django models with a nice color-picker widget.
- [django-model-utils](https://github.com/jazzband/django-model-utils) - Django model mixins and utilities.
- [django-money](https://github.com/django-money/django-money) - Money fields for forms/models.
- [django-phonenumber-field](https://github.com/stefanfoulis/django-phonenumber-field) - Model/form field for normalized phone numbers.
- [django-streamfield](https://github.com/raagin/django-streamfield) - Simple StreamField for plain Django admin (based on Wagtail CMS StreamField idea).

### Models
- [django-lifecycle](https://github.com/rsinger86/django-lifecycle) - Declarative model lifecycle hooks, an alternative to Signals.
- [django-mptt](https://github.com/django-mptt/django-mptt) - Modified Preorder Tree Traversal; working with trees of Model instances.
- [django-taggit](https://github.com/jazzband/django-taggit/) - Simple model tags.
- [django-reversion](https://github.com/etianen/django-reversion) - Version control for model instances.
- [django-simple-history](https://github.com/jazzband/django-simple-history) - Store model history and view/revert changes from the admin.
- [django-polymorphic](https://github.com/django-polymorphic/django-polymorphic) - Django-polymorphic simplifies using inherited models in Django projects.
- [django-recurrence](https://github.com/django-recurrence/django-recurrence) - Utility for working with recurring dates in Django.
- [django-treenode](https://github.com/fabiocaccamo/django-treenode) - Abstract model/admin for tree based stuff.

### Performance
- [django-perf-rec](https://cur.at/GHUO6cn?m=web) - Keep detailed records of the performance of your Django code.
- [New Relic](https://newrelic.com/python/django) - Time middleware, views, and SQL queries.
- [Scout](https://docs.scoutapm.com/#django) - Time middleware, template rendering, and SQL queries with automatic N+1 detection.
- [django-query-profiler](https://github.com/django-query-profiler/django-query-profiler) - Django query profiler to help resolve N+1 queries.
- [django-silk](https://github.com/jazzband/django-silk) - Live profiling and inspection of HTTP requests and database queries.
- [py-spy](https://github.com/benfred/py-spy) - Sampling profiler for Python programs.
- [pyinstrument](https://github.com/joerick/pyinstrument) - Call stack profiler for Python, Django, Flask, FastAPI.

### Search
- [django-haystack](https://github.com/django-haystack/django-haystack) - Modular search for Django.
- [django-watson](https://github.com/etianen/django-watson) - Full-text search plugin.
- [django-admin-search](https://github.com/shinneider/django-admin-search) - Modal filter for django admin.
- [django-elasticsearch-dsl](https://github.com/django-es/django-elasticsearch-dsl) - Elasticsearch DSL integration for Django.

### Search Engine Optimisation
- [django-check-seo](https://github.com/kapt-labs/django-check-seo) - Check SEO of pages.

### Security
- [django-csp](https://github.com/mozilla/django-csp) - Adds [Content-Security-Policy](http://www.w3.org/TR/CSP/) headers to Django.
- [django-feature-policy](https://github.com/adamchainz/django-feature-policy) - Set the draft security HTTP header `Feature-Policy` on a Django app.
- [django-protected-media](https://github.com/cobusc/django-protected-media) - Manages media that are considered sensitive in a protected fashion.
- [DJ Checkup](https://djcheckup.com) - Runs several checks on your deployed Django site to check for common security mistakes.

### Static Assets
- [django-storages](https://github.com/jschneier/django-storages) - A single library to support multiple custom storage backends for Django.
- [django-compressor](https://github.com/django-compressor/django-compressor/) - Compress JavaScript/CSS into a single cached file.
- [easy-thumbnails](https://github.com/SmileyChris/easy-thumbnails) - Image thumbnails for Django.
- [whitenoise](https://github.com/evansd/whitenoise) - Simplified static file serving for Python websites.

### Task Queues
- [beatserver](https://github.com/rajasimon/beatserver) - A periodic task scheduler for Django.
- [django-q](https://github.com/Koed00/django-q) - A multiprocessing distributed task queue.
- [django-rq](https://github.com/rq/django-rq) - Integration for Redis Queue.
- [django-redis](https://github.com/niwinz/django-redis) - Full-featured Redis cache backend for Django.
- [celery](https://github.com/celery/celery) - Robust and broker-agnostic task queues for bigger, performance-focused projects.
- [flower](https://github.com/mher/flower) - Flower is a web-based tool for monitoring and administrating Celery clusters.
- [django-celery-beat](https://github.com/celery/django-celery-beat) - A periodic task scheduler with database configured by Django's Admin Panel.
- [celery-exporter](https://github.com/danihodovic/celery-exporter) - Prometheus & Grafana monitoring of Celery tasks.
- [django-dramatiq](https://github.com/Bogdanp/django_dramatiq) - Task processing library with a focus on simplicity, reliability, and performance.

### Templates

- [curlylint](https://www.curlylint.org/) - Experimental HTML templates linting for Jinja, Nunjucks, Django templates, Twig, Liquid.
- [django-components](https://github.com/EmilStenstrom/django-components/) - A way to create simple reusable template components in Django.
- [django-template-partials](https://github.com/carltongibson/django-template-partials/) - Reusable named inline partials for the Django Template Language.
- [djhtml](https://github.com/rtts/djhtml) - Django/Jinja template indenter.
- [djlint](https://www.djlint.com/) - Lint & Format HTML Templates.
- [slippers](https://mitchel.me/slippers/) - Build reusable components in Django without writing a single line of Python.
- [JinjaX](https://jinjax.scaletti.dev/) - Super components powers for your Jinja templates.

### Testing
- [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar/) - Configurable panels to debug requests/responses.
- [pytest-django](https://github.com/pytest-dev/pytest-django) - Use pytest features in Django.
- [django-test-migrations](https://github.com/wemake-services/django-test-migrations) - Test django schema and data migrations, including migrations' order.
- [django-test-plus](https://github.com/revsys/django-test-plus/) - Useful additions to Django's default TestCase.
- [factory-boy](https://github.com/FactoryBoy/factory_boy) - Test fixtures replacement.
- [django-waffle](https://github.com/django-waffle/django-waffle) - A feature flipper for Django.
- [model-bakery](https://github.com/model-bakers/model_bakery) - Object factory for Django (rename of legacy Model Mommy project).
- [django-fakery](https://github.com/fcurella/django-fakery) - An easy-to-use implementation of Creation Methods for Django, backed by Faker.
- [drf-openapi-tester](https://github.com/snok/drf-openapi-tester) - Django test utility for validating Swagger 2.0 and OpenAPI 3.0 documentation.
- [django-google-optimize](https://github.com/adinhodovic/django-google-optimize) - Django application designed to make running server side Google Optimize A/B tests easy.
- [django-pattern-library](https://github.com/torchbox/django-pattern-library) - Pattern library generator for Django templates, to help testing of UI components.
- [storybook-django](https://github.com/torchbox/storybook-django) - Develop Django UI components in isolation, with Storybook.

### URLs
- [dj-database-url](https://github.com/jacobian/dj-database-url) - Database URLs.
- [urlman](https://github.com/andrewgodwin/urlman) - A nicer way to do URLs for Django models.
- [django-robots](https://github.com/jazzband/django-robots) - This is a basic Django application to manage robots.txt files following the robots exclusion protocol, complementing the Django Sitemap contrib app.
- [django-redirects](https://github.com/fabiocaccamo/django-redirects) - Redirects as they should be, with full control.

### Users
- [django-allauth](https://github.com/pennersr/django-allauth/) - Improved user registration including social auth.
- [django-allauth-ui](https://github.com/danihodovic/django-allauth-ui/) - Better looking templates for django-allauth.
- [django-improved-user](https://github.com/jambonsw/django-improved-user) - A custom Django user that authenticates via email. Follows identity and authentication best practices.
- [django-organizations](https://github.com/bennylope/django-organizations/) - Multi-user accounts for Django projects.
- [django-cas-ng](https://github.com/django-cas-ng/django-cas-ng) - Django-cas-ng is Django CAS (Central Authentication Service) 1.0/2.0/3.0 client library to support SSO (Single Sign On) and Single Logout (SLO).

### Views
- [django-braces](https://github.com/brack3t/django-braces) - Reusable, generic mixins.
- [django-easy-audit](https://github.com/soynatan/django-easy-audit) - Keep track of user actions.
- [django-extra-views](https://github.com/AndrewIngram/django-extra-views) - Extra class-based generic views.
- [django-vanilla-views](https://github.com/tomchristie/django-vanilla-views) - Simpler class-based views in Django.
- [django-stronghold](https://github.com/mgrouchy/django-stronghold) - Makes all your Django views default login_required.

## Python Packages

_A short list of Python packages that work well with Django._

- [bleach](https://github.com/mozilla/bleach) - Sanitize your inputs/forms.
- [black](https://github.com/psf/black) - Uncompromising Python code formatter.
- [coveragepy](https://github.com/nedbat/coveragepy) - Code coverage measurement.
- [faker](https://github.com/joke2k/faker) - Faker is a Python package that generates fake data for you.
- [huey](https://github.com/coleifer/huey) - A little task queue for Python.
- [nplusone](https://github.com/jmcarp/nplusone) - Auto-detect n+1 queries.
- [pillow](https://github.com/python-pillow/Pillow) - Python Imaging Library.
- [pytest](https://github.com/pytest-dev/pytest/) - Testing framework.
- [python-decouple](https://github.com/henriquebastos/python-decouple) - Strict separation of settings from code.
- [python-slugify](https://github.com/un33k/python-slugify) - Returns unicode slugs.
- [sentry-python](https://github.com/getsentry/sentry-python) - Error reporting SDK.
- [python-socketio](https://github.com/miguelgrinberg/python-socketio) - Python implementation of the Socket.IO_ realtime client and server. [(create Socket.io Django server instance)](https://python-socketio.readthedocs.io/en/latest/server.html?highlight=django#creating-a-server-instance)

## Resources

### Official Resources

<!--lint ignore double-link--> 
- [Project Website](https://www.djangoproject.com/) - Official Django website.
- [Documentation](https://docs.djangoproject.com/en/dev/) - Comprehensive documentation for all Django versions.
- [Polls Tutorial](https://docs.djangoproject.com/en/dev/intro/tutorial01/) - Build a polls tutorial while learning Django internals.
- [Source Code](https://github.com/django/django/) - Hosted on GitHub.

### Educational

- [Django Girls Tutorial](https://tutorial.djangogirls.org/en/) - Use function-based views to build a blog app.
- [LearnDjango](https://learndjango.com/) - Tutorials and premium courses on Django and Django REST Framework.
- [Adam Johnson](https://adamj.eu/tech/) - Adam is on the Technical Board of Django and regularly writes tutorials.
- [💡 Photon Designer - Django tutorials](https:/photondesigner.com/articles) - Django tutorials by Tom Dekan on how to build Django apps simply - from how to build an instant messenger with Django, add instant search, to using Google Drive as a database. Updated regularly.     
- [TestDriven](https://testdriven.io/blog/) - Multiple Django-specific tutorials on topics like Docker, payments, and more.
- [Classy Class-Based Views](https://ccbv.co.uk/) - Detailed descriptions of methods/properties/attributes for each generic class-based view.
- [Classy Django Forms](https://github.com/ana-balica/classy-django-forms) - Detailed descriptions of methods/properties/attributes for each form class.
- [Classy Django REST Framework](http://www.cdrf.co) - Detailed descriptions with methods/attributes for DRF class-based views and serializers.
- [Simple is Better than Complex](https://simpleisbetterthancomplex.com/) - Regularly updated website with many tutorials and tips on Django.
- [Full Stack Python's Django Page](https://www.fullstackpython.com/django.html) - Explanation of Django philosophy and links to other resources and tutorials.
- [RealPython](https://realpython.com/tutorials/django/) - Many high-quality tutorials on Django.
- [Mozilla Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django) - Create a lending library app.
- [Matt Layman](https://www.mattlayman.com) - Regular tutorials and deep-dives on Django topics.
- [Django Sites](https://www.djangosites.org/) - Comprehensive listing of sites built with Django.
- [Django Styleguide](https://github.com/HackSoftware/Django-Styleguide) - Styleguide for Django with best practices and examples.
- [Django Template Tags and Filters](https://www.djangotemplatetagsandfilters.com/) - Additional docs on Django's 57 built-in template filters and 27 template tags.
- [Django for Everybody](https://www.dj4e.com/) - A complete course for webdev beginners focused on Django.
- [CS50W](https://cs50.harvard.edu/web/2020/) - Harvard's University introductory course to web development, it explains Django as backend framework.

### Community

<!--lint disable double-link-->
- [Django Forum](https://forum.djangoproject.com/) - Official Discourse board.
- [Community Page](https://www.djangoproject.com/community/) - Featuring feeds of Community Blog Posts, Jobs, and more.
- [Django Users Google Group](https://groups.google.com/forum/#!forum/django-users/) - Very active discussion board for questions/answers.
- [Developers Google Group](https://groups.google.com/forum/#!forum/django-developers/) - For contributions to Django itself only.
- [Mastodon](https://fosstodon.org/@django) - For official announcements on updates, security fixes, etc.
- [Twitter](https://twitter.com/djangoproject/) - For official announcements on updates, security fixes, etc.
- [Discord Server](https://discord.com/invite/xcRH6mN4fa) - Django Discord Community.
- IRC Channel - Chat with other Django users at irc://irc.freenode.net/django.
<!--lint enable double-link-->

### Conferences

- [DjangoCon US](https://djangocon.us/) ([YouTube Channel](https://www.youtube.com/channel/UC0yY6a79pPY9J0ShIHRf6yw))
- [DjangoCon Europe](https://djangocon.eu/) ([YouTube Channel](https://www.youtube.com/user/djangoconeurope))
- [DjangoCon AU](https://djangocon.com.au/)
- [DjangoCon Africa](https://djangocon.africa/)
- [Django Day Copenhagen](https://github.com/wsvincent/awesome-django#conferences)
- [PyCon US](https://us.pycon.org/2020/) ([YouTube Channel](https://www.youtube.com/channel/UCsX05-2sVSH7Nx3zuk3NYuQ))
- [PyCon Australia](https://2019.pycon-au.org/) ([YouTube Channel](https://www.youtube.com/user/PyConAU))
- [Euro Python](https://ep2019.europython.eu/) ([YouTube Channel](https://www.youtube.com/user/PythonItalia))
- [Django Under the Hood](https://www.youtube.com/channel/UC9T1dhIlL_8Va9DxvKRowBw/videos)
- [Complete listing of all PyCons globally](https://pycon.org)

### Job Boards

- [Django News Jobs](https://jobs.django-news.com/) - A Django job board that also aggregates other job boards.
- [Django Gigs](https://djangogigs.com) - This platform caters specifically to freelance and full-time Django developers. 
- [Django Jobs](https://djangojobs.net) - Django jobs posting for hiring Django Python developers.
- [Python.org Job Boards](https://www.python.org/jobs/) - While not exclusively for Django, this job board is hosted by the official Python website and features a range of Python and Django-related job opportunities.

### Newsletters

- [Django News](https://django-news.com) - Weekly newsletter on announcements, articles, projects, and talks.

### Podcasts

- [Django Chat](https://djangochat.com/) - A weekly podcast from William Vincent and Django Fellow Carlton Gibson with discussions of core Django concepts and regular guests.
- [Django Riffs](https://djangoriffs.com) - A new podcast from Matt Layman.
- [Running in Production](https://runninginproduction.com/tags/django) - Focused on tech stacks with many episodes specifically on Django.
- [TalkPython](https://talkpython.fm/) - The leading Python podcast with several episodes on Django.
- [Podcast Init](https://www.pythonpodcast.com/) - A popular Python podcast that features Django guests on occasion.


### Books

_Django 4.2_
- [Django for Beginners: Build websites with Python and Django](https://djangoforbeginners.com/)

_Django 4.0_
- [Boost Your Django DX](https://adamchainz.gumroad.com/l/byddx)
- [Django for APIs: Build web APIs with Python and Django](https://djangoforapis.com/)
- [Django for Professionals: Production websites with Python and Django](https://djangoforprofessionals.com/)
- [Django 4 By Example: Build powerful and reliable Python web applications from scratch](https://www.amazon.com/dp/1801813051/)

_Django 3.2_
- [Speed Up Your Django Tests](https://adamj.eu/tech/2020/05/04/new-book-speed-up-your-django-tests/)
- [Two Scoops of Django 3.x: Best Practices for the Django Web Framework](https://www.feldroy.com/books/two-scoops-of-django-3-x)
- [A Wedge of Django: Covers Python 3.8 and Django 3.x](https://www.feldroy.com/books/a-wedge-of-django)


## Hosting

### PaaS (Platforms-as-a-Service)
- [Appliku](https://appliku.com)
- [Dokku](https://dokku.com)
- [Divio](https://www.divio.com)
- [Fly](https://fly.io)
- [Google Cloud](https://cloud.google.com/python/django/)
- [Heroku](https://www.heroku.com)
- [Microsoft Azure](https://azure.microsoft.com/en-us/develop/python/)
- [Platform.sh](https://platform.sh)
- [PythonAnywhere](https://www.pythonanywhere.com)
- [Railway](https://railway.app)
- [Render](https://render.com)
- [Vercel](https://vercel.com/home)

### IaaS (Infrastructure-as-a-Service)
- [Digital Ocean](https://www.digitalocean.com)
- [Linode](https://www.linode.com)
- [Amazon Lightsail](https://aws.amazon.com/lightsail/)
- [Hetzner](https://www.hetzner.com)

## Projects

### Boilerplate
- [cookiecutter-django](https://github.com/pydanny/cookiecutter-django/) - A full-bodied starter project, highly customizable.
- [django-base-site](https://github.com/epicserve/django-base-site/) - A Django site with many common third-party packages pre-installed.
- [djangox](https://github.com/wsvincent/djangox/) - Batteries included starter project for Pip, Pipenv, or Docker.
- [DRFx](https://github.com/wsvincent/drfx/) - A DRF starter with user auth, Pipenv, and other goodies.
- [django-project-template](https://github.com/jpadilla/django-project-template) - A deliberately basic project that has multiple staging environments and Heroku deployment config.
- [docker-django](https://github.com/erroneousboat/docker-django/) - A quick starter guide for Django and Docker together.
- [django-docker-template](https://github.com/amerkurev/django-docker-template) - Dockerized Django with Postgres, Gunicorn, and Traefik (with auto renew Let's Encrypt).
- [django-startproject](https://github.com/jefftriplett/django-startproject) - Django start project template with batteries.
- [wemake-django-template](https://github.com/wemake-services/wemake-django-template/) - Bleeding edge Django template focused on code quality and security.
- [django-webpack-starter](https://github.com/khadegd/django-webpack-starter) - Django Webpack starter template for using Webpack 4.
- [sos-django-template](https://github.com/erayerdin/sos-django-template) - Django starter template with separate dev and production settings.
- [django-docker-heroku-template](https://github.com/bfirsh/django-docker-heroku-template) - A template with Docker, GitHub Actions, and Heroku set up for dev/test/prod, plus various other best practices.
- [cookiecutter-vue-django](https://github.com/ilikerobots/cookiecutter-vue-django) - Django + Vue starter project fusing Vue SFCs & Django Templates.
- [launchr](https://github.com/jayfk/launchr) - Launchr is a specialized Django starter template for SaaS web apps.
- [sidewinder](https://github.com/stribny/sidewinder/) - A Django starter kit that focuses on good defaults, developer experience, and deployment. 

### Open Source Projects
- [Blog app with users and forms](https://github.com/wsvincent/djangoforbeginners/tree/master/ch7-blog-app-with-users/)
- [Newspaper app with custom user model, full user auth](https://github.com/wsvincent/djangoforbeginners/tree/master/ch15-comments)
- [pythonic-news](https://github.com/sebst/pythonic-news) - Hacker News clone.
- [Behavior-Driven Development with Aloe](https://github.com/testdrivenio/django-aloe-bdd/)
- [Image Sharing Blog](https://github.com/MeNsaaH/soMedia)
- [Bootcamp: An enterprise social network](https://github.com/vitorfs/bootcamp)
- [Zulip](https://github.com/zulip/zulip/) - Open-source team chat.
- [Django-CRM](https://github.com/MicroPyramid/Django-CRM/) - Open Source Python CRM based on Django.
- [django-job-portal](https://github.com/manjurulhoque/django-job-portal) - Job portal application using Django.
- [Built with Django](https://builtwithdjango.com) - Curated list of awesome Django projects.
- [PostHog](https://github.com/PostHog/posthog) - Open-source product analytics.
- [HyperKitty](https://gitlab.com/mailman/hyperkitty) - A web interface to access GNU Mailman v3 archives.
- [Healthchecks](https://github.com/healthchecks/healthchecks) - A Cron Monitoring Tool written in Python & Django.
- [Flagsmith](https://github.com/Flagsmith/flagsmith) - Open-source Feature Flagging, Remote Config, and AB testing.

## Django REST Framework

_The most popular way to build web APIs with Django._

### DRF Resources

<!--lint disable double-link-->
- [Official Documentation](https://www.django-rest-framework.org/)
- [DRF Source Code](https://github.com/encode/django-rest-framework)
- [awesome-django-rest-framework](https://github.com/nioperas06/awesome-django-rest-framework)
<!--lint enable double-link-->

### DRF Tutorials

<!--lint ignore double-link-->
- [Official REST Framework - A Beginner's Guide](https://learndjango.com/tutorials/official-django-rest-framework-tutorial-beginners)
- [Building APIs with Django and DRF](https://books.agiliq.com/projects/django-api-polls-tutorial/en/latest/)
- [DRF with React](https://www.valentinog.com/blog/drf/)
- [Making React and Django play well together](https://fractalideas.com/blog/making-react-and-django-play-well-together/)

## Wagtail

_Wagtail, the powerful CMS for modern websites._

### Wagtail Resources
<!--lint disable double-link-->
- [Official website](https://wagtail.org/)
- [Developer documentation](https://docs.wagtail.org/en/stable/)
- [User documentation](https://guide.wagtail.org/en-latest/)
- [Wagtail Source Code](https://github.com/wagtail/wagtail/)
- [awesome-wagtail](https://github.com/springload/awesome-wagtail)
- [This week in Wagtail](https://wagtail.org/this-week-in-wagtail/) - A (most) weekly email with updates from the Wagtail core team.
- [Wagtail Space](https://www.wagtail.space/) - Wagtail CMS events around the world.
<!--lint enable double-link-->
