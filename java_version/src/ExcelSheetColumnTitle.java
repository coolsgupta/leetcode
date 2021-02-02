public class ExcelSheetColumnTitle {
    public String convertToTitle(int n) {
        String s = "";
        if (n==1){
            return "A";
        }
        while(n > 0){
            int c_i = n%26;
            if (c_i == 0){
                s = "Z" + s;
                n = n/26 - 1;
            }
            else{
                s = (char)('A'+c_i - 1) + s;
                n = n/26;
            }
        }
        return s;
    }
    public String convertToTitleOptimized(int n) {
        StringBuilder res = new StringBuilder();
        while(n>0) {
            res.insert(0, ((char) ('A' + (n - 1) % 26)));
            n = (n - 1) / 26;
        }
        return res.toString();
        Math.pow()
    }
}
