public class MeetingScheduler {
    public List<Integer> minAvailableDuration(int[][] slots1, int[][] slots2, int duration) {
        Arrays.sort(slots1, (a, b) -> Integer.compare(a[0], b[0]));
        Arrays.sort(slots2, (a, b) -> Integer.compare(a[0], b[0]));
        int i = 0;
        int j = 0;
        List<Integer> soln = new ArrayList<Integer>();
        while (i < slots1.length && j < slots2.length) {
            if (slots1[i][0] >= slots2[j][1]) {
                j++;
                continue;
            }

            if (slots2[j][0] >= slots1[i][1]) {
                i++;
                continue;
            }

            int ms = (slots1[i][0] > slots2[j][0]) ? slots1[i][0] : slots2[j][0];
            int me = (slots1[i][1] < slots2[j][1]) ? slots1[i][1] : slots2[j][1];
            if (me - ms >= duration) {
                soln.add(ms);
                soln.add(ms + duration);
                break;
            }
            if (slots1[i][1] - ms < duration)
                i++;

            if (slots2[j][1] - ms < duration)
                j++;
        }
        return soln;
    }
}
