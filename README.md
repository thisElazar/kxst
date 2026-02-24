# KXST Station Ops

Operations repository for KXST radio station.

## Structure
- `config/` — LibreTime config backup (sanitized)
- `scripts/` — Maintenance scripts (db backup, log rotation)
- `logs/playout/` — Playout logs (FCC compliance)
- `db/` — Nightly database snapshots
- `legal/` — FCC/legal documents
- `docs/` — Station documentation

## Automated Jobs
- **2:00 AM** — Database snapshot (scripts/db-snapshot.sh)
- **2:15 AM** — Playout log commit (scripts/log-commit.sh)
