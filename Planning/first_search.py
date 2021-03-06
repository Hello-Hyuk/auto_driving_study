# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
# 
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left, 
# up, and down motions. Note that the 'v' should be 
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    
    # ' ' -> -1 로 변경하여 해결
    # TypeError: list indices must be integers or slices, not str
    index = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    

    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            index[x2][y2] = i
                            
    for i in range(len(grid)):
        print(index[i])
        
    # path는 goal 지점부터 시작지점으로 mark
    cur_x, cur_y = goal
    path_mark = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    path_mark[cur_x][cur_y] = '*'

    print('\nPath Mark')
    
    while cur_x != init[0] or cur_y != init[1]:
        past_x = cur_x - delta[index[cur_x][cur_y]][0]
        past_y = cur_y - delta[index[cur_x][cur_y]][1]
        
        path_mark[past_x][past_y] = delta_name[index[past_x][past_y]]
        
        cur_x = past_x
        cur_y = past_y
        
    return path_mark # make sure you return the shortest path

if __name__ == '__main__':
    result = search(grid,init,goal,cost)
    for i in range(len(result)):
        print(result[i])
