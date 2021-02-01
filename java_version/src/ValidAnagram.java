public class ValidAnagram {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> sCounter = new HashMap<Character, Integer>();
        Map<Character, Integer> tCounter = new HashMap<Character, Integer>();

        for (char x:s.toCharArray()){
            if (!sCounter.containsKey(x)){
                sCounter.put(x, 0);
            }
            sCounter.put(x, sCounter.get(x) + 1);
        }

        for (char x:t.toCharArray()){
            if (!tCounter.containsKey(x)){
                tCounter.put(x, 0);
            }
            tCounter.put(x, tCounter.get(x) + 1);
        }

        return sCounter.equals(tCounter);
    }
}
