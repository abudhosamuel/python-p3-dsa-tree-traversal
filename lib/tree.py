class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        """
        Uses depth-first search to find the node with the specified 'id'.
        If no such node is found, returns None.
        """
        # Helper function to traverse the tree
        def dfs(node):
            if node is None:
                return None
            # If the current node has the matching 'id', return the node
            if node.get('id') == id:
                return node
            # Recursively search in the children of the current node
            for child in node.get('children', []):
                result = dfs(child)
                if result is not None:
                    return result
            return None

        return dfs(self.root)
