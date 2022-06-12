from time import time
from copy import deepcopy
from src.model import State
from src.constant import ColorConstant

class Bot13520131:
    def init(self) -> None:
        self.col_bonus = []
        self.col_bonus.append(0.5)
        self.col_bonus.append(0.6)
        self.col_bonus.append(0.7)
        self.col_bonus.append(1)
        self.col_bonus.append(0.7)
        self.col_bonus.append(0.6)
        self.col_bonus.append(0.5)

        self.col_points = [0] * 7

        self.emptyColor = ColorConstant.BLACK

    def find(self, state: State, player: int, thinking_time: float) -> int:
        """
        [DESC]
            Function to find the best move for player
        [PARAMS]
            state: State -> current state
            player: int -> player to find the best move
            thinking_time: float -> time limit for bot to find the best move
        [RETURN]
            int -> column to place piece
        """
        # Implement greedy algorithm here
        # ...

        #constants
        self.col_bonus = []
        self.col_bonus.append(0.5)
        self.col_bonus.append(0.6)
        self.col_bonus.append(0.7)
        self.col_bonus.append(1)
        self.col_bonus.append(0.7)
        self.col_bonus.append(0.6)
        self.col_bonus.append(0.5)

        self.emptyColor = ColorConstant.BLACK

        player_num = player
        enemy_player_num = (player + 1) % 2

        player_col = state.players[player_num].color
        enemy_col = state.players[enemy_player_num].color

        col_points = deepcopy(self.col_bonus)

        #check self 3
        self_verti_res = self.check_3_verti(state, player_col)
        if len(self_verti_res) > 0:
            for pos in self_verti_res:
                col_points[pos] = 9999

        self_hori_res = self.check_3_hori(state, player_col)
        if len(self_hori_res) > 0:
            for pos in self_hori_res:
                #checks left side of the horizontal 3 chain
                if (pos[1]-3 >= 0 and
                    state.board[pos[0], pos[1]-3].color == self.emptyColor and
                    ((pos[0]+1 < state.board.row and
                    state.board[pos[0]+1, pos[1]-3].color != self.emptyColor) or 
                    (pos[0] == state.board.row-1))):
                    col_points[pos[1]-3] = 9999

                #checks right side of the horizontal 3 chain
                if (pos[1]+1 < state.board.col and
                    state.board[pos[0], pos[1]+1].color == self.emptyColor and
                    ((pos[0]+1 < state.board.row and
                    state.board[pos[0]+1, pos[1]+1].color != self.emptyColor) or
                    (pos[0] == state.board.row-1))):
                    col_points[pos[1]+1] = 9999
        
        self_left_diag_res = self.check_3_left_diag(state, player_col)
        if len(self_left_diag_res) > 0:
            for pos in self_left_diag_res:
                #checks bottom most of diagonal
                if (pos[0]+3 < state.board.row and
                    pos[1]+3 < state.board.col and
                    state.board[pos[0]+3, pos[1]+3].color == self.emptyColor and
                    ((pos[0]+4 < state.board.row and 
                    state.board[pos[0]+4, pos[1]+3].color != self.emptyColor) or
                    (pos[0]+3 == state.board.row-1))):
                    col_points[pos[1]+3] = 9999

                #checks topmost of diagonal
                if (pos[0]-1 >= 0 and
                    pos[1]-1 >= 0 and
                    state.board[pos[0]-1, pos[1]-1].color == self.emptyColor and
                    state.board[pos[0], pos[1]-1].color != self.emptyColor):
                    col_points[pos[1]-1] = 9999

        self_right_diag_res = self.check_3_right_diag(state, player_col)
        if len(self_right_diag_res) > 0:
            for pos in self_right_diag_res:
                #checks bottommost of diagonal
                if (pos[0]+3 < state.board.row and
                    pos[1]-3 >= 0 and
                    state.board[pos[0]+3, pos[1]-3].color == self.emptyColor and
                    ((pos[0]+4 < state.board.row and
                    state.board[pos[0]+4, pos[1]-3].color == self.emptyColor) or
                    (pos[0]+3 == state.board.row-1))):
                    col_points[pos[1]-3] = 9999

                #checks topmost of diagonal
                if (pos[0]-1 >= 0 and
                    pos[1]+1 < state.board.col and
                    state.board[pos[0]-1, pos[1]+1].color == self.emptyColor and
                    state.board[pos[0], pos[1]+1].color != self.emptyColor):
                    col_points[pos[1]+1] = 9999
        enemy_verti_res = self.check_3_verti(state, enemy_col)
        if len(enemy_verti_res) > 0:
            for pos in enemy_verti_res:
                col_points[pos] = 999

        enemy_hori_res = self.check_3_hori(state, enemy_col)
        if len(enemy_hori_res) > 0:
            for pos in enemy_hori_res:
                #checks left side of the horizontal 3 chain
                if (pos[1]-3 >= 0 and
                    state.board[pos[0], pos[1]-3].color == self.emptyColor and
                    ((pos[0]+1 < state.board.row and
                    state.board[pos[0]+1, pos[1]-3].color != self.emptyColor) or 
                    (pos[0] == state.board.row-1))):
                    col_points[pos[1]] = 999

                #checks right side of the horizontal 3 chain
                if (pos[1]+1 < state.board.col and
                    state.board[pos[0], pos[1]+1].color == self.emptyColor and
                    ((pos[0]+1 < state.board.row and
                    state.board[pos[0]+1, pos[1]+1].color != self.emptyColor) or
                    (pos[0] == state.board.row-1))):
                    col_points[pos[1]] = 999
        
        enemy_left_diag_res = self.check_3_left_diag(state, enemy_col)
        if len(enemy_left_diag_res) > 0:
            for pos in enemy_left_diag_res:
                #checks bottom most of diagonal
                if (pos[0]+3 < state.board.row and
                    pos[1]+3 < state.board.col and
                    state.board[pos[0]+3, pos[1]+3].color == self.emptyColor and
                    ((pos[0]+4 < state.board.row and 
                    state.board[pos[0]+4, pos[1]+3].color != self.emptyColor) or
                    (pos[0]+3 == state.board.row-1))):
                    col_points[pos[1]+3] = 999

                #checks topmost of diagonal
                if (pos[0]-1 >= 0 and
                    pos[1]-1 >= 0 and
                    state.board[pos[0]-1, pos[1]-1].color == self.emptyColor and
                    state.board[pos[0], pos[1]-1].color != self.emptyColor):
                    col_points[pos[1]-1] = 999

        enemy_right_diag_res = self.check_3_right_diag(state, enemy_col)
        if len(enemy_right_diag_res) > 0:
            for pos in enemy_right_diag_res:
                #checks bottommost of diagonal
                if (pos[0]+3 < state.board.row and
                    pos[1]-3 >= 0 and
                    state.board[pos[0]+3, pos[1]-3].color == self.emptyColor and
                    ((pos[0]+4 < state.board.row and
                    state.board[pos[0]+4, pos[1]-3].color == self.emptyColor) or
                    (pos[0]+3 == state.board.row-1))):
                    col_points[pos[1]-3] = 999

                #checks topmost of diagonal
                if (pos[0]-1 >= 0 and
                    pos[1]+1 < state.board.col and
                    state.board[pos[0]-1, pos[1]+1].color == self.emptyColor and
                    state.board[pos[0], pos[1]+1].color != self.emptyColor):
                    col_points[pos[1]+1] = 999

        #checks for piece placement
        for i in range(0, state.board.col):
            col_points[i] += self.column_check(state, i, player_col)

        print(f"{col_points} and {col_points.index(max(col_points))}")

        #choose column with the highest point as the move
        return col_points.index(max(col_points))

    #returns list of columns that has pieces aligned 3
    #and the top piece isn't other color
    def check_3_verti(self, state: State, color):
        board = state.board
        result = []

        # Membuat "counter" simbol sedemikian rupa sehingga
        # proses perhitungan di-reset apabila terganggu oleh simbol lain
        # Apabila proses perhitungan mencapai tiga, maka
        # akan dilakukan counting point berdasarkan logic
        # yang berlaku
        counter = 0
        for i in range(board.col):
            '''
            the way the board is represented, the largest index is at bottom
            while the smallest index is at the top
            '''
            for j in range(board.row-1, -1, -1):
                if board[j, i].color == color:
                    counter += 1
                else:
                    counter = 0

                if counter == 3:
                    top_is_not_enemy = True
                    for k in range(j, -1, -1):
                        if board[k, i].color != color and board[k, i].color != self.emptyColor:
                            top_is_not_enemy = False
                            break
                    if top_is_not_enemy:
                        result.append(i)
                    counter = 0
                    break

        return result

    #returns list of int
    #where int is the location of the last pieces (both row and column in tuple) in the
    #pieces that connect 3 ( left to right )
    def check_3_hori(self, state: State, color):
        board = state.board
        result = []

        # Membuat "counter" simbol sedemikian rupa sehingga
        # proses perhitungan di-reset apabila terganggu oleh simbol lain
        # Apabila proses perhitungan mencapai tiga, maka
        # akan dilakukan counting point berdasarkan logic
        # yang berlaku
        counter = 0

        for i in range(board.row-1, -1, -1):
            for j in range(board.col):
                if board[i, j].color == color:
                    counter += 1
                else:
                    counter = 0

                if counter == 3:
                    result.append((i, j))
        return result

    #returns list of int
    #where int is the location of the last pieces (both row and column in tuple) in the
    #pieces that connect 3 ( top left of the diagonal )
    def check_3_left_diag(self, state: State, color):
        board = state.board
        #stores all pieces with the color color location in the form of tuple
        #first is row, second is column
        pieces_pos = []
        #this code is used to find location of all pieces
        for i in range(board.row-1, -1, -1):
            for j in range(board.col):
                if board[i, j].color == color:
                    pieces_pos.append((i, j))

        result = []
        for piece_pos in pieces_pos:
            if (piece_pos[0] - 3 >= 0 and
               piece_pos[1] - 3 >= 0 and
               board[piece_pos[0]-1, piece_pos[1]-1].color == color and
               board[piece_pos[0]-2, piece_pos[1]-2].color == color):
                result.append((piece_pos[0]-2, piece_pos[1]-2))

        return result

    #returns list of int
    #where int is the location of the last pieces (both row and column in tuple) in the
    #pieces that connect 3 ( top left of the diagonal )
    def check_3_right_diag(self, state: State, color):
        board = state.board
        #stores all pieces with the color color location in the form of tuple
        #first is row, second is column
        pieces_pos = []
        #this code is used to find location of all pieces
        for i in range(board.row-1, -1, -1):
            for j in range(board.col):
                if board[i, j].color == color:
                    pieces_pos.append((i, j))

        result = []
        for piece_pos in pieces_pos:
            if (piece_pos[0] - 3 >= 0 and
               piece_pos[1] + 3 < board.col and
               board[piece_pos[0]-1, piece_pos[1]+1].color == color and
               board[piece_pos[0]-2, piece_pos[1]+2].color == color):
                result.append((piece_pos[0]-2, piece_pos[1]+2))

        return result

    #this returns the index of row which hasn't been filled yet, at column col_num
    #returns -1 if column is full
    def get_unfilled_row_index(self, state: State, col_num: int):
        board = state.board
        for i in range(board.row-1, -1, -1):
            if board[i, col_num].color == self.emptyColor:
                return i
        return -1

    #checks column and then return total points accumulated for each column
    def column_check(self, state: State, col_num: int, color):
        board = state.board

        row_idx = self.get_unfilled_row_index(state, col_num)
        if row_idx == -1:
            return -99999
        total_point = 0

        #checks if placing piece at row_idx connects to other pieces at
        #all direction

        #checks piece connects to left

        if col_num-1 >= 0 and board[row_idx, col_num-1].color == color:
            total_point += 1
            if col_num-2 >= 0 and board[row_idx, col_num-2].color == color:
                total_point += 1

        #checks piece connects to right
        if col_num+1 < board.col and board[row_idx, col_num+1].color == color:
            total_point += 1
            if col_num+2 < board.col and board[row_idx, col_num+2].color == color:
                total_point += 1

        #checks piece connects to bottom
        if row_idx+1 < board.row and board[row_idx+1, col_num].color == color:
            total_point += 1
            if row_idx+2 < board.row and board[row_idx+2, col_num].color == color:
                total_point += 1

        #checks piece connects to left top diagonal
        if row_idx-1 >= 0 and col_num-1 >= 0 and board[row_idx-1, col_num-1].color == color:
            total_point += 1
            if row_idx-2 >= 0 and col_num-2 >= 0 and board[row_idx-2, col_num-2].color == color:
                total_point += 1

        #checks piece connect to right top diagonal
        if row_idx-1 >= 0 and col_num+1 < board.col and board[row_idx-1, col_num+1].color == color:
            total_point += 1
            if row_idx-2 >= 0 and col_num+2 < board.col and board[row_idx-2, col_num+2].color == color:
                total_point += 1

        #checks piece connect to left bottom diagonal
        if row_idx+1 < board.row and col_num-1 >= 0 and board[row_idx+1, col_num-1].color == color:
            total_point += 1
            if row_idx+2 < board.row and col_num-2 >= 0 and board[row_idx+2, col_num-2].color == color:
                total_point += 1

        #checks piece connect to right bottom diagonal
        if row_idx+1 < board.row and col_num+1 < board.col and board[row_idx+1, col_num+1].color == color:
            total_point += 1
            if row_idx+2 < board.row and col_num+2 < board.col and board[row_idx+2, col_num+2].color == color:
                total_point += 1
        
        return total_point