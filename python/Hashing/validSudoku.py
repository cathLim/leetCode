#https://leetcode.com/problems/valid-sudoku/submissions/
#Time complexity for HashMap : O(1)
#Time complexity for check duplicates: O(1)
#Total time complexity : O(9^2), 9*9 = size of grid 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #create a HashMap for columns
        cols = collections.defaultdict(set)
        #create a HashMap for rows
        rows = collections.defaultdict(set)
        #create a HashMap for nine (3*3) sub boxes of grid
        #where the key for this HashMap is r//3 and c//3
        squares = collections.defaultdict(set)

        #iterate over the entire grid of 9*9 dimension
        for r in range(9):
            for c in range(9):
                #check for empty position
                #in this case, the empty position represented by a dot '.'
                #if found, we skip it
                if board[r][c] == ".":
                    continue
                #check for duplicates
                if(board[r][c] in rows[r] 
                or board[r][c] in cols[c] 
                or board[r][c] in squares[(r//3, c//3)]):
                    return False

                #update our HashMap cols, rows and squares
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True