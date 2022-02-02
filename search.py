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


map = read_map_from_file('map01.txt')
print_map(map)
