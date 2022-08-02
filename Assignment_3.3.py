#Assignment_3.3
#Calculate_the_Upper_and_the_lower_Case
# calculate_the_number_of_upper_case_letters_and_lower_case_letters.

def up_low():
    upper_values = 0    
    lower_values = 0
    for i in str1:
        if i.isupper():
            upper_values+=1
        elif i.islower:
            lower_values+=1

    print(f"upper_value: {upper_values}")
    print(f"lower_value: {lower_values}")

str1=input("Enter a string: ")      #String_enter_by_user

up_low()     #Calling_the_function