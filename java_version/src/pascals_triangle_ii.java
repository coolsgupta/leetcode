import java.util.ArrayList;
import java.util.List;

public class pascals_triangle_ii {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> res = new ArrayList<Integer>();
        res.add(1);

        if (rowIndex == 0)
            return res;

        for (int i = 1; i<rowIndex+1; i++){
            List<Integer> current_row = new ArrayList<Integer>();
            current_row.add(1);
            for (int j=1; j<i; j++){
                current_row.add(res.get(j-1) + res.get(j));
            }
            current_row.add(1);
            res = current_row;
        }
        return res;
    }
}
