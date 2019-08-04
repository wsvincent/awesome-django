<div align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat.svg" /></a>
  <br /><br />
  <img width="400" src="django-logo.svg" alt="Django logo">
</div>

# Awesome Django

> A curated list of awesome things related to Django.

## Contents

- [Resources](#resources)
  - [Official](#official-resources)
  - [External](#external-resources)
  - [Community](#community)
  - [Conferences](#conferences)
    - [YouTube Channels](#conference-youtube-channels)
  - [Meetups](#meetups)
  - [Podcasts](#podcasts)
- [Third-Party Packages](#third-party-packages)
- [Tutorials](#tutorials)
  - [Beginner](#beginner-tutorials)
  - [Intermediate/Advanced](#intermediate-advanced)
  - [Docker](#docker)
- [Boilerplate](#boilerplate)
- [Open Source Apps](#open-source-apps)
- [Open Source Projects](#open-source-projects)
- [Django REST Framework](#django-rest-framework)
  - [Resources](#drf-resources)
  - [Tutorials](#drf-tutorials)
  - [DRF Boilerplate](#drf-boilerplate)
  - [Open Source Apps](#drf-open-source-apps)
- [Books](#books)
- [Hosting](#hosting)
- [Courses](#courses)
- [Videos](#videos)
  - [Free Videos](#free-videos)
  - [Paid Videos](#paid-videos)

## Resources

### Official Resources

- [Project Website](https://www.djangoproject.com/) - Official Django website
- [Documentation](https://docs.djangoproject.com/en/dev/) - Comprehensive documentation for all Django versions
- [Polls Tutorial](https://docs.djangoproject.com/en/dev/intro/tutorial01/) - Build a polls tutorial while learning Django internals
- [Source Code](https://github.com/django/django) - Hosted on Github

### External Resources

- [William Vincent's Website](https://wsvincent.com) - Up-to-date tutorials on Django and Django REST Framework.
- [Django Packages](https://djangopackages.org/) - Comprehensive directory of reusable Django apps and tools.
- [Classy Class-Based Views](http://ccbv.co.uk/) - Detailed descriptions of methods/properties/attributes for each generic class-based view.
- [Classy Django Forms](https://cdf.9vo.lt/) - Detailed descriptions of methods/properties/attributes for each form class.
- [Classy Django REST Framework](http://www.cdrf.co/) - Detailed descriptions with methods/attributes for DRF class-based views and serializers.
- [Django Sites](https://www.djangosites.org/) - Comprehensive listing of sites built with Django.
- [Pony Checkup](https://www.ponycheckup.com/) - Security checkups for Django sites.
- [Django Hunter](https://github.com/6IX7ine/djangohunter) - Tool to help identify incorrectly configured Django applications that are exposing sensitive information.
- [Simple is Better than Complex](https://simpleisbetterthancomplex.com/) - Regularly updated website with many tutorials and tips on Django.
- [Full Stack Python's Django Page](https://www.fullstackpython.com/django.html) - Explanation of Django philosophy and links to other resources and tutorials.
- [RealPython](https://realpython.com/tutorials/django/) - Many high-quality tutorials on Django.
- [TestDriven](https://testdriven.io/blog/) - Multiple Django-specific tutorials on topics like Docker, payments, and more.

### Community

- [Users Google Group](https://groups.google.com/forum/#!forum/django-users) - Very active discussion board for questions/answers.
- [Developers Google Group](https://groups.google.com/forum/#!forum/django-developers) - For contributions to Django itself only.
- [Twitter](https://twitter.com/djangoproject) - For official announcements on updates, security fixes, etc.
- IRC Channel - Chat with other Django users at irc://irc.freenode.net/django

### Conferences

- [DjangoCon US](https://2019.djangocon.us/)
- [DjangoCon Europe](https://2019.djangocon.eu/)
- [PyCon US](https://us.pycon.org/2019/)
- [PyCon Australia](https://2019.pycon-au.org/)
- [Euro Python](https://ep2019.europython.eu/)
- [Complete listing of all PyCons globally](https://www.pycon.org/)

### Conference YouTube Channels

- [DjangoCon US](https://www.youtube.com/channel/UC0yY6a79pPY9J0ShIHRf6yw)
- [DjangoCon Europe](https://www.youtube.com/user/djangoconeurope)
- [PyCon US](https://www.youtube.com/channel/UCsX05-2sVSH7Nx3zuk3NYuQ)
- [EuroPython](https://www.youtube.com/user/PythonItalia)
- [PyCon Australia](https://www.youtube.com/user/PyConAU)
- [Django Under the Hood](https://www.youtube.com/channel/UC9T1dhIlL_8Va9DxvKRowBw/videos)

### Meetups

- [Meetups](https://www.meetup.com/topics/django/all/) - 400+ Meetup groups in 65 countries.

### Podcasts

- [Django Chat](https://djangochat.com) - A weekly podcast from William Vincent and Django Fellow Carlton Gibson with discussions of core Django concepts and regular guests.
- [TalkPython](https://talkpython.fm/) - The leading Python podcast with several episodes on Django.
- [Podcast Init](https://www.podcastinit.com/) - A popular Python podcast that features Django guests on occasion.

## Third-Party Packages

_For a complete listing of all available packages, see [Django Packages](https://djangopackages.org/)_

- [channels](https://github.com/django/channels/) - Async support for Django
- [django-allauth](https://github.com/pennersr/django-allauth/) - Improved user registration including social auth
- [django-autocomplete-light](https://github.com/yourlabs/django-autocomplete-light) - Add autocompletion to forms
- [django-compressor](https://github.com/django-compressor/django-compressor/) - Compress JavaScript/CSS into a single cached file
- [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms/) - DRY Django forms
- [dj-database-url](https://github.com/kennethreitz/dj-database-url) - Database URLs
- [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar/) - Configurable panels to debug requests/responses
- [django-environ](https://github.com/joke2k/django-environ) - Environment variables
- [django-extensions](https://github.com/django-extensions/django-extensions/) - Custom management extensions, notably `runserver_plus` and `shell_plus`
- [django-extra-views](https://github.com/AndrewIngram/django-extra-views) - Extra class-based generic views
- [django-filter](https://github.com/carltongibson/django-filter) - Powerful filters based on Django QuerySets
- [django-guardian](https://github.com/django-guardian/django-guardian) - Per object permissions in Django
- [django-hijack](https://github.com/arteria/django-hijack) - Admins can log in and work on behalf of other users without having to know their credentials
- [django-import-export](https://github.com/django-import-export/django-import-export) - Import/export data more easily with admin integration
- [django-loginas](https://github.com/skorokithakis/django-loginas) - "Log in as user" for the Django admin
- [django-model-utils](https://github.com/jazzband/django-model-utils) - Django model mixins and utilities
- [django-organizations](https://github.com/bennylope/django-organizations/) - Multi-user accounts for Django projects
- [django-redis](https://github.com/niwinz/django-redis) - Full featured redis cache backend for Django
- [django-reversion](https://github.com/etianen/django-reversion) - Version control for model instances
- [django-rq](https://github.com/rq/django-rq) - Integration for Redis Queue
- [django-shapeshifter](https://github.com/kennethlove/django-shapeshifter) - A CBV to handle multiple forms in one view
- [django-silk](https://github.com/jazzband/django-silk) - Live profiling and inspection of HTTP requests and database queries
- [django-sql-explorer](https://github.com/groveco/django-sql-explorer) - Share data via SQL queries
- [django-storages](https://github.com/jschneier/django-storages) - A single library to support multiple custom storage backends for Django
- [django-tables2](https://github.com/jieter/django-tables2) - HTML tables with pagination/sorting
- [django-taggit](https://github.com/jazzband/django-taggit/) - Simple model tags
- [django-test-plus](https://github.com/revsys/django-test-plus/) - Useful additions to Django's default TestCase
- [easy-thumbnails](https://github.com/SmileyChris/easy-thumbnails) - Image thumbnails for Django
- [django-vanilla-views](https://github.com/tomchristie/django-vanilla-views) - Simpler class-based views in Django
- [django-watson](https://github.com/etianen/django-watson) - Full-text search plugin
- [factory-boy](https://github.com/FactoryBoy/factory_boy) - Test fixtures replacement
- [pytest-django](https://github.com/pytest-dev/pytest-django) - Use pytest features in Django
- [urlman](https://github.com/andrewgodwin/urlman) - A nicer way to do URLs for Django models
- [whitenoise](https://github.com/evansd/whitenoise) - Simplified static file serving for Python websites

*Content Management Systems (CMSs)*
- [wagtail](https://github.com/wagtail/wagtail) - Popular Django content management system (CMS)
- [mezzanine](https://github.com/stephenmcd/mezzanine) - CMS framework
- [django-cms](https://github.com/divio/django-cms) - CMS for Django


*Django REST Framework*

- [django-cors-headers](https://github.com/OttoYiu/django-cors-headers) - If your back-end and front-end are on different servers, you need this
- [django-rest-auth](https://github.com/Tivix/django-rest-auth) - REST API endpoints for authentication and registration
- [djoser](https://github.com/sunscrapers/djoser) - REST implementation of Django auth
- [django-rest-framework](https://github.com/encode/django-rest-framework) - Web APIs for Django
- [django-rest-framework-simplejwt](https://github.com/davesque/django-rest-framework-simplejwt) - JSON web tokens for DRF
- [django-rest-swagger](https://github.com/marcgibbons/django-rest-swagger) - API document generator for Swagger UI

## Tutorials

### Beginner Tutorials

- [Django Girls Tutorial](https://tutorial.djangogirls.org/en/) - Use function-based views to build a blog app.
- [Django for Beginners](https://djangoforbeginners.com/) - Use class-based views to build three apps of increasing complexity (part of a full-length book).
- [Mozilla Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django) - Create a lending library app.
- [A Complete Beginner's Guide to Django](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/) - In-depth and excellent walkthrough of a new Django app
- [Build a HackerNews clone](https://medium.com/@danieldng/a-little-hacker-news-in-django-part-1-f12aa81dc25d) - Very well-done tutorial for Django 2.0.

### Intermediate/Advanced Tutorials

- [Django Stripe Tutorial](https://testdriven.io/blog/django-stripe-tutorial/)
- [Setting up Stripe Connect with Django](https://testdriven.io/blog/setting-up-stripe-connect-with-django/)
- [Storing Django Static and Media Files on Amazon S3](https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3)
- [Python and Django Logging in Plain English](https://djangodeconstructed.com/2018/12/18/django-and-python-logging-in-plain-english/)

### Docker Tutorials

_Docker is commonly used to work with production-level databases locally like PostgreSQL or MySQL._

- [A Beginner's Guide to Docker](https://wsvincent.com/beginners-guide-to-docker/)
- [A Brief Intro to Docker for Djangonauts](https://www.revsys.com/tidbits/brief-intro-docker-djangonauts/)
- [How to use Django, Docker, and PostgreSQL](https://wsvincent.com/django-docker-postgresql/)
- [Docker for Django Developers (slides)](https://mherman.org/presentations/dockercon-2018/#1)
- [Dockerizing Django with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx)

## Boilerplate

- [cookiecutter-django](https://github.com/pydanny/cookiecutter-django) - A full-bodied starter project, highly customizable.
- [djangox](https://github.com/wsvincent/djangox) - A simpler approach with complete user authentication flow, Pipenv, and more.
- [django-starter-project](https://github.com/jpadilla/django-project-template) - A deliberately basic project that has multiple staging environments and Heroku deployment config.
- [docker-django](https://github.com/erroneousboat/docker-django) - A quick starter guide for Django and Docker together.
- [ponee](https://github.com/valentinogagliardi/ponee) - A lightweight Django template ready for Heroku.
- [wemake-django-template](https://github.com/wemake-services/wemake-django-template) - Bleeding edge django template focused on code quality and security.

## Open Source Apps

- [Hello, World app](https://github.com/wsvincent/djangoforbeginners/tree/master/ch2-hello-world-app)
- [Message Board app](https://github.com/wsvincent/djangoforbeginners/tree/master/ch4-message-board-app)
- [Blog app with users and forms](https://github.com/wsvincent/djangoforbeginners/tree/master/ch7-blog-app-with-users)
- [Newspaper app with custom user model, full user auth](https://github.com/wsvincent/djangoforbeginners/tree/master/ch15-comments)
- [Behavior-Driven Development with Aloe](https://github.com/testdrivenio/django-aloe-bdd)
- [Image Sharing Blog](https://github.com/MeNsaaH/soMedia)
- [Bootcamp: An enterprise social network](https://github.com/vitorfs/bootcamp)

## Open Source Projects

- [Zulip](https://github.com/zulip/zulip) - Open-source team chat
- [django-oscar](https://github.com/django-oscar/django-oscar) - E-commerce for Django
- [saleor](https://github.com/mirumee/saleor) - E-commerce storefront
- [Django-CRM](https://github.com/MicroPyramid/Django-CRM) - Open Source Python CRM based on Django

## Django REST Framework

_The most popular way to build web APIs with Django._

### DRF Resources

- [Official Documentation](http://www.django-rest-framework.org/)
- [DRF Source Code](https://github.com/encode/django-rest-framework)
- [DRF](https://github.com/nioperas06/awesome-django-rest-framework)

### DRF Tutorials

- [Official REST Framework - A Beginner's Guide](https://wsvincent.com/official-django-rest-framework-tutorial-beginners-guide/)
- [DRF Blog API](https://wsvincent.com/django-rest-framework-tutorial/)
- [Building APIs with Django and DRF](https://books.agiliq.com/projects/django-api-polls-tutorial/en/latest/)
- [DRF Serializers, Viewsets, and Routers](https://wsvincent.com/django-rest-framework-serializers-viewsets-routers/)
- [DRF Todo API with User Auth](https://wsvincent.com/django-rest-framework-authentication-tutorial/)
- [DRF User Authentication](https://wsvincent.com/django-rest-framework-user-authentication-tutorial/)
- [DRF with React: Todo API](https://wsvincent.com/django-rest-framework-react-tutorial/)
- [DRF with React](https://www.valentinog.com/blog/tutorial-api-django-rest-react/)
- [Making React and Django play well together](https://fractalideas.com/blog/making-react-and-django-play-well-together/)

### DRF Boilerplate

- [DRFx](https://github.com/wsvincent/drfx)

### DRF Open Source Apps

- [DRF Polls](https://github.com/wsvincent/drf-polls) - API of the official Django polls tutorial
- [DRF Blog](https://github.com/wsvincent/drf-blog-api) - Basic Blog API
- [ECGC](https://github.com/flowerncsu/ecgc-2017) - Example from DjangoCon 2017 talk [Write an API for Almost Anything](https://www.youtube.com/watch?v=-6tR5TffP0w)

## Hosting

### PaaS (Platforms-as-a-Service)

- [Heroku](https://www.heroku.com/)
- [PythonAnywhere](https://www.pythonanywhere.com/details/django_hosting)
- [Divio](https://www.divio.com)
- [Microsoft Azure](https://azure.microsoft.com/en-us/develop/python/)
- [AWS CodeStar](https://aws.amazon.com/codestar/)
- [Google Cloud](https://cloud.google.com/python/django/)
- [Zeit Now](https://zeit.co/now)
- [Dokku](http://dokku.viewdocs.io/dokku/)
- [Render](https://render.com/)

### IaaS (Infrastructure-as-a-Service)

- [Digital Ocean](https://m.do.co/c/c0a588a8bb9e)
- [Linode](https://www.linode.com/?r=70d00cc48f300a318474ba61cb7e7663b6e1531b)
- [Amazon Lightsail](https://aws.amazon.com/lightsail/)

## Books

_Django 2.2_
- [Django for Beginners: Build websites with Python and Django](https://djangoforbeginners.com/)
- [Django for APIs: Build web APIs with Python and Django](https://djangoforapis.com/)
- [Django for Professionals: Production websites with Python and Django](https://djangoforprofessionals.com)


_Django 2.1_
- [Build Your First Website with Django 2.1](https://transactions.sendowl.com/stores/9897/130290)
- [Practical Django 2 and Channels 2](https://www.amazon.com/dp/1484240987/?tag=wsvincent-20)
- [Django 2 Web Development Cookbook](https://www.amazon.com/dp/1788837681/?tag=wsvincent-20)

_Django 2.0_

- [Hello Web App 2.0](https://hellowebbooks.com/learn-django/)
- [Django Design Patterns and Best Practices](https://www.amazon.com/dp/1788831349/?tag=wsvincent-20)
- [Django 2 by Example](https://www.amazon.com/dp/1788472489/?tag=wsvincent-20)

_Django 1.11_

- [Two Scoops of Django: Best Practices for Django 1.11](https://www.amazon.com/dp/0692915729/?tag=wsvincent-20)
- [Test-Driven Development with Python](https://www.amazon.com/dp/1491958707/?tag=wsvincent-20)
- [Django RESTful Web Services](https://www.amazon.com/dp/1788833929/?tag=wsvincent-20)
- [Beginning Django](https://www.amazon.com/dp/1484227867/?tag=wsvincent-20)

## Courses

- [Develop a Real-Time Taxi App with Django Channels and Angular](https://testdriven.io/affiliates/e4245ba649f3/)

## Videos

### Free Videos

_Django 2.1_

- [Django Authentication Tutorial by Vitor Freitas](https://youtu.be/60GTvKCuam8?list=PLLxk3TkuAYnryu1lEcFaBr358IynT7l7H)
- [Build a Startup with Django by CSDojo](https://youtu.be/UyQn0BhVqNU)
- [Just Django](https://www.youtube.com/channel/UCRM1gWNTDx0SHIqUJygD-kQ)

_Django 2.0_

- [Build a Guestbook (30-part series) by Pretty Printed](https://www.youtube.com/watch?v=QVX-etwgvJ8&list=PLXmMXHVSvS-DQfOsQdXkzEZyD0Vei7PKf)
- [Blog Tutorial by Corey Schafer](https://youtu.be/UmljXZIypDc?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
- [CS50's Web Programming with Python and JavaScript](https://www.youtube.com/playlist?list=PLhQjrBD2T382hIW-IsOVuXP1uMzEvmcE5)

_Django 1.11_

- [Todo App by Traversy Media](https://youtu.be/2yXfUPwlZTw)
- [Django Crash Course by Traversy Media](https://youtu.be/D6esTdOLXh4)

### Paid Videos

- [Build Backend Web Apps and APIs with Django](https://www.oreilly.com/library/view/web-development-in/9780134659824/) - 9 hour course from Andrew Pinkham, author of [Django Unleashed](https://www.amazon.com/dp/0321985079/?tag=wsvincent-20), covering APIs, data manipulation, and deployment to Heroku.
- [Build a Real Estate App](https://click.linksynergy.com/link?id=1*FmkJFU6n4&offerid=507388.1952540&type=2&murl=https%3A%2F%2Fwww.udemy.com%2Fpython-django-dev-to-deployment%2F) - 11 hour course by Brad Traversy on building a real estate app with PostgreSQL and deploying to Digital Ocean.
- [Ultimate Web Development Bootcamp](https://click.linksynergy.com/link?id=1*FmkJFU6n4&offerid=507388.1562632&type=2&murl=https%3A%2F%2Fwww.udemy.com%2Fthe-ultimate-beginners-guide-to-django-django-2-python-web-dev-website%2F) - 10 hour course building three apps--word counter, personal portfolio, product hunt clone--and deploying to Digital Ocean.

### License

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

> Some links contain affiliate codes which help me justify the time to keep this list up-to-date.
