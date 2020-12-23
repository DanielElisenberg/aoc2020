from collections import deque


def pick_destination_cup(circle, current_cup):
    current_cup_value = circle[0]
    min_cup = min(circle)
    max_cup = max(circle)
    destination_cup = None

    while destination_cup is None:
        current_cup_value -= 1
        if current_cup_value in circle:
            destination_cup = circle.index(current_cup_value)
        if current_cup_value < min_cup:
            current_cup_value = max_cup + 1
    return destination_cup


def pick_up(circle):
    circle.rotate(-1)
    picked_up = [
        circle.popleft(),
        circle.popleft(),
        circle.popleft()
    ]
    circle.rotate(1)
    return picked_up


def place_cups(circle, picked_up, destination_cup):
    circle.rotate(-destination_cup-1)
    for cup in picked_up:
        circle.append(cup)
    circle.rotate(destination_cup+4)


def hundred_rounds(circle):
    for _ in range(100):
        current_cup = 0
        picked_up = pick_up(circle)
        destination_cup = pick_destination_cup(circle, current_cup)
        place_cups(circle, picked_up, destination_cup)
        circle.rotate(-1)

    circle.rotate(-circle.index(1))
    return ''.join([str(ch) for ch in circle if ch != 1])


def run_moves(circle, times):
    for i in range(times):
        print(i)
        current_cup = 0
        picked_up = pick_up(circle)
        destination_cup = pick_destination_cup(circle, current_cup)
        place_cups(circle, picked_up, destination_cup)
        circle.rotate(-1)

    circle.rotate(-circle.index(1))
    return ''.join([str(ch) for ch in circle if ch != 1])


def ten_million_moves(circle):
    max_cup = max(circle) + 1
    while len(circle) < 1000000:
        circle.append(max_cup)
        max_cup += 1
    run_moves(circle, 10000000)
    return circle[1] * circle[2]


input = '583976241'
circle = deque([int(ch) for ch in input])
print(f'first solution: {run_moves(circle, 100)}')
circle = deque([int(ch) for ch in input])
print(f'second solution: {ten_million_moves(circle)}')
