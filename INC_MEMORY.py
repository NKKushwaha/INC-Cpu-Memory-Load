import time
def consume_memory():
    memory_hog = []
    try:
        while True:
            memory_hog.extend([0] * (100 * 1024 * 1024 // 8))
            allocated_memory_mb = len(memory_hog) * 8 / (1024 * 1024)
            print(f"Allocated {allocated_memory_mb} MB of memory.")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Memory consumption stopped manually.")

if __name__ == "__main__":
    consume_memory()
