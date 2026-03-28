# RAG-Based-Solution

## Step 1 — Enable pgvector:
```sql
CREATE EXTENSION IF NOT EXISTS vector;
```
## Step 2 — Create your table:
```sql
CREATE TABLE rag_chunks (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    doc_id      TEXT NOT NULL,
    source      TEXT,          -- 'jira' | 'confluence'
    title       TEXT,
    url         TEXT,
    content     TEXT,
    embedding   vector(768),   -- use 768 for bge-base (lighter, free-tier friendly)
    metadata    JSONB,
    created_at  TIMESTAMPTZ DEFAULT now()
);
```
```sql
CREATE INDEX ON rag_chunks
    USING hnsw (embedding vector_cosine_ops)
    WITH (m = 16, ef_construction = 64);
```
## Step 3 — Python connection:
```js
pip install psycopg2-binary pgvector sentence-transformers
```
