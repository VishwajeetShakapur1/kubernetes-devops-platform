#!/usr/bin/env bash
set -euo pipefail
URL="${1:-http://localhost:8080}"
for i in $(seq 1 20); do curl -s "$URL/fail" >/dev/null || true; done
echo "Generated 20 application failures"
