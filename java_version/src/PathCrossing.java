class Solution {
    public boolean isPathCrossing(String path) {
        int x = 0;
        int y = 0;
        Set <Integer> visited = new HashSet<Integer>();
        // String currState = String.valueOf(curr[0]) + '#' + String.valueOf(curr[1]);
        visited.add(x*10000 + y);
        for (char m: path.toCharArray()){
            if (m == 'N'){
                y += 1;
            }
            else if (m == 'S'){
                y -= 1;
            }
            else if (m == 'E'){
                x += 1;
            }
            else if (m == 'W'){
                x -= 1;
            }
            // currState = String.valueOf(curr[0]) + '#' + String.valueOf(curr[1]);
            if (visited.contains(x*10000 + y))
                return true;
            
            visited.add(x*10000 + y);
        }
        return false;
    }
}