import re


def common_answers(group):
    amount_of_people = len(group)
    combined_answers = ''.join(group)
    unique_answers = set(combined_answers)
    return [answer for answer in unique_answers
            if combined_answers.count(answer) == amount_of_people]


with open('day06/input.data') as input:
    groups = (
        [re.split('[ :\\n]', line) for line in input.read().split('\n\n')]
    )

unique_answers = [set(''.join(group)) for group in groups]
unique_answers_count = sum([len(answers) for answers in unique_answers])
print(f'first solution: {unique_answers_count}')

common_answers_count = sum([len(common_answers(group)) for group in groups])
print(f'second solution {common_answers_count}')
