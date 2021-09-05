"""
You can create any other helper funtions.
Do not modify the given functions
"""

cost = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 9, -1, 6, -1, -1, -1, -1, -1],
        [0, -1, 0, 3, -1, -1, 9, -1, -1, -1, -1],
        [0, -1, 2, 0, 1, -1, -1, -1, -1, -1, -1],
        [0, 6, -1, -1, 0, -1, -1, 5, 7, -1, -1],
        [0, -1, -1, -1, 2, 0, -1, -1, -1, 2, -1],
        [0, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1],
        [0, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1],
        [0, -1, -1, -1, -1, 2, -1, -1, 0, -1, 8],
        [0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 7],
        [0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0]]
heuristic = [0, 5, 7, 3, 4, 6, 0, 0, 6, 5, 0]
start = 1
goals = [8]


def A_star_Traversal(cost, heuristic, start_point, goals):
    """
    Perform A* Traversal and find the optimal path 
    Args:
        cost: cost matrix (list of floats/int)
        heuristic: heuristics for A* (list of floats/int)
        start_point: Staring node (int)
        goals: Goal states (list of ints)
    Returns:
        path: path to goal state obtained from A*(list of ints)
    """
    path = []
    # TODO

    return path


def all_visited_child(cost, i, visited):
    for j in range(1, len(cost)):
        if(cost[i][j] > 0 and not (visited[j])):
            return 0
    return 1


def DFS_Traversal(cost, start_point, goals):
    """
    Perform DFS Traversal and find the optimal path
        cost: cost matrix(list of floats/int)
        start_point: Staring node(int)
        goals: Goal states(list of ints)
    Returns:
        path: path to goal state obtained from DFS(list of ints)
    """
    try:
        # just check if atleast one path to goal exists
        path = []
        parent = {}
        # TODO
        n = len(cost)
        node = start_point
        visited = [0]*n
        visited[start_point] = 1

        children = [i for i in range(n)
                    if cost[node][i] not in [0, -1]]
        visited[node] = 1
        path.append(node)
        if(node in goals):
            # print("goal : ",node)
            return path
        for j in range(1, n):
            # valid path
            children = [i for i in range(n)
                        if cost[node][i] not in [0, -1]]
            for child in children:
                if(cost[node][child] > 0 and visited[child] == 0):
                    parent[child] = node
                    node = child
                    path.append(node)
                    visited[node] = 1
            if(node in goals):
                # print("goal : ",node)
                return path
            else:
                while(all_visited_child(cost, node, visited)):
                    path.remove(node)
                    # print(path)
                    k = node
                    node = parent[node]
                    parent.pop(k)

            # print("parent :", parent)
            # print(path)
        return path

    except KeyError:
        # In case goal is not reachable at all
        return list()


x = DFS_Traversal(cost, start, goals)
print(x)
