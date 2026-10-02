# Cloud Native Platform

A personal DevOps/SRE project built around a small Kubernetes microservices platform.

I wanted the application itself to stay simple so I could spend time on the parts that normally cause operational work: CI/CD, deployments, monitoring, logs, alerts, scaling and incident handling.

## Stack

- AWS ECR / EKS
- Kubernetes
- Docker
- GitHub Actions
- Argo CD
- Prometheus
- Grafana
- Alertmanager
- Fluent Bit
- OpenSearch
- OpenTelemetry Collector
- HPA
- KEDA
- Python

## Flow

```text
GitHub -> GitHub Actions -> ECR
                         |
                         v
                    Argo CD
                         |
                         v
                       EKS
                 /       |       \
          order-service payment notification
                 |
       +---------+----------+
       |                    |
   Prometheus             Fluent Bit
       |                    |
    Grafana              OpenSearch
       |
 Alertmanager

OpenTelemetry Collector handles OTLP telemetry from instrumented workloads.
```

## Why I built it

The goal was not to create another sample CRUD application. I wanted a small environment where I could practice the operational lifecycle:

```text
build -> test -> scan -> publish -> deploy -> observe -> alert -> troubleshoot -> rollback
```

## Start locally

```bash
python app/order-service/app.py
```

Then:

```bash
curl http://localhost:8080/health
curl http://localhost:8080/metrics
```

Generate traffic:

```bash
./scripts/load-test.sh
```

Generate an incident:

```bash
./scripts/incident-test.sh
```

## Kubernetes

The Kubernetes resources are intentionally split into individual files so that a failure can be traced to a specific resource.

Before applying the deployment manifests, replace:

```text
REPLACE_WITH_ECR
```

with the ECR registry/repository used by the cluster.

## CI/CD

`ci.yaml` runs on pull requests and pushes to `main`.

It:

1. Compiles the Python code.
2. Runs unit tests.
3. Builds each service image.
4. Runs Trivy against the image.
5. Fails the workflow for HIGH/CRITICAL findings that are not marked unfixed.

`publish-ecr.yaml` is a manual workflow for publishing images to ECR using GitHub OIDC.

## GitOps

Argo CD watches:

```text
gitops/environments/dev
```

The Application uses automated sync with prune and self-heal.

## Observability

### Metrics

The order service exposes:

```text
/metrics
```

Prometheus collects request and error counters.

### Logs

Application logs are JSON lines. Fluent Bit reads Kubernetes container logs and enriches them with Kubernetes metadata.

The OpenSearch output is kept as a separate configuration section so the endpoint can be changed without changing the application.

### Traces

The OpenTelemetry Collector accepts OTLP over gRPC/HTTP. The sample collector exports to the debug exporter; an actual trace backend can be plugged in later.

## Scaling

The project demonstrates two approaches:

- HPA for CPU-driven scaling.
- KEDA for Prometheus-driven scaling.

They are alternatives. I would not run both controllers against the same Deployment at the same time in a production setup.

## Incident workflow

For an application error-rate alert:

```text
Alert
  |
  v
Grafana / Prometheus
  |
  v
Pod logs
  |
  v
Recent deployment
  |
  +--> healthy change -> continue investigation
  |
  +--> bad release -> rollback
```

See `docs/runbooks/`.

## Project status

The repository contains the complete configuration needed to build the lab. AWS-specific values such as the ECR repository, OIDC role and GitHub repository URL are intentionally placeholders rather than fake credentials or fake infrastructure.

## Author

Vishwajeet M Shakapur
