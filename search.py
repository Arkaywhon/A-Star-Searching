from queue import PriorityQueue


class WorldMap:

    def __init__(self):
        self.play_map = []
        self.name = None

    def is_populated(self):
        return len(self.play_map) > 0

    def read_from_file(self, file_name):
        self.play_map = []
        self.name = file_name

        with open(file_name, 'r') as file_reader:
            line = file_reader.readline()

            while line != '':
                self.play_map.append(line.rstrip())  # Remove tailing newline character, if one exists.
                line = file_reader.readline()

    def print(self):
        """
        Prints out the 2D map if it's populated.
        :return: Nothing
        """

        if not self.is_populated():
            return

        map_height = len(self.play_map)
        map_width = len(self.play_map[0])

        for i in range(0, map_height):
            for j in range(0, map_width):
                print(self.play_map[i][j], end='')
            print()

    def get_adjacent_options(self, reference_position):
        """
        Gets the positions adjacent to a reference position that can be moved to in the map.
        :param reference_position: The position from which adjacent movable positions will be located.
        :return: A list of (x, y) tuple positions adjacent to the reference position that can be moved to.
        """

        x, y = reference_position

        map_height = len(self.play_map)
        map_width = len(self.play_map[0])

        options = []

        # If the x and y coordinates are not within the map, return an empty list.
        if x < 0 or y < 0:
            return options
        elif x > map_width - 1 or y > map_height - 1:
            return options

        # Check if moving right is possible.
        if x < map_width - 1 and self.play_map[y][x + 1] != '0':
            options.append((x + 1, y))

        # Check if moving left is possible.
        if x > 0 and self.play_map[y][x - 1] != '0':
            options.append((x - 1, y))

        # Check if moving down is possible.
        if y < map_height - 1 and self.play_map[y + 1][x] != '0':
            options.append((x, y + 1))

        # Check if moving up is possible.
        if y > 0 and self.play_map[y - 1][x] != '0':
            options.append((x, y - 1))

        return options


def read_map_from_file(file_name):
    """
    Creates a 2D list map by reading a map from a text file.
    :param file_name: The name of the text file that the map is contained in.
    :return: A 2D list map representing the map that was in the text file.
    """
    map = []

    with open(file_name, 'r') as file_reader:
        line = file_reader.readline()

        while line != '':
            map.append(line.rstrip())  # Remove tailing newline character, if one exists.
            line = file_reader.readline()

    return map


def print_map(map):
    """
    Prints out a 2D list map.
    :param map: The map, represented as a 2D list.
    :return: void
    """

    map_height = len(map)
    map_width = len(map[0])

    for i in range(0, map_height):
        for j in range(0, map_width):
            print(map[i][j], end='')
        print()


def get_adjacent_options(current_position, map):
    """
    Gets a list of adjacent tile positions that can
    be traversed to from a specified position.
    :param x: The x coordinate from where adjacent positions are to be located.
    :param y: The y coordinate from where adjacent positions are to be located.
    :param map: The tile map.
    :return: A list of (x, y) tuple tile positions adjacent to the specified position.
    """

    x, y = current_position

    map_height = len(map)
    map_width = len(map[0])

    options = []

    # If the x and y coordinates are not within the map, return an empty list.
    if x < 0 or y < 0:
        return options
    elif x > map_width - 1 or y > map_height - 1:
        return options

    # Check if moving right is possible.
    if x < map_width - 1 and map[y][x + 1] != '0':
        options.append((x + 1, y))

    # Check if moving left is possible.
    if x > 0 and map[y][x - 1] != '0':
        options.append((x - 1, y))

    # Check if moving down is possible.
    if y < map_height - 1 and map[y + 1][x] != '0':
        options.append((x, y + 1))

    # Check if moving up is possible.
    if y > 0 and map[y - 1][x] != '0':
        options.append((x, y - 1))

    return options


def manhattan_distance(position_1, position_2):
    x1, y1 = position_1
    x2, y2 = position_2
    return abs(x1 - x2) + abs(y1 - y2)


def assemble_path(goal, previous):
    current_pos = goal
    path = [current_pos]

    while current_pos in previous:
        current_pos = previous[current_pos]
        path.append(current_pos)

    path.reverse()
    return path


def find_path(start, goal, map):

    tile_costs = {
        '1': 1,
        '2': 2
    }

    frontier = PriorityQueue()
    frontier.put((0, start))

    reached = {start: 0}
    previous = {}

    while frontier.queue:
        priority_value, position = frontier.get()
        path_cost = reached[position]

        if position == goal:
            return assemble_path(goal, previous)

        for adjacent_position in get_adjacent_options(position, map):

            adj_x, adj_y = adjacent_position
            tile = map[adj_y][adj_x]

            adjacent_path_cost = tile_costs[tile] + path_cost
            heuristic = manhattan_distance(adjacent_position, goal)
            priority = adjacent_path_cost + heuristic

            if (adjacent_position not in reached) or (adjacent_path_cost < reached[adjacent_position]):

                frontier.put((priority, adjacent_position))
                reached[adjacent_position] = adjacent_path_cost
                previous[adjacent_position] = position

    return []


def outline_map_path(map, path):
    """
    Outlines a map with a provided path.
    :param map: A 2D list representation of a map.
    :param path: A list of tuples, each of which are an x, y coordinate.
    :return: A copy of the provided map that has had its path outlined.
    """

    outlined_map = map.copy()

    # Mark the coord in the path with an '*' on the map.
    for x, y in path:
        row = outlined_map[y]  # row is of type string which is immutable.
        list_row = list(row)  # To get around the immutable string, it is converted to a list.
        list_row[x] = '*'  # The specific character at the coordinate can now be modified.
        outlined_map[y] = ''.join(list_row)  # The list is converted back to a string.

    return outlined_map


# ////////////////////////////////////////////////////////////////////////////////
# // Program execution. The following lines can be modified to suit your needs. //
# ////////////////////////////////////////////////////////////////////////////////

map = read_map_from_file('map01.txt')
print_map(map)
print()

start = (2, 2)
goal = (5, 7)

optimal_path = find_path(start, goal, map)

outlined_map = outline_map_path(map, optimal_path)
print_map(outlined_map)
print()


# //////////// Working with Classes ////////////

map1 = WorldMap()
map1.read_from_file('map01.txt')
map1.print()

reference_point = (2, 4)

print('Movable locations adjacent to {0} are: {1}'.format(reference_point, map1.get_adjacent_options(reference_point)))
