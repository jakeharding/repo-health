#!/bin/bash
# Stops and removes all docker containers and images

docker stop $(docker ps -a -q)
sleep 1
docker rm $(docker ps -a -q)
sleep 1
docker rmi $(docker images -a -q)