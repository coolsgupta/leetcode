class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        if (rooms.size() == 0 || (rooms.size() == 1 && rooms.get(0).size() == 0))
            return true;
        
        Set <Integer> visited = new HashSet<Integer>();
        ArrayList<Integer> queue = new ArrayList<Integer>();
        
        queue.addAll(rooms.get(0));
        visited.add(0);
        
        while(!queue.isEmpty()){
            int curr = queue.remove(0);
            if (!visited.contains(curr)){
                visited.add(curr);
                queue.addAll(rooms.get(curr));
            }
        }
        if (visited.size() == rooms.size())
            return true;
        
        return false;
    }
}