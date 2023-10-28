def evaluate(board):
    for player in ['X', 'O']: 
        if (board[0] == board[1] == board[2] == player or
            board[3] == board[4] == board[5] == player or
            board[6] == board[7] == board[8] == player or
            board[0] == board[3] == board[6] == player or
            board[1] == board[4] == board[7] == player or
            board[2] == board[5] == board[8] == player or
            board[0] == board[4] == board[8] == player or
            board[2] == board[4] == board[6] == player):
            if player == 'X':
                return 1  
            else:
                return -1 
    if ' ' not in board:
        return 0  
    return None  

#đgia và tính điểm tối ưu
def minimax(board, depth, is_maximizing):
    result = evaluate(board)
    if result is not None:
        return result
    
    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, False) #O
                board[i] = ' '  
                best_score = max(score, best_score)  
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, True) 
                board[i] = ' '  
                best_score = min(score, best_score)
        return best_score


def find_best_move(board):
    best_move = -1 #lưu trữ bước đi tối ưu đã tìm 
    best_score = -float('inf') 
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X' 
            score = minimax(board, 0, False)# X,O  
            board[i] = ' '  
            if score > best_score:
                best_score = score 
                best_move = i
    return best_move 

# Hàm main để chơi trò chơi
def main():
    board = [' '] * 9
    while True:
        print_board(board)
        if ' ' not in board or evaluate(board) is not None:
            break
        player_move = int(input("Chọn một ô (0-8): "))
        if board[player_move] != ' ':
            print("Ô đã được chọn. Hãy chọn lại.")
            continue
        board[player_move] = 'O'  # Cập nhật bảng sau nước đi của người chơi
        print_board(board)
        if ' ' not in board or evaluate(board) is not None:
            break
        print("Đang đến lượt máy tính...")
        computer_move = find_best_move(board)  
        board[computer_move] = 'X'  
    
    print_board(board)
    result = evaluate(board)
    if result == 1:
        print("Máy tính đã thắng!")
    elif result == -1:
        print("Bạn đã thắng!")
    else:
        print("Hòa!")

def print_board(board):
    for i in range(0, 9, 3): #bd0, end 9, cách 3
        print(board[i], '|', board[i + 1], '|', board[i + 2])
        if i < 6:
            print("---------")

if __name__ == "__main__":
    main()