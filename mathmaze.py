import random

def generate_math_problem():
    """Generates a random math problem."""
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(["+", "-", "*"])
    
    if operation == "+":
        question = f"{num1} + {num2}"
        answer = num1 + num2
    elif operation == "-":
        question = f"{num1} - {num2}"
        answer = num1 - num2
    elif operation == "*":
        question = f"{num1} * {num2}"
        answer = num1 * num2
    
    return question, answer

def display_maze(maze, player_pos):
    """Displays the maze with the player's position."""
    for i, row in enumerate(maze):
        row_str = ""
        for j, cell in enumerate(row):
            if (i, j) == player_pos:
                row_str += "P "  # Player's position
            else:
                row_str += f"{cell} "
        print(row_str)
    print()

def math_maze():
    """Main function for the Math Maze game."""
    # Define a 3x3 maze
    maze = [["S", "1", "2"],
            ["3", "4", "5"],
            ["6", "7", "E"]]
    
    # Starting position
    player_pos = (0, 0)  # Top-left corner (row 0, col 0)
    
    print("Welcome to Math Maze!")
    print("Solve math problems to move through the maze.")
    print("Reach 'E' to win!\n")
    
    while True:
        display_maze(maze, player_pos)
        
        # Check if the player has reached the end
        if player_pos == (2, 2):
            print("🎉 Congratulations! You completed the Math Maze! 🎉")
            break
        
        # Ask the player for their move
        print("Move options: (W) Up, (S) Down, (A) Left, (D) Right")
        move = input("Enter your move: ").strip().upper()
        
        # Calculate the new position
        row, col = player_pos
        if move == "W" and row > 0:
            new_pos = (row - 1, col)
        elif move == "S" and row < 2:
            new_pos = (row + 1, col)
        elif move == "A" and col > 0:
            new_pos = (row, col - 1)
        elif move == "D" and col < 2:
            new_pos = (row, col + 1)
        else:
            print("Invalid move. Try again!")
            continue
        
        # Generate a math problem to solve
        question, answer = generate_math_problem()
        print(f"Solve this problem to move: {question}")
        user_answer = input("Your answer: ").strip()
        
        # Check the answer
        if user_answer.isdigit() and int(user_answer) == answer:
            print("✅ Correct! You moved.")
            player_pos = new_pos  # Update the player's position
        else:
            print("❌ Wrong answer. Stay in place!")
        print()

# Run the game
math_maze()
