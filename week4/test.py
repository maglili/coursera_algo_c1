import random
import gc
import numpy as np
# random.seed(0)


def remove_old_vertice(array, vertice1, vertice2):
    while (vertice1 in array) or (vertice2 in array):
        if vertice1 in array:
            array.remove(vertice1)
        if vertice2 in array:
            array.remove(vertice2)
    return array


def remove_old_vertice_while_add_new(array, vertice1, vertice2, new_node):
    while (vertice1 in array) or (vertice2 in array):
        if vertice1 in array:
            array.remove(vertice1)
            array.append(new_node)
        if vertice2 in array:
            array.remove(vertice2)
            array.append(new_node)
    return array


def karger_sub():
    count = 0
    while len(adjacency_lists) > 2:
        v1 = random.choice(list(adjacency_lists.keys()))
        v2 = random.choice(list(adjacency_lists[v1]))
        while v1 == v2:
            v2 = random.choice(list(adjacency_lists[v1]))
        merge = adjacency_lists[v1] + adjacency_lists[v2]
        merge = remove_old_vertice(merge, v1, v2)
        adjacency_lists['N' + str(count)] = merge

        # update adjacency lists
        for vertice in adjacency_lists[v1]:
            adj = adjacency_lists[vertice]
            adj = remove_old_vertice_while_add_new(
                adj, v1, v2, 'N' + str(count))
            adjacency_lists[vertice] = adj

        for vertice in adjacency_lists[v2]:
            adj = adjacency_lists[vertice]
            adj = remove_old_vertice_while_add_new(
                adj, v1, v2, 'N' + str(count))
            adjacency_lists[vertice] = adj

        # remove old adjaceny list
        del adjacency_lists[v1], adjacency_lists[v2]
        gc.collect()
        # print(adjacency_lists)
        count += 1

    ans = list(adjacency_lists.values())
    if len(ans[0]) != len(ans[1]):
        print('error!')
        quit()
    else:
        return len(ans[0])


def karger():
    N = len(adjacency_lists)**3  # * np.log(len(adjacency_lists))
    trails = int(round(N))
    print('N:', N)
    print('totoal trials:', trails)
    minima = np.inf
    for i in range(trails):
        if i % int(0.1*trails) == 0:
            print('Precessing:', i)
        ans = karger_sub()
        if ans < minima:
            minima = ans
            print(minima)
    return minima


if __name__ == '__main__':
    adjacency_lists = dict()
    path = './kargerMinCut.txt'
    #path = './test.txt'
    with open(path, 'r') as fh:
        for i in fh:
            adj_list = i.split()
            adjacency_lists[adj_list[0]] = adj_list[1:]

    ans = karger()
    # print(adjacency_lists)
    print(ans)
