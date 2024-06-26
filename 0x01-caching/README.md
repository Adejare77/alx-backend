# Caching

## Cache Replacement Policies

Cache replacement policies (Cache Replace Algorithms or Cache algorithm) are optimizing instructions or algorithms which a computer prgoram or hardware-maintained structure can utilize to manage a cache of information.
Caching improves performance by keeping recent or often-used data items in memory locations which are faster, or computationally cheaper to access than normal memory stores. When the cache is full, the algorithm must choose which items to discard to make room for new data.

### Simple Queue-Based Policies

1. First-In First-Out (FIFO): A cache replacement policy the first item added to the cache is the first one to be removed when the cache is full

2. Last-In First-Out (LIFO): A cache replacement policy the most recently added items is the first one to be removed when the cache is full.

3. Most Recently Used (MRU): A cache replacement policy where the most recently used (either added or called) is the first one to be removed

4. Least Recently Used (LRU): A cache replacement policy that remove the least recently used item (either added or called) when the cache is full

5. Least Frequently Used (LFU): A cache replacement policy that removes the least frequently used item when the cache is full
