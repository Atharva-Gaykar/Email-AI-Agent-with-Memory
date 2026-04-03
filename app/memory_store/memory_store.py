from psycopg_pool import ConnectionPool
from langgraph.store.postgres import PostgresStore
from langgraph.checkpoint.postgres import PostgresSaver
from app.memory_store.embeddings import remote_embeddings


pool = ConnectionPool(
    conninfo=DB_URI, 
    min_size=1, 
    max_size=10,
    kwargs={"autocommit": True} 
)

memory_store = PostgresStore(pool, index={"dims": 384, "embed": remote_embeddings})