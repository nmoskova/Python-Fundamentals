def loading_bar(num: int):
    num = num // 10
    bar = '..........'
    for i in range(num):
        bar = bar.replace('.', '%', 1)
        return bar

number = int(input())
print(loading_bar(number))