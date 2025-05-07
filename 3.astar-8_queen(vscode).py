import heapq

def calculate_heuristic(board):
    attacking_pairs = 0
    n = len(board)
    
    # Check for attacking pairs
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                attacking_pairs += 1
    return attacking_pairs

def print_board(board):
    n = len(board)
    # Print the current state of the board
    for row in range(n):
        board_row = ['Q' if col == board[row] else '.' for col in range(n)]
        print(' '.join(board_row))
    print()

def a_star(start_board):
    n = 8
    open_list = []
    heapq.heappush(open_list, (0 + calculate_heuristic(start_board), 0, start_board))
    closed_list = set()
    
    step_count = 0  # To track number of steps taken

    while open_list:
        f, g, board = heapq.heappop(open_list)
        step_count += 1

        if calculate_heuristic(board) == 0:
            print("✅ Solution Found!")
            print_board(board)
            print(f"Total steps taken: {step_count}")
            return board

        for i in range(n):
            for j in range(n):
                if board[i] != j:
                    new_board = board[:]
                    new_board[i] = j

                    if tuple(new_board) not in closed_list:
                        closed_list.add(tuple(new_board))

                        print(f"Placing queen at row {i}, column {j} (step: {g + 1}):")
                        print_board(new_board)

                        heapq.heappush(open_list, (g + 1 + calculate_heuristic(new_board), g + 1, new_board))

    print("❌ No solution found.")
    return None

def get_user_input():
    print("Please enter the initial state for the 8 queens (values between 0 and 7 for each row).")
    print("For example, a valid input could be: [0, 1, 2, 3, 4, 5, 6, 7]")
    while True:
        try:
            user_input = input("Enter the initial state (a list of 8 integers from 0 to 7): ")
            initial_state = list(map(int, user_input.strip('[]').split(',')))

            if len(initial_state) == 8 and all(0 <= x < 8 for x in initial_state):
                print(f"Initial state: {initial_state}")
                return initial_state
            else:
                print("Invalid input. Please enter a list of 8 integers, each between 0 and 7.")
        except ValueError:
            print("Invalid input. Please enter a valid list of integers.")

# Get the initial state from the user
initial_state = get_user_input()

# Run the A* algorithm and display each step
a_star(initial_state)
