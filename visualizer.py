import matplotlib.pyplot as plt

def plot_latency(latencies):
    plt.plot(latencies, marker='o')
    plt.title("I/O Latency Over Time")
    plt.xlabel("Event Index")
    plt.ylabel("Latency (s)")
    plt.grid(True)
    plt.savefig("latency_graph.png")
    plt.close()
