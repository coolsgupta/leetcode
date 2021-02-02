public class BinaryTreeLevelOrderTraversal {
    Map<Integer, ArrayList<Integer>> orderTraversal;
    public void bfs(TreeNode root, int level){
        if (root == null) return;
        if (!this.orderTraversal.containsKey(level))
            this.orderTraversal.put(level, new ArrayList<Integer>());

        this.orderTraversal.get(level).add(root.val);
        this.bfs(root.left, level+1);
        this.bfs(root.right, level+1);
    }

    public List<List<Integer>> levelOrder(TreeNode root) {
        this.orderTraversal = new HashMap<Integer, ArrayList<Integer>>();
        this.bfs(root, 0);
        return new ArrayList(this.orderTraversal.values());

    }
}
