#vallidate input:
#keep asking the user for in2
# put until they enter a number between 1 to 10

while True:
     number = int(input("enter value b/w 1 and 10 :"))
     if 1 <= number <= 10:
         print("thanks")
         break
     else:
         print("invalid no.,try again")
         
         