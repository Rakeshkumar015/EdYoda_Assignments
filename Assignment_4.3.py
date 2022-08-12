# Assignment_4.3
# Program_to_square_the_elements_of_a_list_using_map()_function.


#Taking_user_input_for_a_list
num1 = int(input("Enter the total number of elements in the list: "))
list1 = []
for i in range(num1):
    elmt = int(input("Enter element: "))
    list1.append(elmt)
print("List: ",list1)

#Function_to_square_the_elements_of_the_list
def square(list1):
    return list1 ** 2

result = list(map(square,list1)) #Calling_the_function
print("New List: ",result)