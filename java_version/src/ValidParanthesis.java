public class ValidParanthesis {
    public boolean isValid(String s) {
        Stack<Character> para = new Stack<Character>();
        boolean flag = true;
        for(char x: s.toCharArray()){
            if (x=='('){
                para.push(')');
            }
            else if (x=='['){
                para.push(']');
            }
            else if (x=='{'){
                para.push('}');
            }
            else{
                if (para.isEmpty() || para.peek()!=x){
                    flag = false;
                    break;
                }
                para.pop();
            }
        }
        if (flag && para.isEmpty())
            return true;

        return false;
    }
}
