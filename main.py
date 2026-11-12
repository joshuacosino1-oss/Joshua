from collections import deque

# ==========================================
# 1. BINARY TREE IMPLEMENTATION (COSINO)
# ==========================================
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_val):
        self.root = TreeNode(root_val)

    def bfs(self):
        result = []
        if not self.root:
            return result
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def dfs_preorder(self, node, result=None):
        if result is None:
            result = []
        if node:
            result.append(node.val)
            self.dfs_preorder(node.left, result)
            self.dfs_preorder(node.right, result)
        return result


# ==========================================
# 2. GRAPH IMPLEMENTATION (COSINO)
# ==========================================
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start_node):
        visited = set([start_node])
        queue = deque([start_node])
        result = []

        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            for neighbor in self.adj_list.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def dfs(self, start_node, visited=None, result=None):
        if visited is None:
            visited = set()
        if result is None:
            result = []

        visited.add(start_node)
        result.append(start_node)

        for neighbor in self.adj_list.get(start_node, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited, result)
        return result


# ==========================================
# EXECUTION / TESTING
# ==========================================
if __name__ == "__main__":
    print("--- BINARY TREE (COSINO) ---")
    tree = BinaryTree('C')
    tree.root.left = TreeNode('O')
    tree.root.right = TreeNode('S')
    tree.root.left.left = TreeNode('I')
    tree.root.left.right = TreeNode('N')

    print("BFS Traversal:", " -> ".join(tree.bfs()))
    print("DFS Traversal:", " -> ".join(tree.dfs_preorder(tree.root)))

    print("\n--- GRAPH (COSINO) ---")
    g = Graph()
    edges = [('C', 'O'), ('C', 'S'), ('O', 'I'), ('O', 'N'), ('I', 'N'), ('S', 'N')]
    for u, v in edges:
        g.add_edge(u, v)

    print("BFS Traversal (starting at C):", " -> ".join(g.bfs('C')))
    print("DFS Traversal (starting at C):", " -> ".join(g.dfs('C')))