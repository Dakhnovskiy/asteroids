#!/bin/bash

python scripts/make_migrations.py
python scripts/make_upload_folder.py

nohup python src/app/worker.py &

if [[ ${ENVIRONMENT} = 'LOCAL' ]]; then
    exec uvicorn src.app.app:app --reload --host 0.0.0.0 --port 5000 --log-level info
else
    exec uvicorn src.app.app:app --host 0.0.0.0 --port 5000 --log-level warning
fi