class State:
    def __init__(self, board, goal, moves=0):
        self.board = board
        self. goal = goal
        self.moves = moves

    #return new State swaping i1, i2
    def get_new_board(self, i1, i2, moves):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal, moves)

    #expand child node and return result list
    def expand(self, moves):
        result = []
        i = self.board.index(0)
        if not i in [0,1,2]:#up
            result.append(self.get_new_board(i, i-3 , moves))
        if not i in [0,3,6]:#left
            result.append(self.get_new_board(i, i-1, moves))
        if not i in [2,5,8]:#right
            result.append(self.get_new_board(i, i+1, moves))
        if not i in [6,7,8]:#down
            result.append(self.get_new_board(i, i+3, moves))
        return result

    #print board
    def __str__(self):
        return str(self.board[:3]) + "\n" + str(self.board[3:6]) + "\n" + str(self.board[6:9]) + "\n-------------------\n"
    
    def __eq__(self, other):
        return self.board == other.board

#initial state
puzzle = [1,2,3,
          4,0,5,
          7,8,6]

#destination
goal = [1,2,3,
        4,5,6,
        7,8,0]

#open list
open_queue = []
open_queue.append(State(puzzle, goal))

closed_queue = []
moves = 0

while len(open_queue) != 0:
    current = open_queue.pop(0) #pop()으로 바꾸면 stack -> dfs
    print(current)
    if current.board == goal:
        print("search succeded")
        break
    moves = current.moves + 1
    closed_queue.append(current)
    for state in current.expand(moves):
        if (state in closed_queue) or (state in open_queue):
            continue
        else:
            open_queue.append(state)
        
    
    
    

        