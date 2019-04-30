
import java.util.*;

public class minimum_spanning_tree {
    public static void main(String[] args){
        int[][] matrix = new int[][]{
            {0, 4, 3, 0, 0, 0},
            {4, 0, 1, 2, 0, 0},
            {0, 1, 0, 4, 0, 0},
            {0, 2, 4, 0, 2, 0},
            {0, 0, 0, 2, 0, 6},
            {0, 0, 0, 0, 6, 0}
        };
        int [][] matrix2 = new int[][]{
            {0, 3, 10, 4, 0},
            {3, 0, 9, 1, 5},
            {10, 9, 0, 0, 7},
            {4, 1, 7, 0, 4},
            {0, 5, 0, 4, 0}
        };
        System.out.println(new minimum_spanning_tree().prime_min_spanning_tree(matrix2, matrix2.length));
    }

    
    public int prime_min_spanning_tree(int[][] matrix, int n) {
        // given an undirected graph, return its min spanning tree's weight.
        // also print out min spanning tree's matrix
        ArrayList<Integer> cands = new ArrayList<>();
        Set<Integer> resultSet = new HashSet<>();
        int[][] resultMatrix = new int[n][n];
        int finalWeight = 0;
        // start with 0
        cands.add(0);
        resultSet.add(0);
        while (resultSet.size() < n){
            int[] a = getMin(matrix, resultSet, cands);
            resultSet.add(a[1]);
            cands.add(a[1]);
            resultMatrix[a[0]][a[1]] = matrix[a[0]][a[1]];
            resultMatrix[a[1]][a[0]] = matrix[a[0]][a[1]];
            finalWeight += matrix[a[0]][a[1]];
        }
        printMatrix(resultMatrix, n);
        return finalWeight;
    }

    public void printMatrix(int[][] resultMatrix, int n){
        for (int i = 0; i < n; i ++){
            for (int j = 0; j < n; j ++){
                System.out.print(resultMatrix[i][j] + " ");
            }
            System.out.println();
        }
    }
    public int[] getMin(int[][] matrix, Set<Integer> resultSet, ArrayList<Integer> cands){
        int minVal = Integer.MAX_VALUE;
        int[] minEdge = new int[2];
        for (int cand : cands){
            for (int con = 0; con < matrix.length; con ++){
                if (matrix[cand][con] != 0 && matrix[cand][con] < minVal && !resultSet.contains(con)){
                    minVal = matrix[cand][con];
                    minEdge[0] = cand;
                    minEdge[1] = con;
                }
            }
        }
        return minEdge;
    }
}