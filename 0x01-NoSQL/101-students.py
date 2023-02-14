#!/usr/bin/env python3
"""Mongo python operations"""


def top_students(mongo_collection):
    """Returns all students sorted by avg score"""
    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_student
