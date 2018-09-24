
.PHONY: docker-build
docker-build:
	sudo docker build -t edubenin.api -f $(PWD)/settings/Dockerfile.api . && \
	sudo docker build -t edubenin.webapp -f $(PWD)/settings/Dockerfile.webapp .


.PHONY: docker-run
docker-run:
	sudo docker run --name edubenin.api -p 81:80 -d edubenin.api && \
	sudo docker run --name edubenin.webapp -p 82:80 -d edubenin.webapp

.PHONY: docker-rm
docker-rm:
	sudo docker rm -f $(sudo docker -f "name=edubenin.api" -q) && \
	sudo docker rm -f $(sudo docker -f "name=edubenin.webapp" -q)



deploy: docker-build docker-run

undeploy: docker-rm



