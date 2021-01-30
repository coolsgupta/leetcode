public class RemoveAllAdjacentDuplicatesInString {
    public String removeDuplicates(String S) {
        StringBuilder res = new StringBuilder();
        for (char x: S.toCharArray()){
            int res_length = res.length()-1;
            if (res_length >= 0 && res.charAt(res_length) == x)
                res.deleteCharAt(res_length);
            else
                res.append(x);
        }
        return res.toString();
    }
}
