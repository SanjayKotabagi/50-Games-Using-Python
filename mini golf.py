import random

# Define the size of the mini-golf course
course_width = 10
course_length = 10

# Create a function to initialize the course with obstacles and a hole
def create_course():
    course = [[' ' for _ in range(course_width)] for _ in range(course_length)]
    
    # Place the hole at a random location
    hole_x = random.randint(1, course_width - 2)
    hole_y = random.randint(1, course_length - 2)
    course[hole_y][hole_x] = 'H'
    
    # Place some obstacles
    num_obstacles = random.randint(5, 10)
    for _ in range(num_obstacles):
        obs_x = random.randint(1, course_width - 2)
        obs_y = random.randint(1, course_length - 2)
        course[obs_y][obs_x] = 'X'
    
    return course

# Create the mini-golf course
course = create_course()

# Function to display the course
def display_course(course):
    for row in course:
        print(' '.join(row))
    print()

# Display the initial course
display_course(course)

# Game loop
while True:
    # Get user input for the direction of the shot
    direction = input("Enter shot direction (up/down/left/right): ").lower()
    
    # Calculate the new ball position based on the input
    ball_x, ball_y = 0, 0
    if direction == "up" and ball_y > 0:
        ball_y -= 1
    elif direction == "down" and ball_y < course_length - 1:
        ball_y += 1
    elif direction == "left" and ball_x > 0:
        ball_x -= 1
    elif direction == "right" and ball_x < course_width - 1:
        ball_x += 1
    
    # Check if the ball reached the hole or hit an obstacle
    if course[ball_y][ball_x] == 'H':
        print("Congratulations! You made it to the hole!")
        break
    elif course[ball_y][ball_x] == 'X':
        print("Oops! You hit an obstacle. Game over!")
        break
    
    # Update the course with the new ball position
    course[ball_y][ball_x] = 'O'
    
    # Display the updated course
    display_course(course)
