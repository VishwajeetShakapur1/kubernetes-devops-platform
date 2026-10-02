#!/usr/bin/env bash
set -euo pipefail
kubectl get nodes
kubectl -n platform get pods,svc,hpa
kubectl -n argocd get applications
