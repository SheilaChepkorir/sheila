#Python code that checks whether a number is prime or not.
def prime_num(num):
    if num> 1:  
        for n in range(2,num):  
            if (num % n) == 0:  
                return False
        return True
    else:
        return False
print(prime_num(64))
print(prime_num(5))

#Python code that when you inputs a number the function you have created checks whether the number belongs to the Fibonacci sequence or not.

n=int(input("Enter the number: "))
value_one=0
value_two=1
value_three=1
if n==0 or n==1:
    print("Yes")
else:
    while value_one<n:
        value_one=value_two+value_three
        value_three=value_two
        value_two=value_one
    if value_one==n:
        print("Belongs to the fibonnaci sequence")    
    else:
        print("Doesn't belong to the fibonnaci sequence")