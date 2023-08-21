class LRU_Cache(object):


    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache_map = {}

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache_map:
            # Move the key-value pair to the front of the cache
            value = self.cache_map.pop(key)
            self.cache_map[key] = value
            return value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.cache_map:
            # Update the value of an existing key
            self.cache_map.pop(key)
        elif len(self.cache_map) >= self.capacity:
            # Remove the least recently used key if the cache is full
            self.cache_map.pop(next(iter(self.cache_map)))

        # Add the key-value pair to the cache
        self.cache_map[key] = value

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


## Test Case 1
our_cache.set(7,7)
our_cache.set(5,10)
our_cache.set(8,8)

assert our_cache.get(1) == -1 # return -1 because the cache reached it's capacity and 1 was the least recently used entry

## Test Case 2

assert our_cache.get(5) == 10 # return 10 it's the key 5 new value

## Test Case 3
assert our_cache.get(10) == -1 # return -1 since ky 10 not exist