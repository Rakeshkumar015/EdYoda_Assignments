# Assignment_4.1
# Play_with_Lambda
# Program_to_create_a_lambda_function_that_adds_25_to_a_given_number_passed_in_as_an_argument.


#Function_to_add_any_given_number_with_25
def add(x):
    return lambda num1 :  x + num1  #Lambda

num1 = int(input("Enter any number : ")) #User_input

result = add(25)  #Calling_the_function
print("Result: ",result(num1))