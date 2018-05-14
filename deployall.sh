#!/usr/bin/env bash
set -e

# Enter minikube docker environmeent
eval $(minikube docker-env)

# Build products-service
pushd products-service
docker build . -t products-service:v4 -f deploy/Dockerfile

# Deploy products-service
kubectl apply -f deploy/deployment.yml
kubectl apply -f deploy/service.yml

popd

# Build cart-service
pushd cart-service
docker build . -t cart-service:v4 -f deploy/Dockerfile

# Deploy cart-service
kubectl apply -f deploy/deployment.yml
kubectl apply -f deploy/service.yml

popd

# Deploy api gateway
pushd gateway
kubectl apply -f https://www.getambassador.io/yaml/ambassador/ambassador-no-rbac.yaml
kubectl apply -f ambassador-svc.yml

popd
