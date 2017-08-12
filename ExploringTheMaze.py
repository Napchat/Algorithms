import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

class Maze:
    def __init__(self, maze_file_name):
        rows_in_maze = 0
        columns_in_maze = 0

        # Preparing for drawing the maze
        self.maze_list = []
        maze_file = open(maze_file_name, 'r')
        for line in maze_file:
            row_list = []
            col = 0
            for ch in line[:-1]:
                row_list.append(ch)
                if ch == 'S':
                    # The start point of our turtle
                    self.start_row = rows_in_maze
                    self.start_col = col
                col = col + 1
            rows_in_maze = rows_in_maze + 1
            self.maze_list.append(row_list)
            columns_in_maze = len(row_list)

        self.rows_in_maze = rows_in_maze
        self.columns_in_maze = columns_in_maze
        self.x_translate = -columns_in_maze / 2
        self.y_translate = rows_in_maze / 2
        self.t = turtle.Turtle(shape = 'turtle')
        self.wn = turtle.Screen()
        # 坐标原点在迷宫中心
        self.wn.setworldcoordinates(-(columns_in_maze - 1) / 2 - 0.5,
                                    -(rows_in_maze - 1) / 2 - 0.5,
                                    (columns_in_maze - 1) / 2 + 0.5,
                                    (rows_in_maze - 1) / 2 + 0.5)

    def draw_maze(self):
        self.t.speed(10)
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(x + self.x_translate,
                        - y + self.y_translate, 'tan')
        self.t.color('black')
        self.t.fillcolor('blue')

    def draw_centered_box(self, x, y, color):
        self.t.up()
        self.t.goto(x-0.5, y-0.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def move_turtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.x_translate,
            -y + self.y_translate))
        self.t.goto(x + self.x_translate, -y + self.y_translate)

    def drop_bread_crumb(self, color):
        self.t.dot(10, color)

    def update_position(self, row, col, val=None):
        if val:
            self.maze_list[row][col] = val
        self.move_turtle(col, row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'blue'
        else:
            color = None

        if color:
            self.drop_bread_crumb(color)

    def is_exit(self, row, col):
        return (row == 0 or
            row == self.rows_in_maze - 1 or
            col == 0 or
            col == self.columns_in_maze - 1)

    def __getitem__(self, idx):
        return self.maze_list[idx]

def search_from(maze, start_row, start_column):
    maze.update_position(start_row, start_column)

    # Base cases:
    # Run into an obstacle
    if maze[start_row][start_column] == OBSTACLE:
        return False
    # Found a square that has already been explored
    if (maze[start_row][start_column] == TRIED or
            maze[start_row][start_column] == DEAD_END):
        return False
    # Success
    if maze.is_exit(start_row, start_column):
        maze.update_position(start_row, start_column, PART_OF_PATH)
        print('Found the exit')
        return True
    maze.update_position(start_row, start_column, TRIED)

    # Otherwise, use logical short circuiting to try each
    # direction in turn
    found = (search_from(maze, start_row - 1, start_column) or
        search_from(maze, start_row + 1, start_column) or
        search_from(maze, start_row, start_column - 1) or
        search_from(maze, start_row, start_column + 1))
    if found:
        maze.update_position(start_row, start_column, PART_OF_PATH)
    else:
        maze.update_position(start_row, start_column, DEAD_END)
    return found

if __name__ == '__main__':
    my_maze = Maze('maze2.txt')
    my_maze.draw_maze()
    my_maze.update_position(my_maze.start_row, my_maze.start_col)

    search_from(my_maze, my_maze.start_row, my_maze.start_col)