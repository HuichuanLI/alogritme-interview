"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import defaultdict


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        node_memo = defaultdict(Node)
        self.dfs(node, node_memo)
        root = node
        for node in node_memo.keys():
            for elem in node.neighbors:
                node_memo[node].neighbors.append(node_memo[elem])
        return node_memo[root]

    def dfs(self, node, node_memo):
        if not node:
            return
        node_memo[node] = Node(node.val)
        for elem in node.neighbors:
            if elem not in node_memo:
                self.dfs(elem, node_memo)
