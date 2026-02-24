#!/bin/bash
# Nightly database snapshot for KXST
# Cron: 0 2 * * *
set -euo pipefail

REPO_DIR="$HOME/kxst"
DB_DIR="$REPO_DIR/db"

# Dump database
pg_dump -U libretime libretime | gzip > "$DB_DIR/libretime-$(date +%Y%m%d).sql.gz"

# Keep only last 30 days
find "$DB_DIR/" -name "*.sql.gz" -mtime +30 -delete

# Commit and push
cd "$REPO_DIR"
git add db/
git commit -m "db snapshot $(date +%Y-%m-%d)" --allow-empty
git push
