#!/bin/sh
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
heroku plugins:install heroku-container-registry || exit 1
docker login -u _ --password=$HEROKU_API_KEY registry.heroku.com || exit 1
heroku container:push web --app $HEROKU_APP_NAME || exit 1
heroku container:release web --app $HEROKU_APP_NAME || exit 1
