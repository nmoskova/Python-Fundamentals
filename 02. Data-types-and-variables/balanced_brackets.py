num_lines_followed = int(input())
balanced = False
list_brackets = []

for each_line in range(1, num_lines_followed + 1):
    line = input()

    if line == '(' or line == ')':
        list_brackets += line
i = len(list_brackets)

if i % 2 == 0:
    for each in list_brackets[::2]:
        if each == '(':
            for closing_bracket in list_brackets[1::2]:
                if closing_bracket == ")":
                    balanced = True
if balanced:
    print('BALANCED')
else:
    print('UNBALANCED')


