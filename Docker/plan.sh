#!/bin/bash
set -xe
git clone $REPO
cd $TFDIR
terraform init -input=false
terraform plan -input=false -out tfplan
kubectl create configmap $NAME-tfplan --from-file=tfplan