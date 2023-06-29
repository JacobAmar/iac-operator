redeploy:
		kubectl delete configmap tfproject-controller
		kubectl create configmap tfproject-controller --from-file=main.py
		kubectl rollout restart deployment/tfproject-controller