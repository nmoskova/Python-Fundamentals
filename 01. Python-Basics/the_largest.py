number = int(input())
number_as_string = str(number)

largest = sorted([i for i in number_as_string], reverse=True)

print(int("".join(largest)))