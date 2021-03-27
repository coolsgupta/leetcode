class Solution {
    public String reorderSpaces(String text) {
        int spaceCount = 0;
        ArrayList<String> words= new ArrayList<String>();
        StringBuilder currWord = new StringBuilder();
        
        for (char x: text.toCharArray()){
            if (x == ' '){
                if (currWord.length() > 0){
                    words.add(currWord.toString());
                    currWord = new StringBuilder();
                }
                spaceCount++;
            }
            else{
                 currWord.append(x);  
            }
        }
        if (currWord.length() > 0){
            words.add(currWord.toString());
        }
        int wordCount = words.size() - 1;
        int eqSpace = (wordCount > 0)? Math.abs(spaceCount/wordCount): 0;
        int exSpace = (wordCount > 0)? spaceCount%wordCount: spaceCount;
        StringBuilder res = new StringBuilder();
        res.append(words.get(0));
        for (int x = 1; x < words.size(); x++){
            for (int i=0; i<eqSpace; i++){
                res.append(' ');
            }
            res.append(words.get(x));
        }
        for (int i=0; i<exSpace; i++){
            res.append(' ');
        }
        
        return res.toString();   
    }
}