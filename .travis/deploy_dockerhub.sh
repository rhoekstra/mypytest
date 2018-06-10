#!/bin/sh
#docker login -e $DOCKER_EMAIL -u $DOCKER_USER -p $DOCKER_PASS
docker login -u $DOCKER_USER -p $DOCKER_PASS || exit 1
if [ "$TRAVIS_BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi
docker build -f Dockerfile -t $TRAVIS_REPO_SLUG:$TAG . || exit 1
docker push $TRAVIS_REPO_SLUG || exit 1
