
# Create thread to find prime number

import threading
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result):
    primes = [n for n in range(start, end) if is_prime(n)]
    result.extend(primes)

def threaded_prime_checker(start, end, num_threads=4):
    threads = []
    results = []
    chunk_size = (end - start) // num_threads
    
    for i in range(num_threads):
        thread_start = start + i * chunk_size
        thread_end = start + (i + 1) * chunk_size if i != num_threads - 1 else end
        result = []
        thread = threading.Thread(target=check_primes, args=(thread_start, thread_end, result))
        threads.append(thread)
        results.append(result)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    primes = [prime for result in results for prime in result]
    print("Prime numbers:", primes)

if __name__ == "__main__":
    start_range = 1
    end_range = 100
    num_threads = 4
    threaded_prime_checker(start_range, end_range, num_threads)