---
---
<div align="center">
  <a href="https://github.com/sindresorhus/awesome#readme"><img src="https://awesome.re/badge-flat.svg" /></a><br>
  <img width="400" src="./assets/django-logo.svg" alt="Django logo">
</div>

# Awesome Django
> A curated list of awesome things related to Django. Maintained by <a rel="" href="https://github.com/wsvincent">William Vincent</a> and <a rel="" href="https://github.com/jefftriplett">Jeff Triplett</a>.

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
  - [ECommerce](#ecommerce)
  - [Editors](#editors)
  - [Files/Images](#filesimages)
  - [Forms](#forms)
  - [General](#general)
  - [Logging](#logging)
  - [Models](#models)
  - [Performance](#performance)
  - [Search](#search)
  - [Security](#security)
  - [Static Assets](#static-assets)
  - [Task Queues](#task-queues)
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
- [django-admin-env-notice](https://github.com/dizballanze/django-admin-env-notice) - Visually distinguish environments in Django Admin, for example: `development`, `staging`, `production`.
- [django-admin-interface](https://github.com/fabiocaccamo/django-admin-interface) - Customize Admin by the admin itself(color, header. title,logo) and  popup windows replaced by modals.
- [django-material-admin](https://github.com/MaistrenkoAnton/django-material-admin) - Material design for django administration 

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
- [django-ninja](https://django-ninja.rest-framework.com/) - Django Ninja - Fast Django REST framework based on type annotations.
- [django-tastypie](https://github.com/django-tastypie/django-tastypie) - Creating delicious APIs for Django apps since 2010.
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

### Configuration
- [confidential](https://github.com/candidco/confidential) - Manage configs and secrets (with CLI support).
- [django-environ](https://github.com/joke2k/django-environ) - Environment variables.
- [django-split-settings](https://github.com/sobolevn/django-split-settings) - Organize multiple settings files.
- [django-constance](https://github.com/jazzband/django-constance) - A Django app for storing dynamic settings in pluggable backends (Redis and Django model backend built in) with an integration with the Django admin app.
- [djenv](https://github.com/danieljdufour/djenv) - Load Django settings from environmental variables.
- [django-configurations](https://github.com/jazzband/django-configurations) - eases Django project configuration by relying on the composability of Python classes and following principles of [the twelve-factor app](https://12factor.net/config).

### Content Management Systems
<!--lint disable double-link-->
- [wagtail](https://github.com/wagtail/wagtail) - Popular Django content management system (CMS). See [awesome-wagtail](https://github.com/springload/awesome-wagtail) too.
- [mezzanine](https://github.com/stephenmcd/mezzanine) - CMS framework.
- [django-cms](https://github.com/divio/django-cms) - CMS for Django.
- [feincms](https://github.com/feincms/feincms) - An extensible Django-based CMS.
- [puput](https://github.com/APSL/puput) - Blog app features with Wagtail.
<!--lint enable double-link-->

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
- [django-wysiwyg-redactor](https://github.com/douglasmiranda/django-wysiwyg-redactor) - A lightweight wysiwyg editor for Django.
- [django-business-logic](https://github.com/dgk/django-business-logic) - Visual DSL framework for django.
- [django-quill-editor](https://github.com/LeeHanYeong/django-quill-editor) - django-quill-editor makes Quill.js easy to use on Django Forms and admin sites.
- [django-summernote](https://github.com/summernote/django-summernote) - Summernote is a simple WYSIWYG editor.

### Files/Images
- [django-cleanup](https://github.com/un1t/django-cleanup) - Zero configuration file/image removal for local and remote files.

### Forms
- [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms/) - DRY Django forms.
- [django-floppyforms](https://github.com/jazzband/django-floppyforms) - Full control of form rendering.
- [django-formtools](https://github.com/jazzband/django-formtools) - For form previous and multi-step forms, previously part of Django until 1.8.
- [django-widget-tweaks](https://github.com/jazzband/django-widget-tweaks) - Tweak form field rendering in templates.
- [django-autocomplete-light](https://github.com/yourlabs/django-autocomplete-light) - Add autocompletion to forms.
- [django-shapeshifter](https://github.com/kennethlove/django-shapeshifter) - A CBV to handle multiple forms in one view.

### General
- [django-filter](https://github.com/carltongibson/django-filter) - Powerful filters based on Django QuerySets.
- [django-guardian](https://github.com/django-guardian/django-guardian) - Per object permissions in Django.
- [django-sql-explorer](https://github.com/groveco/django-sql-explorer) - Share data via SQL queries.
- [django-tables2](https://github.com/jieter/django-tables2) - HTML tables with pagination/sorting.

### Logging
- [django-guid](https://github.com/JonasKs/django-guid) - Inject a GUID (Correlation-ID) into every log message in a Django request.

### Models
- [django-fakery](https://github.com/fcurella/django-fakery) - An easy-to-use implementation of Creation Methods for Django, backed by Faker.
- [django-lifecycle](https://github.com/rsinger86/django-lifecycle) - Declarative model lifecycle hooks, an alternative to Signals.
- [django-model-utils](https://github.com/jazzband/django-model-utils) - Django model mixins and utilities.
- [django-money](https://github.com/django-money/django-money) - Money fields for forms/models.
- [django-phonenumber-field](https://github.com/stefanfoulis/django-phonenumber-field) - Model/form field for normalized phone numbers.
- [django-taggit](https://github.com/jazzband/django-taggit/) - Simple model tags.
- [django-reversion](https://github.com/etianen/django-reversion) - Version control for model instances.
- [django-simple-history](https://github.com/treyhunner/django-simple-history) - Store model history and view/revert changes from the admin.
- [django-polymorphic](https://github.com/django-polymorphic/django-polymorphic) - Django-polymorphic simplifies using inherited models in Django projects.

### Performance
- [django-perf-rec](https://cur.at/GHUO6cn?m=web) - Keep detailed records of the performance of your Django code.
- [New Relic](https://newrelic.com/python/django) - Time middleware, views, and SQL queries.
- [Scout](https://docs.scoutapm.com/#django) - Time middleware, template rendering, and SQL queries with automatic N+1 detection.
- [django-query-profiler](https://github.com/django-query-profiler/django-query-profiler) - Django query profiler to help resolve N+1 queries.
- [django-silk](https://github.com/jazzband/django-silk) - Live profiling and inspection of HTTP requests and database queries.
- [py-spy](https://github.com/benfred/py-spy) - Sampling profiler for Python programs.

### Search
- [django-haystack](https://github.com/django-haystack/django-haystack) - Modular search for Django.
- [django-watson](https://github.com/etianen/django-watson) - Full-text search plugin.

### Search engine optimisation
- [django-check-seo](https://github.com/kapt-labs/django-check-seo) - Check SEO of pages.

### Security
- [django-csp](https://github.com/mozilla/django-csp) - Adds [Content-Security-Policy](http://www.w3.org/TR/CSP/) headers to Django.
- [django-feature-policy](https://github.com/adamchainz/django-feature-policy) - Set the draft security HTTP header `Feature-Policy` on a Django app.
- [django-protected-media](https://github.com/cobusc/django-protected-media) - Manages media that are considered sensitive in a protected fashion.

### Static Assets
- [django-storages](https://github.com/jschneier/django-storages) - A single library to support multiple custom storage backends for Django.
- [django-compressor](https://github.com/django-compressor/django-compressor/) - Compress JavaScript/CSS into a single cached file.
- [easy-thumbnails](https://github.com/SmileyChris/easy-thumbnails) - Image thumbnails for Django.

### Task Queues
- [beatserver](https://github.com/rajasimon/beatserver) - A periodic task scheduler for Django.
- [django-q](https://github.com/Koed00/django-q) - A multiprocessing distributed task queue.
- [django-rq](https://github.com/rq/django-rq) - Integration for Redis Queue.
- [django-redis](https://github.com/niwinz/django-redis) - Full featured Redis cache backend for Django.
- [celery](https://github.com/celery/celery) - Robust and broker-agnostic task queues for bigger, performance-focused projects.
- [django-dramatiq](https://github.com/Bogdanp/django_dramatiq) - Task processing library with a focus on simplicity, reliability and performance.

### Testing
- [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar/) - Configurable panels to debug requests/responses.
- [pytest-django](https://github.com/pytest-dev/pytest-django) - Use pytest features in Django.
- [django-test-migrations](https://github.com/wemake-services/django-test-migrations) - Test django schema and data migrations, including migrations' order.
- [django-test-plus](https://github.com/revsys/django-test-plus/) - Useful additions to Django's default TestCase.
- [factory-boy](https://github.com/FactoryBoy/factory_boy) - Test fixtures replacement.
- [django-waffle](https://github.com/django-waffle/django-waffle) - A feature flipper for Django.
- [model-bakery](https://github.com/model-bakers/model_bakery) - Object factory for Django (rename of legacy Model Mommy project).
- [django-swagger-tester](https://github.com/sondrelg/django-swagger-tester) - Django test utility for validating Swagger documentation.
- [django-google-optimize](https://github.com/adinhodovic/django-google-optimize) - Django application designed to make running server side Google Optimize A/B tests easy.

### URLs
- [dj-database-url](https://github.com/jacobian/dj-database-url) - Database URLs.
- [urlman](https://github.com/andrewgodwin/urlman) - A nicer way to do URLs for Django models.
- [django-robots](https://github.com/jazzband/django-robots) - This is a basic Django application to manage robots.txt files following the robots exclusion protocol, complementing the Django Sitemap contrib app.

### Users
- [django-allauth](https://github.com/pennersr/django-allauth/) - Improved user registration including social auth.
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
- [whitenoise](https://github.com/evansd/whitenoise) - Simplified static file serving for Python websites.

## Resources

### Official Resources

- [Project Website](https://www.djangoproject.com/) - Official Django website.
- [Documentation](https://docs.djangoproject.com/en/dev/) - Comprehensive documentation for all Django versions.
- [Polls Tutorial](https://docs.djangoproject.com/en/dev/intro/tutorial01/) - Build a polls tutorial while learning Django internals.
- [Source Code](https://github.com/django/django/) - Hosted on GitHub.

### Educational

- [Django Girls Tutorial](https://tutorial.djangogirls.org/en/) - Use function-based views to build a blog app.
- [LearnDjango](https://learndjango.com/) - Tutorials and premium courses on Django and Django REST Framework.
- [Adam Johnson](https://adamj.eu/tech/) - Adam is on the Technical Board of Django and writes regular tutorials.
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

### Community

<!--lint disable double-link-->
- [Django Forum](https://forum.djangoproject.com/) - Discourse Board.
- [Community Page](https://www.djangoproject.com/community/) - Featuring feeds of Community Blog Posts, Jobs, and more.
- [Django Users Google Group](https://groups.google.com/forum/#!forum/django-users/) - Very active discussion board for questions/answers.
- [Developers Google Group](https://groups.google.com/forum/#!forum/django-developers/) - For contributions to Django itself only.
- [Twitter](https://twitter.com/djangoproject/) - For official announcements on updates, security fixes, etc.
- IRC Channel - Chat with other Django users at irc://irc.freenode.net/django.
<!--lint enable double-link-->

### Conferences

- [DjangoCon US](https://2019.djangocon.us/) ([YouTube Channel](https://www.youtube.com/channel/UC0yY6a79pPY9J0ShIHRf6yw))
- [DjangoCon Europe](https://2020.djangocon.eu/) ([YouTube Channel](https://www.youtube.com/user/djangoconeurope))
- [Django Day Copenhagen](https://github.com/wsvincent/awesome-django#conferences)
- [PyCon US](https://us.pycon.org/2020/) ([YouTube Channel](https://www.youtube.com/channel/UCsX05-2sVSH7Nx3zuk3NYuQ))
- [PyCon Australia](https://2019.pycon-au.org/) ([YouTube Channel](https://www.youtube.com/user/PyConAU))
- [Euro Python](https://ep2019.europython.eu/) ([YouTube Channel](https://www.youtube.com/user/PythonItalia))
- [Django Under the Hood](https://www.youtube.com/channel/UC9T1dhIlL_8Va9DxvKRowBw/videos)
- [Complete listing of all PyCons globally](https://pycon.org)

### Newsletters

- [Django News](https://django-news.com) - Weekly newsletter on announcements, articles, projects, and talks.

### Podcasts

- [Django Chat](https://djangochat.com/) - A weekly podcast from William Vincent and Django Fellow Carlton Gibson with discussions of core Django concepts and regular guests.
- [Django Riffs](https://djangoriffs.com) - A new podcast from Matt Layman.
- [Running in Production](https://runninginproduction.com/tags/django) - Focused on tech stacks with many episodes specifically on Django.
- [TalkPython](https://talkpython.fm/) - The leading Python podcast with several episodes on Django.
- [Podcast Init](https://www.pythonpodcast.com/) - A popular Python podcast that features Django guests on occasion.


### Books

_Django 3.1_
- [Django for Beginners: Build websites with Python and Django](https://djangoforbeginners.com/)
- [Django for APIs: Build web APIs with Python and Django](https://djangoforapis.com/)
- [Django for Professionals: Production websites with Python and Django](https://djangoforprofessionals.com/)
- [Two Scoops of Django 3.x: Best Practices for the Django Web Framework](https://www.feldroy.com/collections/two-scoops-press/products/two-scoops-of-django-3-x)
- [A Wedge of Django: Covers Python 3.8 and Django 3.x](https://www.feldroy.com/collections/two-scoops-press/products/django-crash-course)

_Django 3.0_
- [Speed Up Your Django Tests](https://adamj.eu/tech/2020/05/04/new-book-speed-up-your-django-tests/)
- [Django 3 by Example](https://djangobyexample.com/)
- [Django 3 Web Development Cookbook](https://www.packtpub.com/eu/web-development/django-3-web-development-cookbook-fourth-edition)
- [Mastering Django](https://www.amazon.com/Mastering-Django-Nigel-George/dp/0648884414/)
- [Build a website with Django 3](https://www.amazon.com/Build-Website-Django-Nigel-George/dp/0648884406/)

_Django 2.2_
- [Tango with Django](https://www.tangowithdjango.com/)

## Hosting

### PaaS (Platforms-as-a-Service)
- [Heroku](https://www.heroku.com/)
- [PythonAnywhere](https://www.pythonanywhere.com)
- [Divio](https://www.divio.com/)
- [Microsoft Azure](https://azure.microsoft.com/en-us/develop/python/)
- [AWS CodeStar](https://aws.amazon.com/codestar/)
- [Google Cloud](https://cloud.google.com/python/django/)
- [Zeit Now](https://zeit.co/home)
- [Dokku](http://dokku.viewdocs.io/dokku/)
- [Render](https://render.com/)

### IaaS (Infrastructure-as-a-Service)
- [Digital Ocean](https://www.digitalocean.com)
- [Linode](https://www.linode.com/)
- [Amazon Lightsail](https://aws.amazon.com/lightsail/)
- [Hetzner](https://www.hetzner.com/)

## Projects

### Boilerplate
- [cookiecutter-django](https://github.com/pydanny/cookiecutter-django/) - A full-bodied starter project, highly customizable.
- [djangox](https://github.com/wsvincent/djangox/) - Batteries included starter project for Pip, Pipenv, or Docker.
- [DRFx](https://github.com/wsvincent/drfx/) - A DRF starter with user auth, Pipenv, and other goodies.
- [django-project-template](https://github.com/jpadilla/django-project-template) - A deliberately basic project that has multiple staging environments and Heroku deployment config.
- [docker-django](https://github.com/erroneousboat/docker-django/) - A quick starter guide for Django and Docker together.
- [ponee](https://github.com/valentinogagliardi/ponee/) - A lightweight Django template ready for Heroku.
- [wemake-django-template](https://github.com/wemake-services/wemake-django-template/) - Bleeding edge Django template focused on code quality and security.
- [django2-project-template](https://github.com/vigo/django2-project-template/) - A quick starter template with PostgreSQL.
- [django-webpack-starter](https://github.com/khadegd/django-webpack-starter) - Django Webpack starter template for using Webpack 4.
- [sos-django-template](https://github.com/erayerdin/sos-django-template) - Django starter template with separate dev and production settings.
- [django-docker-heroku-template](https://github.com/bfirsh/django-docker-heroku-template) - A template with Docker, GitHub Actions, and Heroku set up for dev/test/prod, plus various other best practices.
- [cookiecutter-vue-django](https://github.com/ilikerobots/cookiecutter-vue-django) - Django + Vue starter project fusing Vue SFCs & Django Templates.

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
- [DRF Blog API](https://wsvincent.com/django-rest-framework-tutorial/)
- [Building APIs with Django and DRF](https://books.agiliq.com/projects/django-api-polls-tutorial/en/latest/)
- [DRF with React: Todo API](https://wsvincent.com/django-rest-framework-react-tutorial/)
- [DRF with React](https://www.valentinog.com/blog/drf/)
- [Making React and Django play well together](https://fractalideas.com/blog/making-react-and-django-play-well-together/)

## Wagtail

_Wagtail, the powerful CMS for modern websites._

### Wagtail Resources
<!--lint disable double-link-->
- [Official Documentation](https://wagtail.io/)
- [Wagtail Source Code](https://github.com/wagtail/wagtail/)
- [awesome-wagtail](https://github.com/springload/awesome-wagtail)
- [This week in Wagtail](https://wagtail.io/this-week-in-wagtail/) - A (most) weekly email with updates from the Wagtail core team.
- [Wagtail Space](https://www.wagtail.space/) - Wagtail CMS events around the world.
<!--lint enable double-link-->
