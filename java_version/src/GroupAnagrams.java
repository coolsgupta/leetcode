public class GroupAnagrams {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, ArrayList<String>> groups = new HashMap<String, ArrayList<String>>();

        for(String s: strs){
            char[] sChars = s.toCharArray();
            Arrays.sort(sChars);
            String anagram = String.valueOf(sChars);
            if(!groups.containsKey(anagram)) groups.put(anagram, new ArrayList<String>());
            groups.get(anagram).add(s);
        }
        return new ArrayList(groups.values());

    }
}
