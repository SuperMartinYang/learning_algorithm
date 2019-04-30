import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Set;
import java.util.Queue;

class Vertex implements Comparable<Vertex> {
	
	private Integer id;
	private Integer weight;
	public Vertex(Integer id, Integer weight) {
		super();
		this.id = id;
        this.weight = weight;
    }

    /**
     * @return the id
     */
    public Integer getId() {
        return id;
    }
    /**
     * @param id the id to set
     */
    public void setId(Integer id) {
        this.id = id;
    }
    /**
     * @return the weight
     */
    public Integer getWeight() {
        return weight;
    }
    /**
     * @param weight the weight to set
     */
    public void setWeight(Integer weight) {
        this.weight = weight;
    }

    @Override
	public String toString() {
		return id + "";
    }
    
    @Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result
				+ ((this.weight == null) ? 0 : weight.hashCode());
		result = prime * result + ((this.id == null) ? 0 : id.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Vertex other = (Vertex) obj;
		if (this.weight == null) {
			if (other.getWeight() != null)
				return false;
		} else if (this.weight != other.getWeight())
			return false;
		if (this.id == null) {
			if (other.getId() != null)
				return false;
		} else if (this.id != other.getId())
			return false;
		return true;
    }
    
    @Override
    public int compareTo(Vertex o) {
		if (this.weight < o.getWeight())
			return -1;
		else if (this.weight > o.getWeight())
			return 1;
        else
            return 0;
    }
}

class Graph {
    HashMap<Integer, ArrayList<Vertex>> vertices;
    public Graph(){
        this.vertices = new HashMap<>();
    }
    public void addVertex(Integer id, Vertex vertex) {
        ArrayList<Vertex> tl = this.vertices.getOrDefault(id, new ArrayList<>());
        tl.add(vertex);
        this.vertices.put(id, tl);
	}
}

public class Main {
    public static void main(String[] args){
        // get input
        Scanner sc = new Scanner(System.in);
        String cnt = sc.nextLine();
        String[] cnts = cnt.split(" ");
        Graph graph = new Graph();
        // graph.vertices = new HashSet<>();
        int vertexCnt = Integer.parseInt(cnts[0]);
        int edgeCnt = Integer.parseInt(cnts[1]);
        for (int i = 0; i < edgeCnt; i++){
            String eg = sc.nextLine();
            String [] para = eg.split(" ");
            int v1 = Integer.parseInt(para[0]);
            int v2 = Integer.parseInt(para[1]);
            int w = Integer.parseInt(para[2]);
            graph.addVertex(v1, new Vertex(v2, w));
            graph.addVertex(v2, new Vertex(v1, w));
        }
        String se = sc.nextLine();
        String[] sne = se.split(" ");
        int s = Integer.parseInt(sne[0]);
        int e = Integer.parseInt(sne[1]);
        // dijkstra
        Main dig = new Main();
        ArrayList<ArrayList<Vertex>> res = dig.getShortestPath(graph, s, e);
        // get the total weight
        ArrayList<Vertex> realRes;
        for (ArrayList<Vertex> tr: res){
            Collections.reverse(tr);
        }
        Collections.sort(res, new Comparator<ArrayList<Vertex>>(){
            @Override
            public int compare(ArrayList<Vertex> o1, ArrayList<Vertex> o2) {
                if(o1.size() == o2.size()){
                    for(int i = 0; i < o1.size(); i ++){
                        if(o1.get(i).getId() == o2.get(i).getId()) continue;
                        return o1.get(i).getId() - o2.get(i).getId();
                    }
                }
                return o1.size() - o2.size();
            }
        });
        
        realRes = res.get(0);

        System.out.println(realRes.get(realRes.size() - 1).getWeight());
        for (int i = 0; i < realRes.size(); i ++)
            System.out.print(realRes.get(i) + (i == realRes.size() - 1 ? "" : " "));
        System.out.println();
    }
    public ArrayList<ArrayList<Vertex>> getShortestPath(Graph graph, int start, int end){
        HashMap<Integer, Integer> weights = new HashMap<>();
        HashMap<Integer, ArrayList<Vertex>> previous = new HashMap<>();
        PriorityQueue<Vertex> nodes = new PriorityQueue<>();
        ArrayList<ArrayList<Vertex>> path = new ArrayList<>();
        for (int vet : graph.vertices.keySet()){
            if (vet == start){
                weights.put(vet, 0);
                nodes.add(new Vertex(vet, 0));
            }else {
                weights.put(vet, Integer.MAX_VALUE);
                nodes.add(new Vertex(vet, Integer.MAX_VALUE));
            }
            previous.put(vet, new ArrayList<>());
        }
        while (!nodes.isEmpty()){
            Vertex smallest = nodes.poll();
            if (weights.get(smallest.getId()) == Integer.MAX_VALUE) break;
            if (smallest.getId() == end){
                // found it, get the shortest path with lower lexi, BFS to get it
                Queue<HashMap<Integer, ArrayList<Vertex>>> level = new LinkedList<>();
                HashMap<Integer, ArrayList<Vertex>> startMap = new HashMap<>();
                startMap.put(smallest.getId(), new ArrayList<>(Arrays.asList(smallest)));
                level.add(startMap);
                boolean flag = true;
                while (!level.isEmpty() && flag){
                    Queue<HashMap<Integer, ArrayList<Vertex>>> tmp = new LinkedList<>();
                    while (!level.isEmpty()){
                        HashMap<Integer, ArrayList<Vertex>> nd = level.poll();
                        Set<Integer> k = nd.keySet();
                        if (k.contains(start)){
                            flag = false;
                            path.add(new ArrayList<>(nd.get(start)));
                        }
                        for (Vertex v : previous.get(k.toArray()[0])){
                            HashMap<Integer, ArrayList<Vertex>> nmp = new HashMap<>();
                            ArrayList<Vertex> a = nd.get(k.toArray()[0]);
                            ArrayList<Vertex> na = new ArrayList<>(a);
                            na.add(v);
                            nmp.put(v.getId(), na);
                            tmp.add(nmp);
                        }
                    }
                    level = tmp;
                }
                return path;
            }
            for (Vertex neighbor : graph.vertices.get(smallest.getId())) {
				Integer alt = weights.get(smallest.getId()) + neighbor.getWeight();
                if (alt < weights.get(neighbor.getId())) {
                    weights.put(neighbor.getId(), alt);
                    ArrayList<Vertex> pv = new ArrayList<>();
                    pv.add(smallest);
                    previous.put(neighbor.getId(), pv);
					
					for(Vertex n : nodes) {
						if (n.getId() == neighbor.getId()) {
							nodes.remove(n);
                            n.setWeight(alt);
							nodes.add(n);
							break;
						}
					}
				} else if (alt == weights.get(neighbor.getId())){
                    ArrayList<Vertex> pv = previous.getOrDefault(neighbor.getId(), new ArrayList<>());
                    pv.add(smallest);
                    previous.put(neighbor.getId(), pv);
                }
            }
        }
        return new ArrayList<>();
    } 
}