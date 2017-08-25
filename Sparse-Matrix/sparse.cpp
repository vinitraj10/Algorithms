#include <iostream>

using namespace std;

int main(){
	int sparseMatrix[3][4] = {
		{0,0,1,0},
		{0,2,0,0},
		{0,4,0,5},
	};

	int size = 0 ;//	size of new matrix
	for(int i=0;i<3;i++){
		for(int j=0;j<4;j++){
			if(sparseMatrix[i][j]!=0)
				size++;
		}
	}
	int k=0;
	int newMatrix[3][size];
	for(int i=0;i<3;i++){
		for(int j=0;j<4;j++){
			if(sparseMatrix[i][j]!=0){
				newMatrix[0][k]=i;
				newMatrix[1][k]=j;
				newMatrix[2][k]=sparseMatrix[i][j];
				k++;
			}
		}
	}
	//print new Matrix
	for(int i=0;i<3;i++){
		for(int j=0;j<size;j++)
			cout<<newMatrix[i][j]<<"\t";
		cout<<endl;
	}

}
/*
	output:-
	0 	1	2	2
	2	1	1	3
	1	2	4	5
	
*/