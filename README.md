# DNSDIST Dashboard

A centralized dashboard to view **Top Queries** from multiple DNSDIST servers.

## Features

- Query multiple DNSDIST servers via their REST API
- Display top queries per server
- Dockerized frontend (React) and backend (FastAPI)

## Setup

1. Edit `config.py` to include your DNSDIST servers and API keys.
2. Run:

```bash
docker-compose up --build
```

3. Access the frontend at `http://localhost:3000`

## Notes

Ensure that the DNSDIST web API is accessible to this Docker VM.
