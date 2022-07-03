#!/usr/bin/env bash
set -eo pipefail

python -m venv /tmp/venv

source /tmp/venv/bin/activate && pip install -qr requirements.txt

while ! </dev/tcp/db/3306; do sleep 5; done

gunicorn -b 0.0.0.0:4000 main:app --reload --timeout 99999