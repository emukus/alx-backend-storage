#!/usr/bin/python3
"""Lists all documents in a collection using pymongo"""


def list_all(mongo_collection):
    """Returns an empty list if no document is in the collection"""
    return [doc for doc in mongo_collection.find()]
