all: redeploy tf_deploy

init:
	kubectl apply -f ../crds/
	kubectl create configmap tfproject-controller --from-file=main.py
redeploy:
		kubectl delete configmap tfproject-controller
		kubectl create configmap tfproject-controller --from-file=main.py
		kubectl rollout restart deployment/tfproject-controller

tf_deploy:
	kubectl apply -f ../examples/tfp.yaml

docker_build:
	$(eval IMAGE_NAME := $(shell /bin/bash -c 'echo iac-operator-$$RANDOM'))
	docker build -t ttl.sh/$(IMAGE_NAME):1h ../Docker
	docker push ttl.sh/$(IMAGE_NAME):1h
	echo $(IMAGE_NAME)