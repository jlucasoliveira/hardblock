#!/usr/bin/sh
poetry run python -m debugpy --wait-for-client --listen 0.0.0.0:5678 -m uvicorn hardblock.asgi:application --reload --host 0.0.0.0 --port 8080