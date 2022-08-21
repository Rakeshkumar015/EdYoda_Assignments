# Assignment_5
# Create_Your_own_built-in_class_method
# Write_a_Python_class_to_implement_pow(x, n)

class Power:

    def pow(self,x,n):
        if x==0 or x==1 or n==1:
            return x
        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 0
        else:
            return x**n

# Creating_object
obj = Power()

# Taking_user_input
x = int(input("Enter x value: "))
n = int(input("Enter n value: "))

res = obj.pow(x,n)  # Storing_output_in_a_variable
print("pow(", x, ",", n,") =" ,res)