

secret_word = "Michael Scott"

guess= "" #must be predefined before overwritten

guess_count = 0
guess_limit = 3
out_of_guesses= False

while guess != secret_word and not(out_of_guesses):#!= is not equal to, not() when boolean is false
    if guess_count < guess_limit:
        guess = input("enter a word: ") # 
        guess_count = guess_count +1
    else:
        out_of_guesses= True



if  out_of_guesses:
    print("you loose")
else:
    print("you win")
    
    
    