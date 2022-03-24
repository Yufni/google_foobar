def solution(entrances, exits, path):
    max_flow = 0

    def residual_comprobation(room):
        if isinstance(room,str):
            if room[len(room)-1:] == 'r':
                return int(room[:-1])
        return room

    def capacity(link):
        return link[1] - link[0]

    #source: {target: [flow, capacity], ...}
    infinity = float('inf')
    graph = {'s': {target:[0,infinity] for target in entrances}}
    graph.update({source: {target: [0, path[source][target]] for target in range(len(path[source])) if path[source][target] != 0} for source in range(len(path))})
    graph.update({target: {'t':[0,infinity]} for target in exits})
    graph.update({'t': {}})
    residual_list = [[room, list(graph[room].keys())] for room in graph.keys()]
    for target in residual_list:
        for source in target[1]:
            try:
                graph[source][target[0]]
                graph[source].update({str(target[0]) + 'r': [0, 0]})
            except KeyError:
                graph[source].update({target[0]: [0, 0]})

    while True:
        visited = {room: 'no_visited' for room in graph.keys()}
        visited['s'] = 0
        level = 1
        queue = ['s']
        dfs_trayectory = {0: ['s']}

        #bfs
        while queue[0] != [] and dfs_trayectory[len(dfs_trayectory)-1] != ['t']:
            queue.append([])
            dfs_trayectory.update({level: []})
            for actual_room in queue[0]:
                for target_room in graph[actual_room].keys():
                    try:
                        if visited[target_room] == 'no_visited' and capacity(graph[actual_room][target_room]) > 0:
                            visited[target_room] = level
                            queue[1].append(target_room)
                            dfs_trayectory[level].append(target_room)
                    except KeyError:
                        actual_without_r = residual_comprobation(actual_room)
                        target_without_r = residual_comprobation(target_room)
                        if visited[target_without_r] == 'no_visited' and capacity(graph[actual_without_r][target_without_r]) > 0:
                            visited[target_without_r] = level
                            queue[1].append(target_room)
                            dfs_trayectory[level].append(target_room)
            level += 1
            queue.pop(0)
        
        if visited['t'] == 'no_visited':
            return max_flow

        #dfs
        trayectory = ['s']
        bottleneck = [infinity]
        level = 1
        while trayectory != []:
            find_path = False
            source = trayectory[len(trayectory) - 1]
            if source == 't':
                flow = min(bottleneck)
                max_flow += flow
                trayectory.pop(0)
                source = 's'
                for target in trayectory:
                    graph[source][target][0] += flow
                    graph[target][source][0] -= flow
                    source = target
                trayectory = ['s']
                bottleneck = [infinity]
                level = 1
                continue
            else:
                for target in dfs_trayectory[level]:
                    try:
                        actual_capacity = capacity(graph[source][target])
                    except KeyError:
                        continue
                    if actual_capacity > 0:
                        trayectory.append(target)
                        bottleneck.append(actual_capacity)
                        level += 1
                        find_path = True
                        break
            if find_path == False:
                dfs_trayectory[level - 1].remove(source)
                trayectory.pop()
                bottleneck.pop()
                level -= 1
            

if __name__ == '__main__':
    print(solution([0,1], [28,29,30], [[0,0,50,20,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0], 
[0,0,0,0,65,30,0,28,0,0,0,0,0,0,0,32,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,40,20,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,30,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,15,20,8,0,0,0,15,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0], 
[0,0,0,0,0,0,15,0,0,0,0,15,0,0,0,0,0,0,0,0,4,0,0,20,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,10,8,9,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,45,0,0,0,0,30,0,0,0,0,14,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,42,0,0,14,0,0,0,0,12,0,0,0,0,0,0,0,15,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,40,0,50,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,8,0,0,0,0,0,0,45,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,30,16,0,0,0,0,0,32,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,22,24,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,10,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,0,0,0,0,0,12,13,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,0,0,0,0,0,0,20,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,23,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,20,0,0,0,0,0,0,0,0,0,0,0,0,0,56,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,42,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,50,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,12,50,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,82,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,32,0,0,0,0,0,0,0,0,0,0,30,25], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,40], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,20], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]))