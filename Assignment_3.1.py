#Assignment_3.1
#Game_of_functions
#Sum_all_the_numbers_in_a_list

def Sum_list(): #Defining_the_Function
    sum =  0
    for i in list1:    #Using_For_loop_for_Addition
        if len(list1)<= 1:
            print("Please enter more numbers")
        else:
            sum += i
    print(f"Sum of numbers: {sum}")     #Printing_the_Sum_value


list1 = []      #Creating_an_empty_list
num1 = int(input("How many numbers: ")) #How_many_numbers_user_have_to_input
for n in range(num1):
    num2 = int(input("Enter number: ")) #Values_enter_by_user
    list1.append(num2)  #Assigning_the_values_to_the_list
print(f"List is: {list1}")    #printing_the_list

Sum_list()      #Calling_the_Function

