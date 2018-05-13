#!/usr/bin/env bash
set -e

# Enter minikube docker environmeent
eval $(minikube docker-env)

# Build products-service
pushd products-service
docker build . -t products-service:v1 -f deploy/Dockerfile

# Deploy products-service
kubectl apply -f deploy/deployment.yml
kubectl apply -f deploy/service.yml

popd

# Build cart-service
pushd cart-service
docker build . -t cart-service:v1 -f deploy/Dockerfile

# Deploy cart-service
kubectl apply -f deploy/deployment.yml
kubectl apply -f deploy/service.yml

popd
