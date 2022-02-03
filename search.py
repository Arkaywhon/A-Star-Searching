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


def get_adjacent_options(x, y, map):
    """
    Gets a list of adjacent tile positions that can
    be traversed to from a specified position.
    :param x: The x coordinate from where adjacent positions are to be located.
    :param y: The y coordinate from where adjacent positions are to be located.
    :param map: The tile map.
    :return: A list of (x, y) tuple tile positions adjacent to the specified position.
    """

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


map = read_map_from_file('map01.txt')
print_map(map)
print(get_adjacent_options(5, 2, map))