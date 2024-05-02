@_default:
    just --list

@alex:
	bunx alex README.md

@bootstrap:
    pip install --upgrade pip pip-tools
    pip install --upgrade --requirement requirements.in

@build:
    just toc
    bundle exec jekyll build

@down:
    docker-compose down

@lint:
    -curlylint _layouts/
    -bunx awesome-lint README.md

@serve:
    # modd --file=modd.conf
    just up ""

@start *ARGS="--detach":
    just up {{ ARGS }}

@up *ARGS:
    docker-compose up {{ ARGS }}

@toc:
	bunx doctoc README.md

@test:
    pytest

@coverage:
    pytest --cov=app

@deploy:
    git push heroku main

@backup:
    rsync -avz --exclude='*.log' /path/to/source /path/to/backup

@rollback:
    git checkout HEAD^

@analyze:
    bandit -r .

@format:
    black .

@encrypt:
    gpg --encrypt --recipient recipient@example.com filename.txt

@decrypt:
    gpg --decrypt filename.txt.gpg > filename.txt

@generate-keypair:
    ssh-keygen -t rsa -b 4096 -f ~/.ssh/my_key

@ssh-login:
    ssh username@hostname

@remote-sync:
    rsync -avz /path/to/local username@hostname:/path/to/remote

