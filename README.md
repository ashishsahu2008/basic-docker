# basic-rest-api

Commands to run the project in docker

# Build docker image with present code
# This command executes code written in Dockerfile and builds image with name provided
docker build -t <name> <directory of docker file>
docker build -t rest-project .

# Run docker image in a container. 1 docker image can be run separately into many containers for scaling
# This command forwards port 80 of our machine to port 80 of container
docker run -p 80:80 rest-project


# This command uses docker-compose.yml file
# This command mounts volume provided in docker-compose.yml file into the container and thus looks into
# state of the file and provides any changes real time, but it does not build image everytime there
# is a change in file. So make sure to build image for permanent persistence
docker-compose up

# This command runs containers in detached mode/in the background
docker-compose -d

# This command stops containers and removes containers, networks, volumes, and images created by up
docker-compose down
