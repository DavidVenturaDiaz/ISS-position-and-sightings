NAME ?= davidventuradiaz

all: build run push

images:
     docker images | grep ${NAME}

ps:
     docker ps -a | grep ${NAME}

build:
     docker build -t ${NAME}/iss-position-and-sightings .

run:
     docker run --name "iss-location-and-sightings" -d -p 5035:5000 davidventuradiaz/iss-location-and-sightings:latest


push:
     docker push ${NAME}/iss-position-and-sightings
