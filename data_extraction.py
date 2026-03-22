# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:45:21 2026

@author: Neeraj
"""


import data_extraction_helpr as hlpr



def main():
    
    #hlpr.get_all_chuks_pages_from_confluence()    
    
    content=hlpr.extract_docx_content("D:\\Coding\\GEN AI - Transformation\\Data-Extraction\\RAG_Enterprise_Solution_v2.docx")
    print(content)
    content.metadata

if __name__ == "__main__":
    main()