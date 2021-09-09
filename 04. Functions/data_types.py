# •	If the data type is int, multiply the number by 2.
# •	If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
# •	If the data type is string, surround the input with "$".
def data_type(type: str, action):
    result = 0

    if type == 'int':
        result = int(action) * 2
    elif type == 'real':
        result = (float(action) * 1.5)
    elif type == 'string':
        result = '$' + action + '$'
    return result


type_of_action = input()
action = input()

if type_of_action == 'real':
    print(f'{data_type(type_of_action, action):.2f}')
else:
    print(data_type(type_of_action, action))