electrons = int(input())
shell_position = 1
layers_list = []

while electrons > 0:
    electrons_in_layer = 2 * pow(shell_position, 2)

    if electrons_in_layer > electrons:
        layers_list.append(electrons)
        electrons = 0

    else:
        electrons -= electrons_in_layer
        layers_list.append(electrons_in_layer)

    shell_position += 1

print(layers_list)