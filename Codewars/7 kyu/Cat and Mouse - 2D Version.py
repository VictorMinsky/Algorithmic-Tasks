"""
You will be given a string (map) featuring a cat "C" and a mouse "m". The rest of the string will be made up of dots (".") The cat can move the given number of moves up, down, left or right, but not diagonally.

You need to find out if the cat can catch the mouse from it's current position and return "Caught!" or "Escaped!" respectively.

Finally, if one of two animals are not present, return "boring without two animals".

Examples
moves = 5

map =
..C......
.........
....m....

returns "Caught!" because the cat can catch the mouse in 4 moves
moves = 5

map =
.C.......
.........
......m..

returns "Escaped!" because the cat cannot catch the mouse in  5 moves
"""



def cat_mouse(map_, moves):
    paths = map_.split()
    if 'C' not in map_ or 'm' not in map_:
        return "boring without two animals"
    cat_pos, mouse_pos = [0, 0], [0, 0]
    for index, way in enumerate(paths):
        if 'C' in way:
            cat_pos[0] = index
            cat_pos[1] = way.index('C')
        if 'm' in way:
            mouse_pos[0] = index
            mouse_pos[1] = way.index('m')
    return "Caught!" if abs(cat_pos[0] - mouse_pos[0]) + abs(cat_pos[1] - mouse_pos[1]) <= moves else "Escaped!"
