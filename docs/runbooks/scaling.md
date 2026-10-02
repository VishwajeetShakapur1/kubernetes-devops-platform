# Scaling Runbook

## HPA

```bash
kubectl -n platform get hpa
kubectl -n platform describe hpa order-service
```

Check CPU requests first. HPA CPU utilization is calculated against the resource request.

## KEDA

```bash
kubectl -n platform get scaledobject
kubectl -n platform describe scaledobject order-service
```

Check that Prometheus is reachable from the KEDA operator and that the query returns a value.
