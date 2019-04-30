import java.util.Arrays;

class Solution{
    public static void main(String[] args){
        Solution s = new Solution();
        int[][] grid = {
            {0, 1, 0, 1},
            {1, 1, 1, 0},
            {1, 0, 0, 1},
            {1, 1, 1, 1}
        };
        System.out.println(s.no_island(grid));
    }
    public int no_island(int[][] grid){
        // problematic ?
        int m = grid.length;
        int n = m == 0 ? 0 : grid[0].length;

        int[] parent = new int[n * m + 1];
        int[] rank = new int[n * m + 1];
        Arrays.fill(parent, -1);
        int res = 0;
        int[][] d = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        for (int i = 0; i < m; i ++){
            for (int j = 0; j < n; j ++){
                if (grid[i][j] == 1){
                    parent[i * n + j] = i * n + j;
                }
                boolean flag = false;
                for (int []p : d){
                    int x = i + p[0], y = j + p[1];
                    if (x >= 0 && x < m && y >= 0 && y < n){
                        if (find(x * n + y, parent) != -1) {
                            flag = true;
                            if (rank[i * n + j] >= rank[x * n + j]){
                                parent[x * n + j] = parent[i * n + j];
                                rank[i * n + j] += 1;
                            }else {
                                parent[i * n + j] = parent[x * n + y];
                                rank[x * n + j] += 1;
                            }
                        }
                    }
                }
                res += flag ? 0 : 1; 
            }
        }

        return res;
    }

    public int no_island_dfs(int[][] grid){
        int m = grid.length;
        int n = m == 0 ? 0 : grid[0].length;
        int res = 0;
        for (int i = 0; i < m; i ++){
            for (int j = 0; j < n; j ++){
                if (grid[i][j] == 1){
                    dfs(i, j, m, n, grid);
                    res += 1;
                }
            }
        }
        return res;
    }

    public void dfs(int i, int j, int m, int n, int[][] grid){
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == 0) return;
        grid[i][j] = 0;
        int[][] d = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        for (int[]p : d){
            System.out.print(p[0] + ":" + p[1] + "\n");
            int x = i + p[0];
            int y = j + p[1];
            dfs(x, y, m, n, grid);
        }
    }

    public int find(int i, int[] parent){
        if (i != parent[i] && parent[i] != -1){
            parent[i] = find(parent[i], parent);
        }
        return parent[i];
    }
}