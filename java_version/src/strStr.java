public class strStr {
    public int strStr(String haystack, String needle) {
        int i = 0;
        if (needle.length()== 0) return 0;

        while(i<=haystack.length()-needle.length()){
            if (haystack.charAt(i) == needle.charAt(0)){
                int j = 1;
                boolean flag = true;
                while(j<needle.length()){
                    if(haystack.charAt(i + j) != needle.charAt(j)){
                        flag = false;
                        break;
                    }
                    j++;
                }
                if(flag) return i;
            }
            i++;
        }
        return -1;
    }
}
