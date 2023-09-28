def strategic_count(mapfile):
    '''
    1. Use DFS to solve the problem.
    2. First breaking the mapfile into parts, each parts has one source and few destinations
        - The source can go to destinations, which is a data type of dict
    3. Store all parts into dict, where key is the source and values is a list of destinations
    4. Then use this dict to run DFS
    '''
    graph = {}
    with open(mapfile) as f:
        # For graph building
        for line in f:
            parts = line.rstrip('\n').split()
            source = parts[0]
            destinations = parts[1:]
            graph[source] = destinations

        def dfs(source, destination, cache):
            '''
            1. First we run some base cases, for example
                - If the source is destination, which means it is a possible way, return 1
                - If the source is 'deadend', which means it is not possible be a way, return 0
                - If the source is not in the graph, which is an error, return 0
                - If the source is in cache, read the possible_ways in cache, return it
                    - Since each source can be accessed more than one time, the source that access again, means that the
                    possible ways will increase by the number for that source's possible ways
            2. If base cases not happened, means that the source is new and valued to run DFS
            3. Read all values from the graph dict for the key is source, through these values and run DFS for each, and
            add the possible ways into the total_ways
            4. Add this source's total possible ways into the cache
                - Cache is also a dict, logged for a source, how many ways is founded.
            5. Note that the start point has only one source 'CountryA', so each time the DFS will read cached current
            possible ways from 'CountryA' to all seen points. In this case the total way is always increasing.
            '''
            # Base case:
            if source == destination:
                return 1
            if source == 'deadend':
                return 0
            if source not in graph:
                return 0
            if source in cache:
                return cache[source]

            total_ways = 0
            # For each source, through neighbors
            for neighbor in graph[source]:
                # Recursively run dfs to find possible way
                total_ways += dfs(neighbor, destination, cache)
            cache[source] = total_ways
            return total_ways
    return dfs('CountryA', 'capitalB', {})


# for your testing out
# Do not include them in your submission
# print(strategic_count('mapfile1.txt')) #ans = 4
# print(strategic_count('mapfile2.txt')) #ans = 5

