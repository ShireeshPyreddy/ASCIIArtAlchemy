from datetime import datetime
import random

"""
Notes: This is an 100 by 30 ASCII Art. Hence, maximize the terminal to the full screen to view it properly. 
"""


def generate_date_night_ascii_art():
    date_formats = ['%m/%d/%Y', '%d-%m-%Y', '%Y.%m.%d', '%B %d, %Y']
    date = datetime.now().strftime(random.choice(date_formats))
    time_formats = ['%I:%M %p', '%H:%M', '%I:%M:%S %p']
    time = datetime.now().strftime(random.choice(time_formats))
    grid_char = random.choice(['.', ' '])
    sand_char = '~'
    cloud_forms = ["    .-- \n  .-(   ) \n  (   .  ) \n (   (   )) \n  `- __.'  ",
                   "          .-~~~-.   \n  .- ~ ~-(       )_ _  \n /                     ~ -.\n |                          |  \n \                         .' \n  ~- . _____________ . -~",
                   "          .-~~~-.   \n  .- ~ ~-(       )_ _  \n /                     ~ -.\n |                          |  \n \                         .' \n  ~- ._ ,. ,.,.,., ,.. -~"]
    cloud = random.choice(cloud_forms)
    star_char = '+'

    red = '\033[31m'
    reset = '\033[0m'
    green = '\033[32m'
    brown = '\033[33m'
    blue = '\033[34m'
    dark_brown = '\033[90m'
    white = '\033[37m'
    pink = '\033[35m'

    heart = '♥'
    flower = '  *  \n * * \n* * *\n  |  '
    table_colors = [brown, blue, white]
    chair_colors = [dark_brown, white]

    # Randomly choose a table color from the list of table_colors.
    table_color = random.choice(table_colors)
    chair_color = random.choice(chair_colors)
    moon_char = ':'
    if grid_char == ".":
        moon_char = '#'
    moon = f'  _..._  \n .{moon_char * 5}. \n{moon_char * 7}: \n{moon_char * 7}: \n `{moon_char * 5}` \n   `{moon_char * 3}`   '
    tree = '     &&&     \n    &&&&&    \n   &&&&&&&   \n  &&&&&&&&&  \n &&&&&&&&&&& \n  &&&&&&&&&  \n   &&&&&&&   \n     |||     \n     |||     \n     |||     \n     |||     \n     |||     \n     |||     \n     |||     \n     |||     \n     |||     '
    small_tree = '   &&   \n  &&&&  \n &&&&&& \n   ||   \n   ||   \n   ||   \n   ||   '
    small_tree_prob = random.random()
    trees_colors = [green, white]
    tree_color = random.choice(trees_colors)
    flowers_colors = [pink, white]
    flower_color = random.choice(flowers_colors)

    # Randomizing the food items.
    food_items = [
        ['_______', '|pizza|', '|_____|'],
        ['  ___  ', ' |ham| ', ' |___| '],
        ['  ___  ', ' |pie| ', ' |___| '],
        ['  ____  ', ' |cake| ', ' |____| '],
    ]
    food_item = random.choice(food_items)
    wine_glass = '  __   \n |  |  \n |__|  \n  ||   '
    grid = [[grid_char for _ in range(100)] for _ in range(30)]
    for i in range(30 - 14, 30 - 6):
        grid[i][50:54] = [table_color + moon_char + reset] * 4
    moon_position = random.choice(['top_left', 'top_right'])

    for i in range(24, 30):
        for j in range(100):
            grid[i][j] = sand_char

    # Randomly choose a position for the cloud between column 30 and column 60.
    cloud_positions = []
    cloud_pos = random.randint(30, 60)
    # Add the cloud to the grid at the chosen position.
    for i, line in enumerate(cloud.split('\n')):
        for j, char in enumerate(line):
            grid[2 + i][cloud_pos + j] = char
            cloud_positions.append([2 + i, cloud_pos + j])

    # Loop through the first 8 rows of the grid.
    for i in range(8):
        # Loop through each column of the grid.
        for j in range(100):
            # Randomly choose a probability of changing the grid_char to star_char.
            prob = random.random()
            # If the probability is less than 0.01, change the grid_char to star_char.
            if prob < 0.01 and [i, j] not in cloud_positions:
                grid[i][j - 1] = " "
                grid[i][j] = star_char
                try:
                    grid[i][j + 1] = " "
                except IndexError:
                    pass

    if moon_position == 'top_left':
        for i, line in enumerate(moon.split('\n')):
            for j, char in enumerate(line):
                grid[i][j] = char
        date_with_dots = date + grid_char * 5
        for i, char in enumerate(date_with_dots):
            grid[1][-len(date_with_dots) + i] = char
        time_with_dots = time + grid_char * 5
        for i, char in enumerate(time_with_dots):
            grid[2][-len(time_with_dots) + i] = char
        for i, line in enumerate(tree.split('\n')):
            for j, char in enumerate(line):
                # If the char is not a space, add the green color to it.
                if char != ' ':
                    char = tree_color + char + reset
                grid[8 + i][85 + j] = char

        if small_tree_prob < 0.5:
            # Add the small tree to the grid at the chosen position.
            for i, line in enumerate(small_tree.split('\n')):
                for j, char in enumerate(line):
                    if char != ' ':
                        char = tree_color + char + reset
                    grid[17 + i][2 + j] = char
    else:
        for i, line in enumerate(moon.split('\n')):
            for j, char in enumerate(line):
                grid[i][-len(line) + j] = char
        date_with_dots = date + sand_char * 5
        for i, char in enumerate(date_with_dots):
            grid[-2][-len(date_with_dots) + i] = char
        time_with_dots = time + sand_char * 5
        for i, char in enumerate(time_with_dots):
            grid[-1][-len(time_with_dots) + i] = char
        for i, line in enumerate(tree.split('\n')):
            for j, char in enumerate(line):
                grid[8 + i][2 + j] = tree_color + char + reset

        # Randomly choose a number of flowers between 1 and 2.
        num_flowers = random.randint(1, 2)
        # Loop through the number of flowers.
        for k in range(num_flowers):
            # Choose a position for the flower at the right most of the grid
            flower_pos = 93 - k * 6
            # Add the flower to the grid at the chosen position with the pink color.
            for i, line in enumerate(flower.split('\n')):
                for j, char in enumerate(line):
                    if char != ' ':
                        char = flower_color + char + reset
                    grid[20 + i][flower_pos + j] = char

    # Add the table to the grid at the center position with the chosen color.
    table_positions = []
    for i in range(25):
        grid[15][40 + i] = table_color + '%' + reset
        table_positions.append([15, 40 + i])

    # Adding the randomized food item to the scene.
    food_positions = []
    for i, line in enumerate(food_item):
        for j, char in enumerate(line):
            grid[12 + i][49 + j] = char
            food_positions.append([12 + i, 49 + j])

    # Adding wine to the scene.
    wine_positions = []
    for i, line in enumerate(wine_glass.split('\n')):
        for j, char in enumerate(line):
            # If the char is not a space, add the red color to it.
            if char != ' ':
                char = red + char + reset
            grid[11 + i][42 + j] = char
            grid[11 + i][56 + j] = char
            wine_positions.append([11 + i, 42 + j])

    # Adding two "%" characters evenly spaced about 23% from the left end and 68% from the right end of the grid.
    left_percent_pos = int(len(grid[0]) * 0.23)
    right_percent_pos = int(len(grid[0]) * 0.68)

    # Adding the "%" characters to the specified row.
    for i in range(30 - 11, 30 - 6):
        grid[i][left_percent_pos:left_percent_pos + 4] = [chair_color + "%" + reset] * 4
        grid[i][left_percent_pos + 9:left_percent_pos + 13] = [chair_color + "%" + reset] * 4
        grid[i][left_percent_pos + 4: left_percent_pos + 9] = " " * 5
        grid[i][right_percent_pos:right_percent_pos + 4] = [chair_color + "%" + reset] * 4
        grid[i][right_percent_pos + 9:right_percent_pos + 13] = [chair_color + "%" + reset] * 4
        grid[i][right_percent_pos + 4: right_percent_pos + 9] = " " * 5

    # Adding 17 "%" characters to the top of the previously added "%" characters.
    for i in range(17):
        grid[30 - 12][left_percent_pos + i - 2] = chair_color + "%" + reset
        grid[30 - 12][right_percent_pos + i - 2] = chair_color + "%" + reset

    # Adding a male and a female sitting above the previously added 17 "%" characters.
    male = ['O     ', '|\\    ', '| \\__ ', '|     ', '|     ', '|     ', '|     ', '|--\\ ']
    female = ['    O~;', '   /| ;', '__/ |', '    |', '    |', '    |', '    |', ' /--|', "/"]

    # Place the modified code after the original code for adding the male and female to the grid.
    for i, line in enumerate(male):
        for j, char in enumerate(line):
            grid[30 - 20 + i][left_percent_pos + j + 12] = char
    for i, line in enumerate(female):
        for j, char in enumerate(line):
            grid[30 - 20 + i][right_percent_pos + j - 4] = char

    # Randomly choose a number of hearts between 3 and 5.
    num_hearts = random.randint(3, 5)
    # Loop through the number of hearts.
    for _ in range(num_hearts):
        # Randomly choose a position for the heart between row 10 and row 15, and column 15 and column 75.
        heart_row = random.randint(10, 15)
        heart_col = random.randint(15, 75)
        # Check if the chosen position overlaps with the male or the female.
        # If it does, choose another position until it doesn't.
        while grid[heart_row][heart_col] in male or grid[heart_row][heart_col] in female or \
                [heart_row, heart_col] in table_positions + wine_positions + food_positions:
            heart_row = random.randint(10, 15)
            heart_col = random.randint(15, 75)
        # Add the heart to the grid at the chosen position with the red color.
        grid[heart_row][heart_col] = red + heart + reset

    return '\n'.join([''.join(row) for row in grid])


print(generate_date_night_ascii_art())
