words = [el for el in input().split()]
palindrome_word = input()

palindrome_list = [el for el in words if el[::-1] == el]

print(palindrome_list)
print(f"Found palindrome {palindrome_list.count(palindrome_word)} times")
