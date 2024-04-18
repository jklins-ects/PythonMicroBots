from __future__ import annotations
from colorama import Fore, Style

class Cell:
    def __init__(self, color:str, val:int):
        self.color = color
        self.val = val
        self.row:int
        self.col:int

    def similar(self, other:Cell):
        """returns true if the val or color are the same"""
        return self.color == other.color or self.val == other.val
    
    def __str__(self):
        return f'{self.color}{self.val}{Style.RESET_ALL}'

def print_cell(cell:Cell):
    print(cell, end=' ')

def build_board(board:list):
    """prints the board to screen. Also, assigns row/col to each cell (this was a patch)"""
    for row in range(len(board)):
        for col in range(len(board[row])):
            print_cell(board[row][col])
            #doing this to make life easier
            board[row][col].row = row
            board[row][col].col = col
        print()


def find_possible_moves(t1:Cell, board:list):
    """checks for similar cells in the provided cells row and column"""
    possible = []
    for i in range(len(board)):
        #checks downward
        if i != t1.row and t1.similar(board[i][t1.col]):
            possible.append(board[i][t1.col])
        #checks across
    for j in range(len(board[t1.row])):
         if j != t1.col and t1.similar(board[t1.row][j]):
            possible.append(board[t1.row][j])
    return possible

def find_shortest_path(start:Cell, end:Cell, board:list, visited:list = []):
    """recursively searches for the shortest path to the end with the given start"""
    if start == end:
        visited = visited + [start]
        return visited 
    else:
        possible = find_possible_moves(start, board)
        shortest = []
        #create a different array that we can build on
        checked = visited + [start]
        for p in possible:
            if not p in checked:
                path = find_shortest_path(p, end, board, checked)
                #this makes sure the len of path is at least 1 (meaning we found the target)
                #without that, it's possible there are no moves because we already visited a cell
                #that is part of a shorter path. That would return a 0 length and would not work. 
                if len(shortest) == 0 or (len(path) < len(shortest) and len(path) > 0):
                    shortest = path
       
        return shortest


def main():
    board = [
        [Cell(Fore.MAGENTA, 5), Cell(Fore.MAGENTA, 2), Cell(Fore.MAGENTA, 3), Cell(Fore.YELLOW, 2), Cell(Fore.WHITE, 1), Cell(Fore.BLUE, 1)],
        [Cell(Fore.RED, 6), Cell(Fore.RED, 4), Cell(Fore.YELLOW, 3),Cell(Fore.WHITE, 2), Cell(Fore.GREEN, 2), Cell(Fore.RED, 2)],
        [Cell(Fore.BLUE, 4), Cell(Fore.GREEN, 5), Cell(Fore.GREEN, 3), Cell(Fore.MAGENTA, 4), Cell(Fore.GREEN, 6), Cell(Fore.WHITE, 4)],
        [Cell(Fore.WHITE, 6), Cell(Fore.BLUE, 6), Cell(Fore.BLUE, 2), Cell(Fore.MAGENTA, 6), Cell(Fore.YELLOW, 5), Cell(Fore.MAGENTA, 1)],
        [Cell(Fore.RED, 3), Cell(Fore.YELLOW, 4), Cell(Fore.WHITE, 3), Cell(Fore.RED, 1), Cell(Fore.BLUE, 5), Cell(Fore.YELLOW, 6)],
        [Cell(Fore.BLUE, 3), Cell(Fore.GREEN, 4), Cell(Fore.WHITE, 5), Cell(Fore.GREEN, 1), Cell(Fore.RED, 5), Cell(Fore.YELLOW, 1)],
    ]
    again = ""
    while again.lower() != "q":
        try:
            build_board(board)
            print("For entering the following coordinates, the rows/cols are 0 indexed")
            start = input("Enter start row,col -> ").split(",")
            end = input("Enter end row,col -> ").split(",")
            startCell = board[int(start[0])][int(start[1])]    
            endCell = board[int(end[0])][int(end[1])]
            print()
            print(f"Going from {startCell} to {endCell}")
            path = find_shortest_path(startCell,endCell , board)
            for c in path:
                print(str(c), end=" ")
            print()
        except:
            print("An error occurred. Make sure your input is in the form #,#")
        again = input("Enter q to quit or anything else to go again -> ")
    

if __name__ == "__main__":
    main()
