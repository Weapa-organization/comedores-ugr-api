THIS_FILE := $(lastword $(MAKEFILE_LIST))
.PHONY:help
help:		## Show this help.
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)
build:		## Build the docker image
	docker-compose -f docker-compose.yml build $(c)
up-detach:	## Run the docker container in detached mode
	docker-compose -f docker-compose.yml up -d $(c)
up:		## Run the docker image
	docker-compose -f docker-compose.yml up $(c)
start:		## Start the docker image
	docker-compose -f docker-compose.yml start $(c)
down:		## Stop the docker image
	docker-compose -f docker-compose.yml down $(c)
destroy:	## Destroy the docker image
	docker-compose -f docker-compose.yml down -v $(c)
stop:		## Stop the docker image
	docker-compose -f docker-compose.yml stop $(c)
restart: 	## Restart the docker image
	docker-compose -f docker-compose.yml stop $(c)
	docker-compose -f docker-compose.yml up -d $(c)
logs:		## Show the logs of the docker image
	docker-compose -f docker-compose.yml logs --tail=100 -f $(c)
ps:		## Show the status of the docker image
	docker-compose -f docker-compose.yml ps