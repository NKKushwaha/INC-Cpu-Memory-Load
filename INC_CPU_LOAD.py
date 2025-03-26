import time
import threading

def simulate_cpu_load(increase_rate, duration):
    def cpu_intensive_task():
        while True:
            num = 2
            primes = []
            while num <= 10000:
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    primes.append(num)
                num += 1
    
    end_time = time.time() + duration
    load_threads = []

    while time.time() < end_time:
        for _ in range(increase_rate):
            thread = threading.Thread(target=cpu_intensive_task)
            thread.daemon = True
            load_threads.append(thread)
            thread.start()
            time.sleep(1)  


        print(f"Increasing CPU load: {len(load_threads)} tasks running.")
    

    while True:
        time.sleep(10)

# Example usage
simulate_cpu_load(increase_rate=2, duration=10)  # Increase load by 2 tasks per second for 10 seconds
