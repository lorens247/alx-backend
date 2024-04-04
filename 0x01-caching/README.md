# 0x01 - Caching

This is an overview of caching systems, including their principles, strategies, and purposes.

## What is a Caching System?

A caching system is a mechanism used to store frequently accessed data in a temporary storage area, known as a cache, to expedite data retrieval and improve system performance. By caching data in memory or disk, a caching system reduces the need for repeated computations or expensive database queries, thereby enhancing application responsiveness and scalability.

## Cache Replacement Policies

### FIFO (First-In, First-Out)

FIFO is a cache replacement policy where the oldest cached items are removed first when the cache reaches its maximum capacity. It operates on the principle of "first come, first served," where the items that entered the cache earliest are evicted to make room for new entries.

### LIFO (Last-In, First-Out)

LIFO is a cache replacement policy where the most recently cached items are removed first when the cache is full. It follows the "last come, first served" principle, where the items that entered the cache last are evicted first.

### LRU (Least Recently Used)

LRU is a cache replacement policy that removes the least recently used items from the cache when it reaches its capacity limit. It prioritizes keeping recently accessed or frequently accessed items in the cache to maximize cache hits and minimize cache misses.

### MRU (Most Recently Used)

MRU is a cache replacement policy that removes the most recently used items from the cache when the cache is full. It prioritizes keeping the most recently accessed items in the cache, assuming they are more likely to be accessed again in the near future.

### LFU (Least Frequently Used)

LFU is a cache replacement policy that removes the least frequently used items from the cache when it reaches its capacity limit. It prioritizes keeping items that have been accessed most often, assuming they are more valuable and likely to be accessed again.

## Purpose of a Caching System

The primary purpose of a caching system is to improve application performance by reducing latency and enhancing scalability. By storing frequently accessed data closer to the application or user, caching systems minimize the need for repeated computations or expensive data retrieval operations, resulting in faster response times and better overall user experience.

## Limits of a Caching System

Caching systems have several limitations, including:

- Cache Size: Caching systems have a finite cache size, limiting the amount of data that can be stored in the cache at any given time. When the cache reaches its capacity limit, cache eviction policies determine which items are removed to make room for new entries.
- Cache Invalidation: Caching systems rely on cache invalidation mechanisms to ensure that cached data remains consistent with the underlying data source. Invalidation strategies must be implemented to update or remove cached items when the corresponding data changes.
- Cache Coherency: Maintaining cache coherency, or ensuring that all copies of cached data are consistent, can be challenging, especially in distributed caching environments. Strategies such as cache invalidation, cache replication, and cache coherence protocols are used to address this issue.

