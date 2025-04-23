import datetime
import pandas as pd

query_log = []

def log_query(query, response):
    query_log.append({
        "timestamp": datetime.datetime.now().isoformat(),
        "query": query,
        "response": response
    })

def get_logs():
    return pd.DataFrame(query_log)
