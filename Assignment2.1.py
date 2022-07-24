#Assignment_2.1
#Fun_with_Lists_and_Tuples
#Python_program_to_get_a_list,_sorted_in_increasing_order_
#by_the_last_element_in_each_tuple_from_a_given_list_of_non-empty_tuples.

#Creating_a_list_of_tuple
number = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1), (4, 7), (3, 6)]
print("list of tuple before sorting: ", number)     #printing_the_list_before_sorting

#Sorting list of tuples in Increasing order by last element   
for i in range( len(number) ): 
    for j in range( i, len(number) ):
        if number [i][1] > number [j][1]:       
            number [i], number [j] = number [j], number [i]

print("list of tuple after sorting:  ", number)     #printing_the_list_after_sorting
