# Fastuator

Production-ready monitoring for FastAPI.  
K8s probes, Prometheus metrics, health checks in 1 line.

## Features

- 🏥 Health checks (liveness, readiness)
- 📊 Prometheus metrics
- ℹ️ System information

## Installation

```bash
pip install fastuator
```

## Quick Start

```python
from fastapi import FastAPI
from fastuator import Fastuator

app = FastAPI()
Fastuator(app)  # Done!

# GET /actuator/health
# GET /actuator/liveness
# GET /actuator/readiness
# GET /actuator/metrics
# GET /actuator/info
```