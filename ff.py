import sys

t = int(input())
tcount = 0

page_tracker = [None] * t

pages = [None] * t
cache_sizes = [None] * t
while tcount < t:
    
    cache_sizes[tcount] = int(input())
    n = int(input())
    
    page_tracker[tcount] = {}
    
    schedule = input().strip().split()
    
    pages[tcount] = schedule
        
    tcount += 1
for tcount in range(t):
    for i in range(len(pages[tcount])):
        #print(pages[tcount][i])
        if pages[tcount][i] not in page_tracker[tcount].keys():
            page_tracker[tcount][pages[tcount][i]] = []
        page_tracker[tcount][pages[tcount][i]].append(i)




for tcount in range(t):
    cache_size = cache_sizes[tcount]
    cache = list()
    miss = 0
    schedule = pages[tcount]
    capacity = 0
    curr_count = 0
       
    for page in schedule:
        if page in cache:
            page_tracker[tcount][page].remove(curr_count)
            curr_count += 1
            continue
            
        elif capacity < cache_size:
            cache.append(page)
            #print(page)
            
            page_tracker[tcount][page].remove(curr_count)
            
            miss += 1
            capacity += 1
            curr_count += 1
        else:
            
            furthest_index = 0
            furthest_cached = None
            
            for cached in cache:
                #print(page_tracker[tcount][cached])
                if len(page_tracker[tcount][cached]) > 0:
                    if page_tracker[tcount][cached][0] > furthest_index:
                        furthest_index = page_tracker[tcount][cached][0]
                        furthest_cached = cached
                else:
                    furthest_cached = cached
                    break
                        
            #print(furthest_cached)
            cache.remove(furthest_cached)
            page_tracker[tcount][page].remove(curr_count)
            cache.append(page)
            curr_count += 1
            
            miss += 1
    print(miss)






