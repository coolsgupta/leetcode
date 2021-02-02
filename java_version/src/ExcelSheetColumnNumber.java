public class ExcelSheetColumnNumber {
    public int titleToNumber(String s) {
        int pow = 0;
        int num = 0;
        char[] clms = s.toCharArray();
        for(int i=clms.length - 1; i>=0; i--){
            num += (int)(clms[i] - 'A' + 1)*Math.pow(26, pow);
            pow += 1;
        }
        return num;
    }
}
