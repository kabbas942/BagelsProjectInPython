import random
class bagals:
    Num_Digits = 3
    Max_Guesses = 10
    def main(self):
        print("\n******************** Bagals Project ********************\n")
        print("*Maximum No. of Guesses {}\n*No. of Digits is {}\n".format(10,3))
        #while True:
        secretNum = self.getSecretNum()
        print(secretNum)
        print("I have Thoughtup a number.")
        print('You have {} guesses to get it.'.format(self.Max_Guesses))
        numGuesses = 1
        while numGuesses <= self.Max_Guesses:
            guess = ''
            if len(guess)!=self.Num_Digits or not guess .isdecimal():
                print("Guess #{}:".format(numGuesses))
                guess=input("> ")
            numGuesses+=1
            clues = self.getClues(guess,secretNum)
            print(clues)
            if guess==secretNum:
                break
            if numGuesses > self.Max_Guesses:
                print("You runout of guesses!")
                print("The answer was {}".format(secretNum))                
                print("Do you want to play again? \n Yes \n NO")
                if not input('> ').lower().startswith('y'):  
                    break
        print('Thanks Playing!')
            #break

    
    def getSecretNum(self):
        Numbers = list('0123456789')
        random.shuffle(Numbers)
        secretNums = ''
        for i in range(self.Num_Digits):
            secretNums +=str(Numbers[i])
        return secretNums
    
    def getClues(self,guess,secretNum): 
        if guess == secretNum:            
            print("Get Secret Numbers {}".format(secretNum))
            return "you got it!"
        clues=[]
        for i in range(len(guess)):
            if guess[i]==secretNum[i]:
                clues.append('Fermi')
            elif guess[i] in secretNum:
                clues.append('Pico')
        if len(clues) == 0:
            return 'bagals'
        else:
            clues.sort()
            return ' '.join(clues)
                       
                