from collections.abc import Iterator
from contextlib import contextmanager

from psycopg import Connection
from psycopg.rows import TupleRow
from psycopg_pool import ConnectionPool


class Database:
    """Manage pooled PostgreSQL connections."""

    def __init__(
        self,
        conninfo: str,
        *,
        min_size: int = 1,
        max_size: int = 5,
        timeout: float = 10.0,
        autocommit: bool = False,
    ) -> None:
        self._pool: ConnectionPool[Connection[TupleRow]] = ConnectionPool(
            conninfo=conninfo,
            min_size=min_size,
            max_size=max_size,
            timeout=timeout,
            kwargs={"autocommit": autocommit},
            open=False,
        )

    def open(self) -> None:
        """Open the pool and wait for initial connections."""
        self._pool.open(wait=True)

    def close(self) -> None:
        """Close the connection pool."""
        self._pool.close()

    @contextmanager
    def connection(self) -> Iterator[Connection[TupleRow]]:
        """Borrow a connection from the pool."""
        with self._pool.connection() as conn:
            yield conn
