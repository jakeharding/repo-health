#!/bin/bash

docker exec -it repohealth_web_1 coverage run --source=repo_health ./manage.py test

# npm test is currently broken in a docker container
docker exec -it repohealth_web_1 npm test --prefix ./repo_health/index/static/ -- --single-run
