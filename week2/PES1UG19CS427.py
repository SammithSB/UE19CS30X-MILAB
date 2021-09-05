

"""
You can create any other helper funtions.
Do not modify the given functions
"""


def update_frontier_with_min(frontier, index, canditate_cost):
    if(frontier[index][0] < canditate_cost):
        return
    if(frontier[index][0] > canditate_cost):
        frontier[index][0] = canditate_cost
        return
    return


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
    path = [start_point]
    # TODO
    explored = []

    frontier = [[heuristic[start_point], path]]

    def get_path_list(frontier):
        path_list = []
        for i in frontier:
            path_list.append(i[1])
        return path_list
    while len(frontier) > 0:
        curr_cost, curr_path = frontier.pop(0)
        n = curr_path[-1]
        curr_cost -= heuristic[n]
        if n in goals:
            return curr_path
        append_to_list(explored, n)
        children = [i for i in range(len(cost[0]))
                    if cost[n][i] not in [0, -1]]
        for i in children:
            new_curr_path = curr_path + [i]
            new_path_cost = curr_cost + cost[n][i] + heuristic[i]
            if i not in explored:
                if new_curr_path not in get_path_list(frontier):
                    to_append = list((new_path_cost, new_curr_path))
                    append_to_list(frontier, to_append)
                    frontier = sorted(frontier, key=lambda x: (x[0], x[1]))
            elif new_curr_path in get_path_list(frontier=frontier):
                index = (index for index in range(len(frontier))
                         if(frontier[index][1] == path))
                update_frontier_with_min(frontier, index, new_path_cost)
                frontier = sorted(frontier, key=lambda x: (x[0], x[1]))
    return path


def append_to_list(lis, to_append):
    lis.append((to_append))


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
        appa = {}
        # TODO
        n = len(cost)
        node = start_point
        visited = [0]*n
        visited[start_point] = 1
        '''
        makkalu = [i for i in range(n)
                   if cost[node][i] not in [0, -1]]
        '''
        makkalu = []
        i = 0
        for i in range(i):
            if(cost[node][i] not in [0, -1]):
                makkalu.append(i)
        visited[node] = 1
        path.append(node)
        if(node in goals):
            # print("goal : ",node)
            return path
        for j in range(1, n):
            # valid path
            makkalu = [i for i in range(n)
                       if cost[node][i] not in [0, -1]]
            for child in makkalu:
                if(cost[node][child] > 0 and visited[child] == 0):
                    appa[child] = node
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
                    node = appa[node]
                    appa.pop(k)

            # print("appa :", appa)
            # print(path)
        return path

    except KeyError:
        # In case goal is not reachable at all
        return list()
