class Cell:
    next_state = None

    def __init__(self, state='-'):
        self.state = state

    def evolve(self):
        if not self.next_state:
            return
        self.state = self.next_state
        self.next_state = None


def start(coords, runs):
    x_min = min([i[0] for i in coords])
    x_max = max([i[0] for i in coords])
    y_min = min([i[1] for i in coords])
    y_max = max([i[1] for i in coords])

    x_items = 10
    y_items = 10

    board = [[Cell() for _ in range(x_items)] for _ in range(y_items)]

    def get_neighbours(x, y):

        def get_neighbour(_x, _y):
            try:
                return board[_y][_x]
            except IndexError:
                return None

        n = []
        neighbour_positions = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x - 1, y + 1),
                               (x - 1, y - 1), (x + 1, y - 1)]
        for position in neighbour_positions:
            neighbour = get_neighbour(position[0], position[1])
            if position[0] >= 0 and position[1] >= 0 and neighbour:
                n.append(neighbour)
        return n

    def print_board():
        for _row in board[::-1]:
            print('  '.join([c.state for c in _row]))
        print('==========================================')

    for coord in coords:
        board[coord[1]][coord[0]].state = '*'

    print('INITIAL')
    print_board()

    for _ in range(runs):

        for y_idx, row in enumerate(board):
            for x_idx, cell in enumerate(row):
                neighbours = get_neighbours(x_idx, y_idx)
                live_neighbours = [n for n in neighbours if n.state == '*']

                if cell.state == '*' and len(live_neighbours) < 2:
                    cell.next_state = '-'
                if cell.state == '*' and (len(live_neighbours) == 2 or len(live_neighbours) == 3):
                    cell.next_state = '*'
                if cell.state == '*' and len(live_neighbours) > 3:
                    cell.next_state = '-'
                if cell.state == '-' and len(live_neighbours) == 3:
                    cell.next_state = '*'

        for row in board:
            for cell in row:
                cell.evolve()

        print_board()


start([(3, 3), (4, 3), (4, 2)], 10)
