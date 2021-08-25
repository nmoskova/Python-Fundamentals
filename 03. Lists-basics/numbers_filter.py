n = int(input())
even = []
odd = []
positive = []
negative = []

for _ in range(n):
    number = int(input())
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)

    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

category = input()  # even, odd, positive, negative

if category == 'even':
    print(even)
elif category == 'odd':
    print(odd)
elif category == 'positive':
    print(positive)
elif category == 'negative':
    print(negative)