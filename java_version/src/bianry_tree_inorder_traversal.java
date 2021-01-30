public class bianry_tree_inorder_traversal {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> vals = new ArrayList<Integer>();
        if (root != null){
            List<TreeNode> stack = new ArrayList<TreeNode>();
            stack.add(root);
            TreeNode curr = root.left;
            int stack_size = 0;

            while(true){
                if (curr!=null){
                    stack.add(curr);
                    stack_size += 1;
                    curr = curr.left;
                }
                else if(!stack.isEmpty()){
                    curr = stack.remove(stack_size);
                    stack_size -= 1;
                    vals.add(curr.val);
                    curr = curr.right;
                }
                else{
                    break;
                }
            }
        }

        return vals;
    }
}
