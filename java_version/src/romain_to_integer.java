class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> vals = new HashMap<>();

        vals.put('M', 1000);
        vals.put('D', 500);
        vals.put('C', 100);
        vals.put('L', 50);
        vals.put('X', 10);
        vals.put('V', 5);
        vals.put('I', 1);

        int last_val = vals.get(s.charAt(s.length()-1));;
        int total = last_val;

        for (int i = s.length() - 2; i>=0; i--){
            int current_val = vals.get(s.charAt(i));
            if (current_val < last_val){
                total -= current_val;
            }
            else{
                total += current_val;
            }
            last_val = current_val;
        }
        return total;

    }
}