#!/usr/bin/env python3
"""log stats"""
from pymongo import MongoClient

client = MongoClient('mongodb://127:0:0:1:27017')
db = client.logs
collection = db.nginx

total_logs = collection.count_documents({})

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({"method": method}) for method in methods}

status_get_count = collection.count_documents({"method": "GET", "path": "/status"})

print(f"{total_logs} logs")
print("Methods:")
for method, count in method_counts.items():
    print(f"\tmethod {method}: {count}")
print(f"{status_get_count} status check")
