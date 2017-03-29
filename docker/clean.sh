docker stop $(docker ps -a -q)
sleep 1
docker rm $(docker ps -a -q)
sleep 1
docker rmi $(docker images -a -q)