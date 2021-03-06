public class WordDistance {
    Map<String, ArrayList<Integer>> words;
    int length;

    public WordDistance(String[] words) {
        this.words = new HashMap<String, ArrayList<Integer>>();
        for (int i=0; i<words.length; i++){
            if (!this.words.containsKey(words[i])){
                this.words.put(words[i], new ArrayList<Integer>());
            }
            this.words.get(words[i]).add(i);
        }
        this.length = words.length;
    }

    public int shortest(String word1, String word2) {
        ArrayList<Integer> word1_indices = this.words.get(word1);
        ArrayList<Integer> word2_indices = this.words.get(word2);
        int diff = this.length;
        for (int i=0; i< word1_indices.size(); i++){
            for(int j=0; j<word2_indices.size(); j++){
                diff = Math.min(diff, Math.abs(word1_indices.get(i)-word2_indices.get(j)));
                if (diff<=1)
                    return diff;
            }
        }
        return diff;
    }

    // optimized
    public int shortest(String word1, String word2) {
        ArrayList<Integer> word1_indices = this.words.get(word1);
        ArrayList<Integer> word2_indices = this.words.get(word2);
        int diff = this.length;
        int i = 0;
        int j = 0;
        while(i<word1_indices.size() && j<word2_indices.size()){
            int x = word1_indices.get(i);
            int y = word2_indices.get(j);
            diff = Math.min(diff, Math.abs(x-y));
            if (diff<=1)
                return diff;

            if (x<y){
                i++;
            }
            else{
                j++;
            }
        }
        return diff;
    }

}
