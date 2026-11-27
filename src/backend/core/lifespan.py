from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.concurrency import run_in_threadpool
from vestium.core.config import settings
from vestium.core.database import Database


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    db = Database(
        conninfo=settings.database_url,
        min_size=settings.db_min_size,
        max_size=settings.db_max_size,
        timeout=settings.db_timeout,
    )

    try:
        await run_in_threadpool(db.open)
        app.state.db = db
        yield
    finally:
        await run_in_threadpool(db.close)
