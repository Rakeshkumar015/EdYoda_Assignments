#Assignment1.2
#Program_that_accepts_a_word_from_the_user_and_reverse_it

word = str(input("eneter a word: "))    #User_have_to_input_a_word

for i in range(len(word)-1,-1,-1):
    print(word[i], end="")              #To_get_output_in_a_single_line