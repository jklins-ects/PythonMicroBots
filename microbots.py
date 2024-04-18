from colorama import Fore, Style

class Cell:
    def __init__(self, color, val):
        self.color = color
        self.val = val
        self.row = None
        self.col = None

    def __str__(self):
        return f'{self.color}{self.val}{Style.RESET_ALL}'

def print_cell(cell):
    print(cell, end=' ')

def build_board(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            print_cell(board[row][col])
            #doing this to make life easier
            board[row][col].row = row
            board[row][col].col = col
        print()

def cells_have_common(cell1, cell2):
    return cell1.val == cell2.val or cell1.color == cell2.color

def find_possible_moves(t1, board):
    possible = []
    for i in range(len(board)):
        #checks downward
        if i != t1.row and cells_have_common(board[i][t1.col], t1):
            possible.append(board[i][t1.col])
        #checks across
    for j in range(len(board[t1.row])):
         if j != t1.col and cells_have_common(board[t1.row][j], t1):
            possible.append(board[t1.row][j])
    return possible

def find_shortest_path(t1, t2, board, visited = []):

    if t1 == t2:
        visited = visited + [t1]
        return visited 
    else:
        possible = find_possible_moves(t1, board)
        shortest = []
        checked = visited + [t1]
        for p in possible:
            if not p in checked:
                path = find_shortest_path(p, t2, board, checked)
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

    build_board(board)

    path = find_shortest_path(board[1][0],board[2][0], board)
    print()
    for c in path:
        print(str(c), end=" ")
    

if __name__ == "__main__":
    main()
