#!/usr/bin/env bash
set -e

# Enter minikube docker environmeent
eval $(minikube docker-env)

# Build products-service
pushd products-service
docker build . -t products-service:v1

# Deploy products-service
kubectl apply -f deployment.yml
kubectl apply -f service.yml

popd

# Build cart-service
pushd cart-service
docker build . -t cart-service:v1

# Deploy cart-service
kubectl apply -f deployment.yml
kubectl apply -f service.yml

popd
