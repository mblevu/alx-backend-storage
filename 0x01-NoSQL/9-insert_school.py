#!/usr/bin/env python3
"""Insert a document in Python based on kwargs"""


def InsertSchool(mongo_collection, **kwargs):
    """Insert a document in Python based on kwargs"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
