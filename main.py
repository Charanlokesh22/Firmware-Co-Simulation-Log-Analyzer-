from app.parser import parse_log, protocol_check
from app.analyzer import analyze_performance
from app.visualizer import plot_latency

# Example usage
events = parse_log("sample_logs/sas_log.txt")
violations = protocol_check(events)
analysis = analyze_performance(events)

print("Analysis Summary:", analysis)
print("Protocol Violations:", violations)

# Example latency plotting
latencies = [0.5, 0.8, 0.6, 0.9, 0.4]
plot_latency(latencies)
print("Latency graph saved as latency_graph.png")


