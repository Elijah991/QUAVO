# loan_amount = 10,000,000
# Amount_paid_per_month = 1,000,000
# for r in range (11):
#   if Amount_paid_per_month == r:
#     print(loan_amount-Amount_paid_per_month)
# print(r)

# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#    print("{0} is Even".format(num))
# else:
#    print("{0} is Odd".format(num))


class book_shop:

    # constructor
    def __init__(self, title):
        self.title = title

    # Sample method
    def book(self):
        print('The tile of the book is', self.title)


b = book_shop('Sandman')
b.book()
# The tile of the book is Sandman