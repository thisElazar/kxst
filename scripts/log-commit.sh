#!/bin/bash
# Nightly playout log commit for KXST (FCC compliance)
# Cron: 15 2 * * *
set -euo pipefail

REPO_DIR="$HOME/kxst"
LOG_DIR="$REPO_DIR/logs/playout"

# Copy latest playout logs
cp /var/log/libretime/playout/*.log "$LOG_DIR/" 2>/dev/null || true

# Commit and push
cd "$REPO_DIR"
git add logs/
git commit -m "playout logs $(date +%Y-%m-%d)" --allow-empty
git push
