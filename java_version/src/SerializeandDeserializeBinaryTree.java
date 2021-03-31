/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {
    
    int i;
    String[] nodes;
    public String serialize(TreeNode root, String str){
        if (root==null){
            str += "None,";
        }
        else{
            str += str.valueOf(root.val) + ",";
            str = serialize(root.left, str);
            str = serialize(root.right, str);
        }
        return str;
    }

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        String res = serialize(root, "");
        // System.out.println(res);
        return res;
    }
    
    public TreeNode dfs(){
        if (this.nodes.length == 0 || this.nodes[i].equals("None")){
            this.i++;
            return null;
        }
        TreeNode root = new TreeNode(Integer.parseInt(this.nodes[this.i]));
        this.i++;
        // System.out.println(this.i);
        if (this.i < this.nodes.length)
            root.left = dfs();
        
        if (this.i < this.nodes.length)
            root.right = dfs();
        
        return root;
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        this.nodes = data.split(",");
        // System.out.println(Arrays.toString(nodes));
        if (this.nodes.length == 1 && this.nodes[0] == "None"){
            return null;
        }
        this.i = 0;
        return dfs();        
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));