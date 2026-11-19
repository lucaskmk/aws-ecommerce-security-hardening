#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
target_url="${1:-https://maisplace.net.br/}"
case "$target_url" in
  https://maisplace.net.br/|https://maisplace.net.br) ;;
  *) echo "Alvo fora do escopo deste roteiro: $target_url" >&2; exit 2 ;;
esac

scan_stamp="$(date +%Y-%m-%d_%H%M%S)"
out_dir="$repo_dir/external-scan/scan_$scan_stamp"
mkdir -p "$out_dir"

set +e
docker run --rm \
  -v "$out_dir:/zap/wrk:rw" \
  -t ghcr.io/zaproxy/zaproxy:stable zap-baseline.py \
  -t "$target_url" -m 2 \
  -r zap_baseline.html -J zap_baseline.json -w zap_baseline.md
scan_exit=$?
set -e

printf 'Relatórios em %s (exit ZAP: %s)\n' "$out_dir" "$scan_exit"
exit "$scan_exit"
