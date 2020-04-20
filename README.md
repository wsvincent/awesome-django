<div align="center">
  <a href="https://github.com/sindresorhus/awesome#readme"><img src="https://awesome.re/badge-flat.svg" /></a>
  <img width="400" src="django-logo.svg" alt="Django logo">
</div>

# Awesome Django
> A curated list of awesome things related to Django.

## Contents

- [Third-Party Packages](#third-party-packages)
  - [Admin](#admin)
  - [APIs](#apis)
  - [Async](#async)
  - [Commands](#commands)
  - [Configuration](#configuration)
  - [Content Management Systems](#content-management-systems)
  - [ECommerce](#ecommerce)
  - [Files/Images](#files-images)
  - [Forms](#forms)
  - [Models](#models)
  - [Performance](#performance)
  - [Search](#search)
  - [Static Assets](#static-assets)
  - [Task Queues](#task-queues)
  - [Testing](#testing)
  - [Users](#users)
  - [Views](#views)
  - [URLs](#urls)
- [Python Packages](#python-packages)
- [Resources](#resources)
  - [Official](#official-resources)
  - [External](#external-resources)
  - [Community](#community)
  - [Conferences](#conferences)
  - [Podcasts](#podcasts)
  - [Tutorials](#tutorials)
  - [Books](#books)
  - [Courses](#courses)
  - [Videos](#videos)
- [Hosting](#hosting)
  - [PaaS](#paas-platforms-as-a-service)
  - [IaaS](#iaas-infrastructure-as-a-service)
- [Projects](#projects)
  - [Boilerplate](#boilerplate)
  - [Open Source Projects](#open-source-projects)
- [Django REST Framework](#django-rest-framework)
  - [Resources](#drf-resources)
  - [Tutorials](#drf-tutorials)
  - [DRF Boilerplate](#drf-boilerplate)
  - [Open Source Apps](#drf-open-source-apps)

## Third-Party Packages

_For a complete listing of all available packages, see [Django Packages](https://djangopackages.org/)_



- [django-filter](https://github.com/carltongibson/django-filter) - Powerful filters based on Django QuerySets
- [django-guardian](https://github.com/django-guardian/django-guardian) - Per object permissions in Django
- [django-sql-explorer](https://github.com/groveco/django-sql-explorer) - Share data via SQL queries
- [django-tables2](https://github.com/jieter/django-tables2) - HTML tables with pagination/sorting

### Admin
- [django-grappelli](https://github.com/sehmaschine/django-grappelli) - A jazzy skin for the admin
- [django-hijack](https://github.com/arteria/django-hijack) - Admins can log in and work on behalf of other users without having to know their credentials
- [django-import-export](https://github.com/django-import-export/django-import-export) - Import/export data more easily with admin integration
- [django-admin-honeypot](https://github.com/dmpayton/django-admin-honeypot) - Configure a honeypot to see who's trying to hack your site
- [django-loginas](https://github.com/skorokithakis/django-loginas) - "Log in as user" for the Django admin

### APIs
- [django-rest-framework](https://github.com/encode/django-rest-framework) - Web APIs for Django
- [django-cors-headers](https://github.com/adamchainz/django-cors-headers) - If your back-end and front-end are on different servers, you need this
- [django-rest-auth](https://github.com/Tivix/django-rest-auth) - REST API endpoints for authentication and registration
- [django-rest-knox](https://github.com/James1345/django-rest-knox) - Authentication Module for django-rest-auth
- [djoser](https://github.com/sunscrapers/djoser) - REST implementation of Django auth
- [django-rest-framework-simplejwt](https://github.com/davesque/django-rest-framework-simplejwt) - JSON web tokens for DRF
- [django-webpack-loader](https://github.com/owais/django-webpack-loader) - Transparently use webpack with Django
- [drf-yasg](https://github.com/axnsan12/drf-yasg) - Automated generation of real Swagger/OpenAPI 2.0 schemas from Django REST Framework code
- [graphene-django](https://github.com/graphql-python/graphene-django) - GraphQL for Django


### Async
- [channels](https://github.com/django/channels/) - Async support for Django
- [starlette](https://github.com/encode/starlette) - ASGI framework

### Commands
- [django-extensions](https://github.com/django-extensions/django-extensions/) - Custom management extensions, notably `runserver_plus` and `shell_plus`
- [django-click](https://github.com/GaretJax/django-click) - Write Django management commands using the click CLI library
- [django-dbbackup](https://github.com/django-dbbackup/django-dbbackup) - Management commands to help backup and restore your project database and media files

### Configuration
- [confidential](https://github.com/candidco/confidential) - Manage configs and secrets (with CLI support)
- [django-environ](https://github.com/joke2k/django-environ) - Environment variables
- [django-split-settings](https://github.com/sobolevn/django-split-settings) - Organize multiple settings files

### Content Management Systems
- [wagtail](https://github.com/wagtail/wagtail) - Popular Django content management system (CMS)
- [mezzanine](https://github.com/stephenmcd/mezzanine) - CMS framework
- [django-cms](https://github.com/divio/django-cms) - CMS for Django
- [puput](https://github.com/APSL/puput) - Blog app features with Wagtail

### ECommerce
- [saleor](https://github.com/mirumee/saleor) - GraphQL-based Django E-Commerce Platform
- [django-shop](https://github.com/awesto/django-shop) - Django-based shop system
- [shuup](https://github.com/shuup/shuup) - Django E-Commerce Platform

### Files/Images
- [django-cleanup](https://github.com/un1t/django-cleanup) - Zero configuration file/image removal for local and remote files

### Forms
- [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms/) - DRY Django forms
- [django-widget-tweaks](https://github.com/jazzband/django-widget-tweaks) - Tweak form field rendering in templates
- [django-autocomplete-light](https://github.com/yourlabs/django-autocomplete-light) - Add autocompletion to forms
- [django-shapeshifter](https://github.com/kennethlove/django-shapeshifter) - A CBV to handle multiple forms in one view
- [bleach](https://github.com/mozilla/bleach) - Technically not a Django package but very useful

### Models
- [django-fakery](https://github.com/fcurella/django-fakery) - An easy-to-use implementation of Creation Methods for Django, backed by Faker
- [django-lifecycle](https://github.com/rsinger86/django-lifecycle) - Declarative model lifecycle hooks, an alternative to Signals
- [django-model-utils](https://github.com/jazzband/django-model-utils) - Django model mixins and utilities
- [django-money](https://github.com/django-money/django-money) - Money fields for forms/models
- [django-phonenumber-field](https://github.com/stefanfoulis/django-phonenumber-field) - Model/form field for normalized phone numbers
- [django-taggit](https://github.com/jazzband/django-taggit/) - Simple model tags
- [django-reversion](https://github.com/etianen/django-reversion) - Version control for model instances
- [django-simple-history](https://github.com/treyhunner/django-simple-history) - Store model history and view/revert changes from the admin

### Search
- [django-haystack](https://github.com/django-haystack/django-haystack) - Modular search for Django
- [django-watson](https://github.com/etianen/django-watson) - Full-text search plugin

### Performance
- [django-perf-rec](https://cur.at/GHUO6cn?m=web) - Keep detailed records of the performance of your Django code
- [New Relic](https://newrelic.com/python/django) - Time middleware, views, and SQL queries
- [Scout](https://docs.scoutapm.com/#django) - Time middleware, template rendering, and SQL queries with automatic N+1 detection
- [django-query-profiler](https://github.com/django-query-profiler/django-query-profiler) - Django query profiler to help resolve N+1 queries

### Static Assets
- [django-storages](https://github.com/jschneier/django-storages) - A single library to support multiple custom storage backends for Django
- [django-compressor](https://github.com/django-compressor/django-compressor/) - Compress JavaScript/CSS into a single cached file
- [easy-thumbnails](https://github.com/SmileyChris/easy-thumbnails) - Image thumbnails for Django

### Task Queues
- [beatserver](https://github.com/rajasimon/beatserver) - A periodic task scheduler for Django
- [django-q](https://github.com/Koed00/django-q) - A multiprocessing distributed task queue
- [django-rq](https://github.com/rq/django-rq) - Integration for Redis Queue
- [django-redis](https://github.com/niwinz/django-redis) - Full featured Redis cache backend for Django

### Testing
- [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar/) - Configurable panels to debug requests/responses
- [pytest-django](https://github.com/pytest-dev/pytest-django) - Use pytest features in Django
- [django-test-migrations](https://github.com/wemake-services/django-test-migrations) - Test django schema and data migrations, including migrations' order
- [django-test-plus](https://github.com/revsys/django-test-plus/) - Useful additions to Django's default TestCase
- [factory-boy](https://github.com/FactoryBoy/factory_boy) - Test fixtures replacement
- [django-silk](https://github.com/jazzband/django-silk) - Live profiling and inspection of HTTP requests and database queries
- [django-waffle](https://github.com/django-waffle/django-waffle) - A feature flipper for Django
- [model-bakery](https://github.com/model-bakers/model_bakery) - Object factory for Django (rename of legacy Model Mommy project)

### Users
- [django-allauth](https://github.com/pennersr/django-allauth/) - Improved user registration including social auth
- [django-organizations](https://github.com/bennylope/django-organizations/) - Multi-user accounts for Django projects

### Views
- [django-braces](https://github.com/brack3t/django-braces) - Reusable, generic mixins
- [django-extra-views](https://github.com/AndrewIngram/django-extra-views) - Extra class-based generic views
- [django-vanilla-views](https://github.com/tomchristie/django-vanilla-views) - Simpler class-based views in Django

### URLs
- [dj-database-url](https://github.com/jacobian/dj-database-url) - Database URLs
- [urlman](https://github.com/andrewgodwin/urlman) - A nicer way to do URLs for Django models

## Python Packages

_A short list of Python packages that work well with Django._

- [black](https://github.com/psf/black) - Uncompromising Python code formatter
- [coveragepy](https://github.com/nedbat/coveragepy) - Code coverage measurement
- [huey](https://github.com/coleifer/huey) - A little task queue for Python
- [nplusone](https://github.com/jmcarp/nplusone) - Auto-detect n+1 queries
- [pillow](https://github.com/python-pillow/Pillow) - Python Imaging Library
- [pytest](https://github.com/pytest-dev/pytest/) - Testing framework
- [python-slugify](https://github.com/un33k/python-slugify) - Returns unicode slugs
- [sentry-python](https://github.com/getsentry/sentry-python) - Error reporting SDK
- [whitenoise](https://github.com/evansd/whitenoise) - Simplified static file serving for Python websites

## Resources

### Official Resources

- [Project Website](https://www.djangoproject.com/) - Official Django website
- [Documentation](https://docs.djangoproject.com/en/dev/) - Comprehensive documentation for all Django versions
- [Polls Tutorial](https://docs.djangoproject.com/en/dev/intro/tutorial01/) - Build a polls tutorial while learning Django internals
- [Source Code](https://github.com/django/django/) - Hosted on Github

### External Resources

- [LearnDjango](https://learndjango.com/) - Up-to-date tutorials on Django and Django REST Framework.
- [Classy Class-Based Views](https://ccbv.co.uk/) - Detailed descriptions of methods/properties/attributes for each generic class-based view.
- [Classy Django Forms](https://github.com/ana-balica/classy-django-forms) - Detailed descriptions of methods/properties/attributes for each form class.
- [Classy Django REST Framework](http://www.cdrf.co) - Detailed descriptions with methods/attributes for DRF class-based views and serializers.
- [Django Sites](https://www.djangosites.org/) - Comprehensive listing of sites built with Django.
- [Pony Checkup](https://www.ponycheckup.com/) - Security checkups for Django sites.
- [Django Hunter](https://github.com/6IX7ine/djangohunter) - Tool to help identify incorrectly configured Django applications that are exposing sensitive information.
- [Simple is Better than Complex](https://simpleisbetterthancomplex.com/) - Regularly updated website with many tutorials and tips on Django.
- [Full Stack Python's Django Page](https://www.fullstackpython.com/django.html) - Explanation of Django philosophy and links to other resources and tutorials.
- [RealPython](https://realpython.com/tutorials/django/) - Many high-quality tutorials on Django.
- [TestDriven](https://testdriven.io/blog/) - Multiple Django-specific tutorials on topics like Docker, payments, and more.

### Community

- [Django Forum](https://forum.djangoproject.com/) - Discourse Board
- [Community Page](https://www.djangoproject.com/community/) - Featuring feeds of Community Blog Posts, Jobs, and more.
- [Django Users Google Group](https://groups.google.com/forum/#!forum/django-users/) - Very active discussion board for questions/answers.
- [Developers Google Group](https://groups.google.com/forum/#!forum/django-developers/) - For contributions to Django itself only.
- [Twitter](https://twitter.com/djangoproject/) - For official announcements on updates, security fixes, etc.
- IRC Channel - Chat with other Django users at irc://irc.freenode.net/django

### Conferences

- [DjangoCon US](https://2019.djangocon.us/) ([YouTube Channel](https://www.youtube.com/channel/UC0yY6a79pPY9J0ShIHRf6yw))
- [DjangoCon Europe](https://2020.djangocon.eu/) ([YouTube Channel](https://www.youtube.com/user/djangoconeurope))
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
- [TalkPython](https://talkpython.fm/) - The leading Python podcast with several episodes on Django.
- [Podcast Init](https://www.pythonpodcast.com/) - A popular Python podcast that features Django guests on occasion.

### Tutorials

- [Django Girls Tutorial](https://tutorial.djangogirls.org/en/) - Use function-based views to build a blog app.
- [Mozilla Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django) - Create a lending library app.
- [A Complete Beginner's Guide to Django](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/) - In-depth and excellent walkthrough of a new Django app
- [Build a HackerNews clone](https://medium.com/@danieldng/a-little-hacker-news-in-django-part-1-f12aa81dc25d) - Very well-done tutorial for Django 2.0.

### Books

_Django 3.0_
- [Django for Beginners: Build websites with Python and Django](https://djangoforbeginners.com/)
- [Django for APIs: Build web APIs with Python and Django](https://djangoforapis.com/)
- [Django for Professionals: Production websites with Python and Django](https://djangoforprofessionals.com/)
- [Django Crash Course](https://roygreenfeld.com/products/django-crash-course)
- [Django 3 by Example](https://djangobyexample.com/)
- [Django 3 Web Development Cookbook](https://www.packtpub.com/eu/web-development/django-3-web-development-cookbook-fourth-edition)

_Django 2.2_
- [Tango with Django](https://www.tangowithdjango.com/)
- [Build a website with Django 2](https://djangobook.com/build-a-website-with-django-2/)

_Django 2.1_
- [Practical Django 2 and Channels 2](https://www.amazon.com/Practical-Django-Channels-Applications-Capabilities/dp/1484240987)
- [Django 2 Web Development Cookbook](https://www.amazon.com/Django-Web-Development-Cookbook-practical/dp/1788837681)

_Django 2.0_
- [Hello Web App 2.0](https://hellowebbooks.com/learn-django/)
- [Django Design Patterns and Best Practices](https://www.amazon.com/Django-Design-Patterns-Practices-Industry-standard/dp/1788831349)
- [Django 2 by Example](https://www.amazon.com/Django-Example-powerful-reliable-applications/dp/1788472489)

_Django 1.11_

- [Two Scoops of Django: Best Practices for Django 1.11](https://www.feldroy.com/collections/two-scoops-press/products/two-scoops-of-django-1-11)
- [Test-Driven Development with Python](https://www.amazon.com/Test-Driven-Development-Python-Selenium-JavaScript/dp/1491958707)
- [Django RESTful Web Services](https://www.amazon.com/Django-RESTful-Web-Services-services/dp/1788833929)
- [Beginning Django](https://www.amazon.com/Beginning-Django-Application-Development-Deployment/dp/1484227867)

### Videos
- [Python Django Crash Course 2019 by Traversy Media](https://www.youtube.com/watch?v=e1IyzVyrLSU&feature=youtu.be)
- [Full Stack React & Django by Traversy Media](https://www.youtube.com/watch?v=Uyei2iDA4Hs&feature=youtu.be)
- [Just Django](https://www.youtube.com/channel/UCRM1gWNTDx0SHIqUJygD-kQ)
- [Try Django from Coding for Entrepreneurs](https://www.youtube.com/playlist?list=PLEsfXFp6DpzTD1BD1aWNxS2Ep06vIkaeW)
- [Python Django Tutorial by Corey Schafer](https://www.youtube.com/watch?v=UmljXZIypDc&feature=youtu.be)
- [CS50's Web Programming with Python and JavaScript](https://www.youtube.com/playlist?list=PLhQjrBD2T382hIW-IsOVuXP1uMzEvmcE5)

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

## Projects

### Boilerplate
- [cookiecutter-django](https://github.com/pydanny/cookiecutter-django/) - A full-bodied starter project, highly customizable.
- [djangox](https://github.com/wsvincent/djangox/) - A simpler approach with complete user authentication flow, Pipenv, and more.
- [DRFx](https://github.com/wsvincent/drfx/) - A DRF starter with user auth, Pipenv, and other goodies.
- [django-project-template](https://github.com/jpadilla/django-project-template) - A deliberately basic project that has multiple staging environments and Heroku deployment config.
- [docker-django](https://github.com/erroneousboat/docker-django/) - A quick starter guide for Django and Docker together.
- [ponee](https://github.com/valentinogagliardi/ponee/) - A lightweight Django template ready for Heroku.
- [wemake-django-template](https://github.com/wemake-services/wemake-django-template/) - Bleeding edge Django template focused on code quality and security.
- [django2-project-template](https://github.com/vigo/django2-project-template/) - A quick starter template with PostgreSQL.
- [django-webpack-starter](https://github.com/khadegd/django-webpack-starter) - Django Webpack starter template for using Webpack 4.
- [sos-django-template](https://github.com/erayerdin/sos-django-template) - Django starter template with separate dev and production settings

### Open Source
- [Blog app with users and forms](https://github.com/wsvincent/djangoforbeginners/tree/master/ch7-blog-app-with-users/)
- [Newspaper app with custom user model, full user auth](https://github.com/wsvincent/djangoforbeginners/tree/master/ch15-comments)
- [pythonic-news](https://github.com/sebst/pythonic-news) - Hacker News clone
- [Behavior-Driven Development with Aloe](https://github.com/testdrivenio/django-aloe-bdd/)
- [Image Sharing Blog](https://github.com/MeNsaaH/soMedia)
- [Bootcamp: An enterprise social network](https://github.com/vitorfs/bootcamp)
- [Zulip](https://github.com/zulip/zulip/) - Open-source team chat
- [django-oscar](https://github.com/django-oscar/django-oscar/) - E-commerce for Django
- [saleor](https://github.com/mirumee/saleor/) - E-commerce storefront
- [Django-CRM](https://github.com/MicroPyramid/Django-CRM/) - Open Source Python CRM based on Django
- [django-job-portal](https://github.com/manjurulhoque/django-job-portal) - Job portal application using Django

## Django REST Framework

_The most popular way to build web APIs with Django._

### DRF Resources

- [Official Documentation](https://www.django-rest-framework.org/)
- [DRF Source Code](https://github.com/encode/django-rest-framework)
- [awesome-django-rest-framework](https://github.com/nioperas06/awesome-django-rest-framework)

### DRF Tutorials

- [Official REST Framework - A Beginner's Guide](https://learndjango.com/tutorials/official-django-rest-framework-tutorial-beginners)
- [DRF Blog API](https://wsvincent.com/django-rest-framework-tutorial/)
- [Building APIs with Django and DRF](https://books.agiliq.com/projects/django-api-polls-tutorial/en/latest/)
- [DRF with React: Todo API](https://wsvincent.com/django-rest-framework-react-tutorial/)
- [DRF with React](https://www.valentinog.com/blog/drf/)
- [Making React and Django play well together](https://fractalideas.com/blog/making-react-and-django-play-well-together/)


### License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
