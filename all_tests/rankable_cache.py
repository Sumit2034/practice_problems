def say_hello():
    print('Hello, World')

for i in range(5):
    say_hello()


# For reference, here are the Rankable and DataSource interfaces.
# You do not need to implement them, and should not make assumptions
# about their implementations.
class Rankable:
    # Returns the Rank of this object, using some algorithm and potentially
    # the internal state of the Rankable.
    def getRank() -> int:
        pass
 
 
class DataSource:
    def get(key: K) -> Rankable:
        pass
 
class Node:
    def __init__(self, key, rank) -> None:
        self.val = rank
        self.key = key
        self.prev, self.next = None, None
 
# Class we're actually implementing:
class RetainBestCache:
    # Constructor with a data source (assumed to be slow) and a cache size
    # @param data_source the persistent layer of the the cache
    # @param entries_to_retain the number of entries that the cache can hold
    def __init__(self, data_source: DataSource, entries_to_retain: int) -> None:
        # Implementation heres
        self.data_source = data_source
        self.entries_to_retain = entries_to_retain
        self.best_cache = {}
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left
 
    # Gets some data. If possible, retrieves it from cache to be fast. If the data is not cached,
    # retrieves it from the data source. If the cache is full, attempt to cache the returned data,
    # evicting the V with lowest rank among the ones that it has available
    # If there is a tie, the cache may choose any V with lowest rank to evict.
    # @param key the key of the cache entry being queried
    # @return the Rankable value of the cache entry
    def least_rank_key(self):
        least_node = self.right.prev
        return least_node
    
    def max_rank_key(self):
        max_node = self.left.next
        return max_node

    
    def update_least_rank(self, value, key):
        l_node = self.least_rank_key()
        max_node = self.max_rank_key()
        new_node = Node(value["rank"], key)
        if value["rank"] < l_node.key:
            prev = self.right.prev
            prev.next = new_node
            new_node.next = self.right
            self.right.prev = new_node
        elif value["rank"] > max_node:
            nxt = self.left.next
            new_node.prev = self.left
            self.left.next = new_node
            nxt.prev = new_node
        
    
    def evict_least_rank(self, node):
        prev = node.prev
        nxt = node.next
        prev.next= nxt
        nxt.prev = prev

    def get(self, key: K) -> Rankable:
        # Implementation here
        if key in self.best_cache:
            return self.best_cache[key]
        else:
            value = self.data_source.get(key)
            if len(self.best_cache) >= self.entries_to_retain:
                l_node = self.least_rank_key()
                del self.best_cache[l_node.key]
                self.evict_least_rank(l_node)
                self.best_cache[key] = value
                self.update_least_rank(value, key)
        

"""Chirag -> {age, city..., rank = 1}

Sumit -> {age, city,...,rank = 2}    
Jai -> {age, city,...,rank = 0}
Naman -> {age, city,...,rank = 5}   

prev= right.prev 

Max size = 3

-1->5->4->2->1->0->-1

-> -> -> -> ->

Akash -> {age, city....rank =4}

Max size = 3
"""