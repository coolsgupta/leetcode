public class binary_tree_preorder_traversal {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> vals = new ArrayList<Integer>();
        if (root!=null){
            List<TreeNode> stack = new ArrayList<TreeNode>();
            TreeNode curr = root;
            int stack_size = -1;

            while(true){
                if (curr!=null){
                    vals.add(curr.val);
                    stack.add(curr);
                    stack_size += 1;
                    curr = curr.left;
                }
                else if(!stack.isEmpty()){
                    curr = stack.remove(stack_size);
                    stack_size -= 1;
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
