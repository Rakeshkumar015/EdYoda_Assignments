#Assignment1.3
#Counting_the_odd_and_even_numbers_from_a_series_of_numbers

even_num = 0    
odd_num = 0

for i in range(1,11):   #Range_of_numbers
    if i % 2 == 0:
        even_num += 1
    else:
        odd_num += 1

print("In the range of 1 to 10,")

print("even numbers are: ",even_num)    #Printing_count_of_even_numbers
print("odd numbers are: ",odd_num)     #Printing_count_of_odd_numbers