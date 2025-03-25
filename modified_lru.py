# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
import time
from collections import OrderedDict

class LRUCache:
    def __init__(self, func, capacity: int, expiration_time: int):
        self.cache = OrderedDict()  # Stores the cache (arguments as keys, results as values)
        self.capacity = capacity    # Maximum number of items in the cache
        self.func = func            # The function whose results are cached
        self.expiration_time = expiration_time  # Time in seconds after which cache expires

    def __call__(self, *args):
        current_time = time.time()

        # Check if the cache entry exists
        if args in self.cache:
            value, timestamp = self.cache[args]
            
            # If the cached value has expired, recalculate it
            if current_time - timestamp > self.expiration_time:
                print(f"Cache for {args} expired, recomputing...")
                result = self.func(*args)
                self.cache[args] = (result, current_time)  # Update cache with the new result and timestamp
                return result
            
            # Otherwise, move to end (most recently used) and return cached value
            self.cache.move_to_end(args)
            return value

        # If not in cache, calculate the result
        print(f"Cache miss for {args}, computing...")
        result = self.func(*args)
        self.cache[args] = (result, current_time)  # Store result and timestamp in the cache

        # If the cache exceeds capacity, remove the least recently used (oldest)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Removes the first (oldest) item

        return result

def slow_function(x):
    # Simulate a slow function
    print(f"Computing {x}...")
    time.sleep(2)  # Simulate delay
    return x * 2

# Create a cache with a capacity of 3 and cache expiration time of 3 seconds
cache = LRUCache(slow_function, 3, expiration_time=3)

# First time calls - these will compute and cache the result
print(cache(1))  # Computes and caches the result (2)
time.sleep(1)  # Wait for 1 second
print(cache(2))  # Computes and caches the result (4)

# This will access the cache without recomputation (cached result)
time.sleep(1)
print(cache(1))  # Should return cached result (2)

# Wait for the cache to expire (total 3 seconds)
time.sleep(2)
print(cache(1))  # Cache expired, recomputing... (new result)

