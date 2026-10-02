# Deployment

## Local

Run a service:

```bash
python app/order-service/app.py
```

## Docker

```bash
docker build -f docker/order-service.Dockerfile -t order-service:dev .
docker run --rm -p 8080:8080 order-service:dev
```

## Kubernetes

Install metrics/observability dependencies separately, then:

```bash
kubectl apply -f kubernetes/namespace.yaml
kubectl apply -f kubernetes/configmap.yaml
kubectl apply -f kubernetes/services/
kubectl apply -f kubernetes/deployments/
kubectl apply -f kubernetes/hpa/
```

Replace ECR image names before applying deployments.

## GitOps

Update the repository URL in `gitops/applications/platform-dev.yaml`, install Argo CD in the cluster and apply the Application resource.
