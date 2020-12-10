def jolt_differences(numbers):
    jolt_diff_of = {1: 0, 3: 0}
    for i in range(len(numbers)-1):
        diff = numbers[i+1] - numbers[i]
        jolt_diff_of[diff] += 1
    return jolt_diff_of[1] * jolt_diff_of[3]


def possible_arrangments(next_for):
    amount_map = {adapter: 0 for adapter in next_for.keys()}
    amount_map[0] = 1
    amount_map[max(next_for.keys())+1] = 0

    while sum(amount_map.values()) > amount_map[99]:
        for adapter in amount_map.keys():
            if adapter != 99 and amount_map[adapter] > 0:
                for next_adapter in next_for[adapter]:
                    amount_map[next_adapter] += amount_map[adapter]
                amount_map[adapter] -= amount_map[adapter]
    return amount_map[max(next_for.keys())+1]


def next_for_map(numbers):
    next_for = {}
    for i in range(0, len(numbers)-1):
        possible_next = []
        for j in range(i+1, len(numbers)):
            if numbers[j] - numbers[i] > 3:
                break
            if numbers[j] - numbers[i] <= 3:
                possible_next.append(j)
        next_for[i] = possible_next
    return next_for


with open('day10/input.data') as input:
    numbers = [int(line) for line in input.read().split('\n')]

numbers.sort()
numbers = [0] + numbers
numbers.append(numbers[-1]+3)

print(f'first solution: {jolt_differences(numbers)}')
next_for = next_for_map(numbers)
print(f'second solution: {possible_arrangments(next_for)}')
