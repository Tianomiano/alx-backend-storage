#!/usr/bin/env python3
"""
a Python function that lists all documents
in a collection
"""

def list_all(mongo_collection):
    """
    empty list if no document is in the collection
    """
    return mongo_collection.find()
