"""Default health check implementations."""

from typing import Any
import psutil


async def cpu_health() -> dict[str, Any]:
    """Check CPU usage."""
    cpu_percent = psutil.cpu_percent(interval=0.1)
    status = "UP" if cpu_percent < 90 else "DOWN"
    return {
        "status": status,
        "cpu_percent": cpu_percent,
    }


async def memory_health() -> dict[str, Any]:
    """Check memory usage."""
    memory = psutil.virtual_memory()
    status = "UP" if memory.percent < 90 else "DOWN"
    return {
        "status": status,
        "memory_percent": memory.percent,
        "memory_available_mb": memory.available // (1024 * 1024),
    }


async def disk_health() -> dict[str, Any]:
    """Check disk usage."""
    disk = psutil.disk_usage("/")
    status = "UP" if disk.percent < 90 else "DOWN"
    return {
        "status": status,
        "disk_percent": disk.percent,
        "disk_free_gb": disk.free // (1024 ** 3),
    }
