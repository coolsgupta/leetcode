public class twosum {
    public static int countPairs(List<Integer> numbers, int k){
        Set<Integer> hashComp = new HashSet<Integer>();
        int count = 0;
        for (int i = 0; i < numbers.size(); i++){
            int comp = k + number.get(i);
            if (hashComp.contains(comp))
                count++;

            hashComp.add(number.get(i));
        }
        return count;
    }

}
