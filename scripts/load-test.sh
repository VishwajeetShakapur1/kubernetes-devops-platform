#!/usr/bin/env bash
set -euo pipefail
URL="${1:-http://localhost:8080}"
for i in $(seq 1 200); do curl -s "$URL" >/dev/null || true; done
echo "Sent 200 requests to $URL"
