import copy 
initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
] 
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# for row in initial_state:
#     print(row)


#find initial position of 0 
def findInitialPos(initial_state):
    for row in range(3):
        for col in range(3):
            if(initial_state[row][col]==0):
                return row , col 



# up movement 
def move_up(initial_state,row , col):
    new_row = row -1 
    new_col = col 
    up_state = copy.deepcopy(initial_state)
    if(new_row >=0):
        up_state[row][col] , up_state[new_row][new_col] = up_state[new_row][new_col] , up_state[row][col] ;
    return up_state ;

#down movement
def move_down(initial_state,row , col):
    new_row = row +1 
    new_col = col 
    down_state = copy.deepcopy(initial_state)
    if(new_row <=2):
        down_state[row][col] , down_state[new_row][new_col] = down_state[new_row][new_col] , down_state[row][col] ;
    return down_state ;

#left movement 
def move_left(initial_state,row , col):
    new_row = row  
    new_col = col -1
    left_state = copy.deepcopy(initial_state)
    if(new_col >=0):
        left_state[row][col] , left_state[new_row][new_col] = left_state[new_row][new_col] , left_state[row][col] ;
    return left_state ;

def move_right(initial_state,row , col):
    new_row = row  
    new_col = col+1
    right_state = copy.deepcopy(initial_state)
    if(new_col <=2):
        right_state[row][col] , right_state[new_row][new_col] = right_state[new_row][new_col] , right_state[row][col] ;
    return right_state ;


def generate_children(state):
    [row , col]= findInitialPos(state) 
    children = []
    if row>0:
        children.append(move_up(state , row ,col))
    if row < 2 :
        children.append(move_down(state , row ,col))
    if col>0 :
        children.append(move_left(state , row ,col))
    if col<2: 
        children.append(move_right(state , row ,col))
    return children 

def state_to_tuple(state):
    return tuple(tuple(row) for row in state)
stack = []
visited = set()

stack.append(initial_state)

while stack:

    current = stack.pop()

    key = state_to_tuple(current)

    if key in visited:
        continue

    visited.add(key)

    if current == goal_state:
        print("Goal Found")
        break

    children = generate_children(current)

    for child in children:
        stack.append(child)