import pandas as pd
from datetime import datetime

def analyze_performance(events):
    times = [datetime.strptime(e["timestamp"], "%H:%M:%S") for e in events]
    latencies = [(times[i+1] - times[i]).total_seconds() for i in range(len(times)-1)]
    return {
        "total_events": len(events),
        "avg_latency": sum(latencies) / len(latencies) if latencies else 0
    }
