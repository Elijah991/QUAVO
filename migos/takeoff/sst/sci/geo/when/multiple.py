# def multiplication_table (num):
#   print("multiplication_table of", num)
#   for t in range(1,10):
#     print(num, "x", t, "=",num*t )
  
# multiplication_table(4)

def is_palindrome (string):
  reversed_string = string[::-1]
  for r in range(reversed_string):
    return True
  else:
    return False
  
is_palindrome("madam")
