public class FindKClosestElements {
    public int find(int[] arr, int k){
        int beg = 0;
        int end = arr.length - 1;
        int mid = (beg + end)/2;
        while(beg <= end){
            if (arr[mid] == k)
                break;

            if (arr[mid] < k)
                beg = mid + 1;

            else
                end = mid - 1;
            mid = (beg + end)/2;
        }
        return mid;
    }

    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int base = this.find(arr, x);
        int lp = base;
        int rp = base + 1;
        int req_len = 0;
        while(req_len < k){
            if ((rp==arr.length) || (lp >= 0 && x - arr[lp] <= arr[rp] - x))
                lp --;
            else
                rp++;
            req_len ++;
        }

        List<Integer> res = new ArrayList<Integer>();
        // System.out.println(rp);
        // System.out.println(lp);
        // System.out.println(base);

        for (int i= lp+1; i<rp; i++){
            res.add(arr[i]);
        }
        return res;
    }
}
