import random
hang= ['''
          0         |
        / | \       |
       /  |  \      |
          ''', '''
          0         |
        / | \       |
       /  |         |
          ''', '''
          0         |
        / | \       |
          |         |
          ''', '''
          0         |
        / |         |
          |         |
          ''', '''
          0         |
          |         |
          |         |
          ''', '''
          0         |
                    |
                    |
          ''','''
                    |
                    |
                    |
                    ''']
word_list= ["apple","banana","cherry","mango","strawberry","grapes"]
word= random.choice(word_list)
blank=[]
for w in word:
    blank.append("_")
print(blank)
choice= 6
while choice!=0:
    ran= input("Enter a letter: ")
    for i in range(len(word)):
        if(word[i]==ran):
            blank[i]=ran
    if ran not in word:
        choice=choice-1 
    print(blank)
    print("Lives left: ", choice)
    print(hang[choice])
    if '_' not in blank:
        print("You win!")
        choice=0
        break 
if(choice==0):
    print("Game Over!") 

        