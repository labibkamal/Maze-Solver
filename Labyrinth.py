# Labib Kamal 300191346
# Trinity Bates 300129927
'''
maze = ['################','#ppppp#pps##pp##', 'pp###pppp###pp##', '#p###pp#p##ppp##', '#pppp##pp##ppp##', '####p###########', '###pp###########', '####ppppp#######', '########pp####pp', '########ppppppp#', '################']

def nested(lst):
    """Turns list of strings into nested list of strings

    Args:
        list (str): each row of maze

    Returns:
        list: nested list
    """
    nest = []
    for i in range(0, len(maze)):
        x = list(maze[i])
        nest.append(x)
    return nest

maze_mod = nested(maze)'''

def input_function():
    """Receives a list of strings and returns a nested list of strings as the maze.

    Returns:
        list: nested list
    """
    n = int(input('Enter desired rows for matrix: '))
    lst = []
    for i in range(0, n):
        x = input('Enter maze row: ')
        lst.append(x)
    
    print('Maze map complete.')
    nested = []
    for i in range(0, len(lst)):
        x = list(lst[i])
        nested.append(x)
    print('Maze (nested list) has been created.')
    
    return nested 

labyrinth = input_function()
    
def revert(maze):
    """
    Changes modified list of lists back into string lists.

    Args:
        maze (list): nested list

    Returns:
        list of strings
    """
    reverted = []
    for i in maze:
        x = ''
        for j in range(0, len(i)):
            x = x + i[j]
        reverted.append(x)
    return reverted

def printmaze(maze):
    for r in maze:
        for i in r:
            print(i, end = ' ')
        print('')

def find_p(maze):
    """Finds the entrance and exit of a maze matrix

    Args:
        maze (list): nested list

    Returns:
        start, end: start: start index end: end index
    """
    mat = maze.copy()
    column = len(maze[0])
    row = len(maze)

    for i in range(row): 
        for j in range(column):
            if j == 0: #first column
                if mat[i][j] == 'p':
                    entrance = i, j
            if j == column - 1: #last column
                if mat[i][j] == 'p':
                    out = i, j   
    return entrance, out

start, end = find_p(labyrinth)

def solve_maze(maze):
    dead_m = maze.copy()
    temp_m = maze.copy()
    row = len(maze) #row
    column = len(maze[0]) #column
    status = True
    while status:
        r = start[0] #starting point row
        c = start[1] #starting point column
        temp_m = dead_m.copy()
        while r < row and c < column:
            if r == end[0] and c == end[1]:
                temp_m[r][c] = '>'
                status = False
                #print('Maze solved')
                return temp_m
            #deadend
            if (temp_m[r-1][c] != 'p') and (temp_m[r][c+1] != 'p') and (temp_m[r+1][c] != 'p'):
                dead_m[r][c] = '!'
                #print('DEADEND!')
                temp_m = dead_m.copy()
                #print(printmaze(revert(dead_m)))
                break
            #movement
            if temp_m[r+1][c] == 'p': #down
                temp_m[r][c] = 'v'
                r = r + 1
                continue
            elif temp_m[r][c+1] == 'p': #forward
                temp_m[r][c] = '>'
                c = c + 1
                continue
            elif temp_m[r-1][c] == 'p': #up
                temp_m[r][c] = '^'
                r = r - 1
                continue
                                    
solution = solve_maze(labyrinth)
#solve_maze(maze_mod)

def deadends_no_more(solution):
    """Replaces all '!' in the solution with 'p'. Also gets length of the path found

    Args:
        solution (list): nested list

    Returns:
        list: 'nested list', int: length of path
    """
    path_length = 0
    for r in range(0, len(solution)):
        for c in range(0, len(solution[0])):
            if (solution[r][c] == '>') or (solution[r][c] == '^') or (solution[r][c] == 'v'):
                path_length += 1
            if solution[r][c] == '!':
                solution[r][c] = 'p'
    return solution, path_length

final_maze, min_path = deadends_no_more(solution)

printmaze(revert(final_maze)) #printing final_maze as a list of strings
print('The length of the minimum path =', min_path)