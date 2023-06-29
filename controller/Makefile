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