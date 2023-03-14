from collections import defaultdict
import sys

sys.setrecursionlimit(int(1e6))

def solution(edges, target):
    edge_dict = defaultdict(list)
    tree_dict = defaultdict(list)
    visited = [False] * len(target)
    visited[0] = True

    for parent, child in edges:
        edge_dict[parent - 1].append(child - 1)
        # edge_dict[child - 1].append(parent-1)
    
    def dfs(node):
        child_list = []
        for child in edge_dict[node]:
            if visited[child]:
                continue
            visited[child] = True
            child_list.append(child)
        if not child_list:
            return [node]
        tree_dict[node].extend([0, sorted(child_list)])
        leaf_list = []
        for child in child_list:
            leaf_list.extend(dfs(child))
        return leaf_list
    
    def search(node):
        if len(tree_dict[node]) == 0:
            return node
        idx = tree_dict[node][0]
        tree_dict[node][0] = (tree_dict[node][0] + 1) % len(tree_dict[node][1])
        return search(tree_dict[node][1][idx])

    leaf_list = dfs(0)
    print(leaf_list)
    print(tree_dict)
    leaf_cap_dict = {key:0 for key in leaf_list}
    is_leaf_succeeded = {key:False if target[key] > 0 else True for key in leaf_list}
    order_list = []
    print(is_leaf_succeeded)

    while False in is_leaf_succeeded.values():
        cur_node = search(0)
        leaf_cap_dict[cur_node] += 1
        if leaf_cap_dict[cur_node] > target[cur_node]:
            return [-1]
        if not is_leaf_succeeded[cur_node] and target[cur_node] <= leaf_cap_dict[cur_node] * 3:
            is_leaf_succeeded[cur_node] = True
        order_list.append(cur_node)

    answer = [0] * len(order_list)
    print(order_list)
    for leaf in leaf_list:
        leaf_result = []
        sur_cap = target[leaf] - leaf_cap_dict[leaf]
        leaf_result = [1] * (leaf_cap_dict[leaf] - sur_cap % 2 - sur_cap // 2) + \
                        [2] * (sur_cap % 2) + [3] * (sur_cap // 2)
        # for idx, node in enumerate()
        # print(leaf_result)
        for idx, node in enumerate(order_list):
            if node == leaf:
                answer[idx] = leaf_result.pop(0)

    return answer

print(solution([[2, 4], [1, 2], [6, 8], [1, 3], [5, 7], [2, 5], [3, 6], [6, 10], [6, 9]], [0, 0, 0, 3, 0, 0, 5, 1, 2, 3]))

