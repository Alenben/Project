class even:

    def en(self, a):
        if a % 2 == 0:
            print("Number is even:", a)
        else:
            print("Number is odd:", a)


a = int(input("Enter a number:"))
obj = even()
obj.en(a)
