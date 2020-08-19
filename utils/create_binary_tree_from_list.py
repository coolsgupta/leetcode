# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree(tree_nodes, root=None, current_node_index=0):
    if current_node_index < len(tree_nodes):
        if tree_nodes[current_node_index]:
            root = TreeNode(tree_nodes[current_node_index])
            root.left = create_tree(tree_nodes, root.left, 2*current_node_index + 1)
            root.right = create_tree(tree_nodes, root.right, 2*current_node_index + 2)

    return root


def print_tree(root):
    if root:
        if root:
            print(root.val)
            print_tree(root.left)
            print_tree(root.right)

        else:
            print(None)

if __name__ == '__main__':
    arr = [2,1,3,None,4,None,7]
    root = create_tree(arr, None, 0)
    print_tree(root)