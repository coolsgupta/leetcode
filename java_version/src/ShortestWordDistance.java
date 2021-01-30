public class ShortestWordDistance {
    public int shortestDistance(String[] words, String word1, String word2) {
        int x=-1;
        int y=-1;
        int diff = words.length;
        for (int i=0; i<words.length; i++){
            if (words[i].equals(word1))
                x = i;
            else if (words[i].equals(word2))
                y = i;

            if (x!=-1 && y!=-1)
                diff = Math.min(diff, Math.abs(x-y));
        }
        return diff;
    }
}
