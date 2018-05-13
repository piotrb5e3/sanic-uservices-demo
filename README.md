# µservices with sanic and kubernetes demo
This is a demo/practise setup with [Sanic](https://github.com/channelcat/sanic) and [Kubernetes](https://kubernetes.io/)

## Requirements
* Python 3.5+
* Docker
* [Minikube](https://kubernetes.io/docs/getting-started-guides/minikube/)

## Running the demo
* Start minikube: `minikube start`
* Build and deploy services: `./deployall.sh`
* Make a test API call: `curl $(minikube service cart-service --url)/1234/getTotal`