#Assignment_2.2
#Make_Your_Own_mini-Dictionary
#Python_program_to_print_a_dictionary_whose_keys_should_be_the_alphabet_
#from_a-z_and_the_value_should_be_corresponding_ASCII_values.

my_dict = {}    #creating_an_empty_dictionary

for i in range ( 97, 123 ):
    my_dict[chr(i)] = i    #assign_character_to_ASCII_value

print("My dictionry : ", my_dict)    #printing_my_dictionary