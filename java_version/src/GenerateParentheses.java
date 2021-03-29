class Solution {
    public List<String> generateParenthesis(int n) {
        ArrayList<String> ans = new ArrayList<String>();
        this.backtrack(ans, n, "", 0, 0);
        return ans;
    }
    
    public void backtrack(List<String> ans, int n, String curr, int open, int close){
        if (curr.length() == n*2){
            ans.add(curr);
            return;
        }
        
        if (open < n){
            this.backtrack(ans, n, curr + "(", open + 1, close);
        }
        if (close < open){
            this.backtrack(ans, n, curr + ")", open, close + 1);
        }
    }
}