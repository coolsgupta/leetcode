def levelOrderBottom(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []

    level_map = {
        0: [root.val]
    }

    def get_level(node, p_level):
        if node.left:
            if not p_level + 1 in level_map:
                level_map[p_level + 1] = []
            level_map[p_level + 1].append(node.left.val)
            get_level(node.left, p_level + 1)
        if node.right:
            if not p_level + 1 in level_map:
                level_map[p_level + 1] = []
            level_map[p_level + 1].append(node.right.val)
            get_level(node.right, p_level + 1)

    get_level(root, 0)
    values = level_map.values()
    values.reverse()
    return values