import random 
 
def secret_santa(): 
    list_1 = ["Amira","1", "Chad","2", "Mariah","3","Yasmin","4"]

    giftee_options = dict()
    for i in range(0,len(list_1),2):
      giftee_options.update({list_1[i]: list_1[i+1]})

    same = {"Same":0} 
    different = {"Different":0}

   
    choose_again = 'yes' 

    #rules
    while choose_again == 'yes':
        print('Welcome to Secret Santa !') 
        print('You are Santa. You have guess who the elves want you to gift')
        print('Insert a number representing the person you believe should get a present this year')
        print('Your elves will tell you if they believe if its a good idea')
        print('If the elves have a different choice than you then you have to gift the elves choice instead')
        print('Please input the correct number according')
        print('Who Are You Picking?') 

        elf_choice = get_elf_choice() 
        santa_choice = get_santa_choice()

        if elf_choice == santa_choice:
          same["Same"] += 1
        else:
          different["Different"] += 1


        print('You chose', santa_choice, '.')
        print('Elves chose', elf_choice, '.') 
         

        
        print(giftee_result(elf_choice, santa_choice))

        
        choose_again = input("Would You Like to Guess Again?Enter yes or no ") 

    
    print('Your total correct choices', same, '.') 
    print('Your total wrong choices', different, '.')

def get_elf_choice(): 
    
    choice = random.randint(1,3) 

    
    if choice == 1: 
        choice = 'Amira' 
    elif choice == 2: 
        choice = 'Chad' 
    elif choice == 3:
        choice = 'Mariah' 
    else:
        choice = 'Yasmin'

     
    return choice 

 
def get_santa_choice(): 
     
    choice = int(input("Select Picker Amira(1), Chad(2), Mariah(3), Yasmin(4): ")) 

    
    while choice != 1 and choice != 2 and choice != 3 and choice != 4: 
        print('These people are valid Amira(type in 1), Chad(type in 2),Mariah(type in 3') 
        print('or Yasmin(type in 4).') 
        choice = int(input('Enter a valid number please: ')) 

     
    if choice == 1: 
        choice = 'Amira' 
    elif choice == 2: 
        choice = 'Chad' 
    elif choice == 3:
        choice = 'Mariah'
    else: 
        choice = 'Yasmin' 

    
    return choice 

 
def giftee_result(elf_choice, santa_choice): 
   
    if elf_choice == santa_choice:
        result = 'same'
        return("You Get To Keep Your Giftee!")
    else: 
        result = 'different'
        return ("The eleves went a different direction :/ ")
         
secret_santa()
