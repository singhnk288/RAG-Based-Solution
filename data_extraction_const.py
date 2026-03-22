# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:46:38 2026

@author: hp
"""

import os
from dotenv import load_dotenv

load_dotenv()

CONFLUENCE_USERNAME="develneeraj@gmail.com"
CONFLUENCE_BASE_URL = "https://develneeraj.atlassian.net"
CONFLUENCE_KEY= os.getenv("CONFLUENCE_KEY")

CONFLUENCE_SPACE_LIST_URL= "/wiki/rest/api/space"
CONFLUENCE_ALL_PAGES_API_ENDPOINT = "/wiki/rest/api/content"

extracted_image="D:\\Coding\\GEN AI - Transformation\\Data-Extraction\\extracted_image\\"