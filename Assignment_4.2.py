# Assignment_4.2
# Find_the_way_with_Maps
# Program_to-triple_all_numbers_of_a_given_list_of_integers


#Taking_user_input_for_a_list
num1 = int(input("Enter the total number of elements in the list: "))
list1 = []
for i in range(num1):
    elmt1 = int(input("Enter element: "))
    list1.append(elmt1)
print("List: ",list1)

#Function_to_triple_the_elements_of_the_list
def triple(list1):
    return list1 * 3

result = list(map(triple,list1)) #Calling_the_function
print("New List: ",result)