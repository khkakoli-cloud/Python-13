n = int(input("Please enter the total number of Rows :"))
print("Floyd's Traingle")
c = 1 # initialise the input as 1
for i in range(n):
    for j in range(i+1):
        print(c, end =" ")
        c = c + 1
    print()