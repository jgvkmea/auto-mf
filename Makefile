IMAGE_REPOSITORY_NAME := private/auto-mf
CONTAINER_NAME := auto-mf
ECR_REGISTRY := ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com

.PHONY: build
build:
	docker build -t ${IMAGE_REPOSITORY_NAME} .

.PHONY: run
run:
	docker run -it -d --rm -p 9000:8080 --name "${CONTAINER_NAME}" ${IMAGE_REPOSITORY_NAME}

.PHONY: stop
stop:
	docker stop ${CONTAINER_NAME}

.PHONY: logs
logs:
	docker logs ${CONTAINER_NAME}

.PHONY: rebuild
rebuild:
	${MAKE} stop
	${MAKE} build
	${MAKE} run

.PHONY: restart
restart:
	${MAKE} stop
	${MAKE} run

.PHONY: login
login:
	aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com

.PHONY: push
push:
	docker tag ${IMAGE_REPOSITORY_NAME} ${ECR_REGISTRY}/${IMAGE_REPOSITORY_NAME}
	docker push ${ECR_REGISTRY}/${IMAGE_REPOSITORY_NAME}
