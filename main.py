from  hangman_words import word

from hangman_arts import logo, stag

import random

stages = stag
print(logo)
display=[]

list= random.choice(word)

for letter in list:
       display+="_"   
counter=7
end_of_game=False
while not end_of_game:
   
        buchstabe=input("rate ein Buchstaben: ").lower()
    
        for position in range(len(list)):
             letter=list[position]
             if letter ==buchstabe:
                 display[position]=buchstabe
                
        print(display)      

        if buchstabe not in list:
                counter-=1
            
                print(stages[counter])
                if stages[counter]==stages[0]:
                  
                  end_of_game=True   
                  print(stages[0])
                  print("Game over")
            
            
        if "_"not  in display:
           end_of_game=True    
           print("gewonnen")

                #  print(new_postion)
                #  print(f"schadeee....{stages[new_postion]}")




            

