#include <iostream>
#include <vector>
#include <utility>
#include <queue>
#include <algorithm>
using namespace std;

void deleteDupValue(vector<int>& arr) { 
    sort(arr.begin(), arr.end());
    int cnt = 0, i;
    for (i = 0; i < arr.size(); i ++){
        if (arr[i] == arr[i - 1]) cnt ++;
        else arr[i - cnt] = arr[i];
    }
    // for (auto a:arr) cout<<a<<endl;
    // cout<<'\n'<<endl;
    while (cnt + 1 < i){
        arr.pop_back();
        cnt ++;
    }
} 

int fibonacci(const int n){
    vector<int> dp(n + 1, 0);
    dp[0] = 0;
    dp[1] = 1;
    for (int i = 2; i < n + 1; i ++){
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    return dp[n];
}

struct Node{
    int val;
    Node* left;
    Node* right;
};

Node* insertRecursive(Node* root, int val){
    if (!root) return root;
    if (val < root->val){
        if (!root->left) root->left = new Node({val, NULL, NULL});
        else root->left = insertRecursive(root->left, val);
    } else {
        if (!root->right) root->right = new Node({val, NULL, NULL});
        else root->right = insertRecursive(root->right, val);
    }
    return root;
}

void insert(Node* root, int val){
    insertRecursive(root, val);
}

bool dfs(vector<vector<char>>& grid, int i, int j, int m, int n, vector<pair<int,int>>& res, vector<vector<bool>>& visited, vector<pair<int,int>>& directions){
    if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == '*' || visited[i][j]) return false;
    visited[i][j] = true;
    res.push_back(make_pair(i, j));
    if (i == m - 1 && j == n - 1) {
        return true;
    }
    for (auto p: directions){
        if (dfs(grid, i + p.first, j + p.second, m, n, res, visited, directions)) return true;
    }
    res.pop_back();
    return false;
}

void maze(vector<vector<char>>& grid, int i, int j){
    int m = grid.size();
    int n = m > 0 ? grid[0].size() : 0;
    vector<pair<int, int>> res;
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    vector<pair<int, int>> directions;
    directions.push_back(make_pair(0, 1));
    directions.push_back(make_pair(0, -1));
    directions.push_back(make_pair(1, 0));
    directions.push_back(make_pair(-1, 0));
    dfs(grid, i, j, m, n, res, visited, directions);
    // print res;
    for (auto p : res){
        cout << p.first << ',' << p.second << endl;
    }
}


int main(){
    // problem 1:
    cout << "Problem1:" << endl;
    vector<int> arr({2,3,4,5,2,2,4});
    deleteDupValue(arr);
    for (auto a: arr) 
        cout << a << ' ';
    cout << endl;
    // problem 2:
    cout << "Problem2: " << endl;
    cout << fibonacci(8) << endl;

    cout << "Problem3: " << endl;
    Node* root = new Node({4, NULL,NULL});
    root->left = new Node({2, NULL, NULL});
    root->right = new Node({7, NULL, NULL});
    insert(root, 3);
    // go thru tree, print it
    queue<Node*> q;
    q.push(root);
    while (!q.empty()){
        Node* a = q.front(); q.pop();
        cout << a->val << endl;
        if (a->left) q.push(a->left);
        if (a->right) q.push(a->right);
    }

    cout << "Problem4: " << endl;
    vector<vector<char>> grid;
    grid.push_back(vector<char>({'*', '0', '*', '*', '*', '*'}));
    grid.push_back(vector<char>({'*', '0', '*', '*', '*', '*'}));
    grid.push_back(vector<char>({'0', '0', '*', '*', '*', '*'}));
    grid.push_back(vector<char>({'*', '0', '0', '0', '*', '*'}));
    grid.push_back(vector<char>({'*', '0', '*', '0', '0', '*'}));
    grid.push_back(vector<char>({'*', '*', '*', '*', '0', '0'}));
    maze(grid, 0, 1);
    return 0;
}