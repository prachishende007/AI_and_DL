#include<iostream>
#include<vector>
#include<set>
#include<algorithm>
using namespace std;

class SudokuSolver{
    vector<int> board;
    vector<set<int>> domains;
    vector<vector<int>> peers;

    public:
        SudokuSolver(vector<int> initial_board){
            if(initial_board.size() != 81){
                cout<<"Board must have 81 cells";
            }
            board = initial_board;
            initPeers();
        }

        void printBoard(){
            for(int row=0; row<9; row++){

                if(row%3==0 && row != 0) cout<< "-------+------+------\n";
                for(int col=0; col<9; col++){
                    
                    if(col%3==0 && col != 0) cout<< "| ";
                    cout<<getNum(row, col)<<" ";
                }
                cout<<endl;
            }
        }

        bool solve(){
            int row = -1, col = -1;
            bool emptyFound = false;

            for(int r=0; r<9 && !emptyFound; r++){
                for (int c=0; c<9 && !emptyFound; c++){
                    if(getNum(r,c) == 0){
                        row =r;
                        col =c;
                        emptyFound = true;
                    }
                }
            }

            if(!emptyFound) return true;

            for(int val=1; val <=9; val++){
                if(isValid(row, col, val)){
                    setNum(row, col, val);

                    if(solve()) return true;

                    setNum(row, col, 0);
                }
            }
            return false;
        };

        int getNum(int row, int col){
            return board[row*9 + col];
        }
        void setNum(int row, int col, int val){
            board[row*9 + col] = val;
        }
        bool isValid(int row, int col, int val){
            int idx = row * 9 + col;
            for (int peer : peers[idx]){
                if(board[peer] == val) return false;
            }
            return true;
        }

    private:
    void initPeers() {
        peers.resize(81);
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                int idx = row * 9 + col;
                // Add all cells in the same row
                for (int c = 0; c < 9; c++)
                    if (c != col) peers[idx].push_back(row * 9 + c);
                // Add all cells in the same col
                for (int r = 0; r < 9; r++)
                    if (r != row) peers[idx].push_back(r * 9 + col);
                // Add all cells in the same 3x3 box
                int boxRow = (row / 3) * 3;
                int boxCol = (col / 3) * 3;
                for (int r = 0; r < 3; r++) {
                    for (int c = 0; c < 3; c++) {
                        int peerIdx = (boxRow + r) * 9 + (boxCol + c);
                        if (peerIdx != idx &&
                            find(peers[idx].begin(), peers[idx].end(), peerIdx) == peers[idx].end()) {
                            peers[idx].push_back(peerIdx);
                        }
                    }
                }
            }
        }
    }
          
};



int main(){

     vector<int> puzzle = {
        5,3,0, 0,7,0, 0,0,0,
        6,0,0, 1,9,5, 0,0,0,
        0,9,8, 0,0,0, 0,6,0,
        8,0,0, 0,6,0, 0,0,3,
        4,0,0, 8,0,3, 0,0,1,
        7,0,0, 0,2,0, 0,0,6,
        0,6,0, 0,0,0, 2,8,0,
        0,0,0, 4,1,9, 0,0,5,
        0,0,0, 0,8,0, 0,7,9
    };

    SudokuSolver ss(puzzle);
    ss.printBoard();

    if (ss.solve()) {
        cout << "\nSolved Board:\n";
        ss.printBoard();
    } else {
        cout << "\nNo solution exists.\n";
    }
return 0;
}
