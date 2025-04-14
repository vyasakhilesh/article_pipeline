for container in $(docker ps -q); do
    docker network connect my_shared_network $container
done