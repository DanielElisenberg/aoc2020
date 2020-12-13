from collections import deque


def rotate_waypoint(x, y, angle):
    rotation = 360 + angle if angle < 0 else angle
    if rotation == 90:
        return (y, -x)
    elif rotation == 180:
        return (-x, -y)
    elif rotation == 270:
        return (-y, x)


def turn(current_direction, angle):
    directions = deque(['N', 'E', 'S', 'W'])
    directions.rotate(-directions.index(current_direction)-int(angle/90))
    return directions[0]


def move(direction, amount):
    if direction == 'E':
        return (amount, 0)
    if direction == 'W':
        return (-amount, 0)
    if direction == 'N':
        return (0, amount)
    if direction == 'S':
        return (0, -amount)


def move_ship_with_commands(commands):
    (x, y) = (0, 0)
    direction = 'E'
    for command in commands:
        instruction = command['instruction']
        parameter = command['parameter']
        if instruction in ['R', 'L']:
            rotation = -1 if instruction == 'L' else 1
            direction = turn(direction, rotation * parameter)

        else:
            move_direction = direction if instruction == 'F' else instruction
            (move_x, move_y) = move(move_direction, parameter)
            x += move_x
            y += move_y
    return abs(x) + abs(y)


def move_ship_with_waypoint(commands):
    (x, y) = (0, 0)
    (waypoint_x, waypoint_y) = (10, 1)
    for command in commands:
        instruction = command['instruction']
        parameter = command['parameter']
        if instruction in ['R', 'L']:
            rotation = -1 if instruction == 'L' else 1
            (waypoint_x, waypoint_y) = rotate_waypoint(
                waypoint_x, waypoint_y, rotation * parameter
            )
        elif instruction == 'F':
            (move_x, move_y) = (
                (waypoint_x*parameter, waypoint_y*parameter)
            )
            x += move_x
            y += move_y
        else:
            (move_x, move_y) = move(instruction, parameter)
            waypoint_x += move_x
            waypoint_y += move_y
    return abs(x) + abs(y)


with open('day12/input.data') as input:
    commands = [{"instruction": line[0], "parameter": int(line[1:])}
                for line in input.read().split('\n')]

print(f'first solution: {move_ship_with_commands(commands)}')
print(f'second solution: {move_ship_with_waypoint(commands)}')
