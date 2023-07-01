from kubernetes import client, config , watch
import json
# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
crd = client.CustomObjectsApi()
watch = watch.Watch()
for event in watch.stream(crd.list_cluster_custom_object,'terraform.iac.operator','v1','default','tfprojects'):
    print(event)