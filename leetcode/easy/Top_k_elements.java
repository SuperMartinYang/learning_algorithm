import java.util.*;

public class Top_k_elements{
    public static void main(String[] args) {
        String[] ss = { "heelo", "heloo", "hello", "hello", "heloo", "hello" };
        List<String> words = Arrays.asList(ss);
        System.out.println(topK(words, 1));
    }

    public static List<String> topK(List<String> words, int k) {
        Map<String, Integer> mp = new HashMap<>();
        for (String word : words) {
            mp.put(word, mp.getOrDefault(word, 0) + 1);
        }
        // init the priorityqueue
        PriorityQueue<Map.Entry<String, Integer>> pq = new PriorityQueue<>(k, new Comparator<Map.Entry<String, Integer>>() {
            public int compare(Map.Entry<String, Integer> a, Map.Entry<String, Integer> b){
                return a.getValue() > b.getValue() ? 1 : -1;
            }
        });
        for (Map.Entry<String, Integer> a: mp.entrySet()){
            if (pq.size() == k) pq.poll();
            pq.add(a);
        }
        List<String> res = new ArrayList<>();
        while (pq.size() > 0){
            res.add(pq.poll().getKey());
        }
        return res;
    }
}