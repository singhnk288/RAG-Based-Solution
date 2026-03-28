# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:46:38 2026

@author: hp
"""

import os
from dotenv import load_dotenv

load_dotenv()

CONFLUENCE_USERNAME=os.getenv("CONFLUENCE_USERNAME")
CONFLUENCE_BASE_URL = os.getenv("CONFLUENCE_BASEURL")
CONFLUENCE_KEY= os.getenv("CONFLUENCE_KEY")
SUPERBASE_DB_PASSWORD=os.getenv("SUPERBASE_DB_PASSWORD")

CONFLUENCE_SPACE_LIST_URL= "/wiki/rest/api/space"
CONFLUENCE_ALL_PAGES_API_ENDPOINT = "/wiki/rest/api/content"

extracted_image="D:\\Coding\\GEN AI - Transformation\\Data-Extraction\\extracted_image\\"

# =============================================================================
# CREATE TABLE rag_chunks (
#     id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
#     doc_id      TEXT NOT NULL,
#     source      TEXT,          -- 'jira' | 'confluence'
#     title       TEXT,
#     url         TEXT,
#     content     TEXT,
#     embedding   vector(768),   -- use 768 for bge-base (lighter, free-tier friendly)
#     metadata    JSONB,
#     created_at  TIMESTAMPTZ DEFAULT now()
# );
# 
# CREATE INDEX ON rag_chunks
#     USING hnsw (embedding vector_cosine_ops)
#     WITH (m = 16, ef_construction = 64);
# =============================================================================
