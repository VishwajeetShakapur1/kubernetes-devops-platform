# Architecture

```text
Developer
   |
   v
GitHub
   |
   v
GitHub Actions
   |-- tests
   |-- Docker build
   |-- Trivy scan
   v
ECR
   ^
   |
Argo CD <--- Git repository
   |
   v
EKS / Kubernetes
   |
   +-- order-service
   +-- payment-service
   +-- notification-service
   |
   +--> Prometheus --> Grafana
   |        |
   |        +--> Alertmanager
   |
   +--> Fluent Bit --> OpenSearch
   |
   +--> OpenTelemetry Collector
```

The application is deliberately small. The engineering focus is deployment, observability, scaling and operational troubleshooting.
