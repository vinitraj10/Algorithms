#include <iostream>
#include <vector>

using namespace std;

vector <int> adj[2];

int main(){
	int nodes,edges,x,y;
	cin >> nodes; //No of Nodes.
	cin >> edges; //No of edges.

	for(int i=0;i<edges;i++){
		cin >> x >>y;
		adj[x].push_back(y);
	}



	for(int i=1;i<=nodes;i++){
		cout << "Adjancency List for " << i <<": ";
		for(int j=0;j<adj[i].size();j++){
			cout << adj[i][j] << " ";
		}
		cout << endl;
	}
	return 0;
}

