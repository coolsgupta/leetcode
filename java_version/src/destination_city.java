public class destination_city {
    public String destCity(List<List<String>> paths) {
        Set<String> src = new HashSet<String>();
        Set<String> des = new HashSet<String>();

        while(!paths.isEmpty()){
            List<String> pair = paths.remove(0);
            src.add(pair.get(0));
            des.add(pair.get(1));
        }
        des.removeAll(src);
        return des.iterator().next();
    }
}
