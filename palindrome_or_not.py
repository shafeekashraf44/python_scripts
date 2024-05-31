string = input("Enter a word:")
palindrome_check = string[::-1]
print(palindrome_check)
if (string == palindrome_check):
    print(string,"is a palindrome")
else:
    print(string,"is not a palindrome")