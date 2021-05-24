from questions import QUESTIONS


def isAnswerCorrect(question, answer):
   
    if(answer==question["answer"]) :     
        return True

    else:
        return False    

def lifeLine(ques):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
    answer=ques["answer"]
    for i in range (1,5):
        if(answer!=i):
            print(f'\t\t\tOption {i}: {ques[f"option{i}"]}')
            break
    print(f'\t\t\tOption {answer}: {ques[f"option{answer}"]}') 
      


def kbc():
    

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    print(f'\t\t\tWelcome To The Game !!!\n')

    round =0
    amount=0
    padav=1;
    flag=0
    lifeline=0
    while round <15:

        print(f'\tQuestion {padav}: {QUESTIONS[round]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[round]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[round]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[round]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[round]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')

        if ans.lower()=="quit":
            break
        elif ans.lower()=="lifeline":
            if(lifeline==0 and round <14):
                lifeline=1
                lifeLine(QUESTIONS[round])
                ans = input('Your choice ( 1-4 ) : ')


            elif(lifeline==1 and round<14):
                print("You have already used the lifeline !") 
                ans = input('Your choice ( 1-4 ) : ')
                if ans.lower()=="quit":
                    break
            else:
                print("Lifeline is invalid now !")    
                ans = input('Your choice ( 1-4 ) : ')
                if ans.lower()=="quit":
                    break


   

        if isAnswerCorrect(QUESTIONS[round], int(ans) ):
        # print the total money won.
        # See if the user has crossed a level, print that if yes
            print('\nCorrect !')
            amount+=QUESTIONS[round]["money"]
            print("Ab tak ki Dhan-Rashi {} ".format(amount)+"\n")
            if(padav/5==1):
                print("You have crossed the 1st Padaav")
            elif(padav/5==2):
                print("You have crossed the 2nd Padaav")   
            elif (padav/5==3):
                print("You have crossed the 3rd Padaav")      
            

        else:
        # end the game now.
        # also print the correct answer
            print('\nIncorrect !')
            print("The correct answer is {}".format(QUESTIONS[round]["answer"])+"\n")
            flag=1
            break;
           
        round=round+1
        padav=padav+1
    # print the total money won in the end.
    if(flag==0):
        print("Final amount won by you is {} ".format(amount))

    else:
        if(round<5)  :  
            print("Final amount won by you is 0")
        elif(round>=5 and round<=9):
            print("Final amount won by you is 10,000")  
        elif(round>=10 and round <=14):
            print("Final amount won by you is 3,20,000")      
    

kbc()
