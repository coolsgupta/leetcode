public class ReverseWordsinaStringIII {
    public String reverseWords(String s) {
        String[] words = s.split(" ");
        StringBuilder res = new StringBuilder();
        boolean flag = false;
        for (String x: words){
            StringBuilder y = new StringBuilder(x);

            if (flag)
                y.append(" ");

            flag = true;
            res.append(y.reverse());
        }
        return res.toString();
    }
}
