# Order Service High Error Rate

Alert: `OrderServiceHighErrorRate`

## 1. Check pods

```bash
kubectl -n platform get pods -l app=order-service
```

## 2. Inspect recent logs

```bash
kubectl -n platform logs -l app=order-service --tail=100
```

## 3. Check rollout

```bash
kubectl -n platform rollout history deployment/order-service
```

## 4. Roll back when a release is confirmed as the cause

```bash
kubectl -n platform rollout undo deployment/order-service
kubectl -n platform rollout status deployment/order-service
```

## 5. Verify

```bash
kubectl -n platform get pods
curl http://order-service.platform.svc.cluster.local/health
```
