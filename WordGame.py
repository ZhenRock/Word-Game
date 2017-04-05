#Zhenya Rock
#CS 021
#This program is word guessing game. The user will have 5 tries to
#guess what the scrambled word displays is before the game ends. The
#user can give up or quit at any time.

import random
import tkinter


class WordGameGUI:
    def __init__(self):
        #Exception Handling
        try:
            #get the word and its scrambled version
            word, scrambled = get_scrambled_word()
            #set guess attempts to 0
            self.attempts = 0
            #define original word so it can be used later
            self.word = word

            # Create the main window.
            self.main_window = tkinter.Tk()
            # Create three frames to group widgets.
            self.upper_frame = tkinter.Frame()
            self.top_frame = tkinter.Frame()
            self.mid_frame = tkinter.Frame()
            self.bottom_frame = tkinter.Frame()

            #Widgets for upper frame
            self.info_label = tkinter.Label(self.upper_frame, \
                                              text='Your word to unscramble:')
            self.word_label = tkinter.Label(self.upper_frame, \
                                              text=scrambled)
            
            #pack upper frame
            self.info_label.pack(side='left')
            self.word_label.pack(side='left')
            
            #widgets for top frame
            self.prompt_label = tkinter.Label(self.top_frame, \
                                              text='Your guess:')
            self.guess_entry = tkinter.Entry(self.top_frame, \
                                            width=10)

            #Pack top frame's widgets
            self.prompt_label.pack(side='left')
            self.guess_entry.pack(side='left')

            #make StringVar object
            self.value = tkinter.StringVar()

            #create a label and associate it with the StringVar object
            self.statement_label = tkinter.Label(self.bottom_frame, \
                                             textvariable=self.value)
            #Pack middle frame's widgets
            self.statement_label.pack(side='left')
            
            #Create button widgets for the mid frame: guess, give up, quit
            self.guess_button = tkinter.Button(self.mid_frame, \
                                              text='Guess', \
                                              command=self.guess)
            self.giveup_button = tkinter.Button(self.mid_frame, \
                                              text='Give up', \
                                              command=self.giveup)
            self.quit_button = tkinter.Button(self.mid_frame, \
                                              text='Quit', \
                                              command=self.main_window.destroy)
            #Pack the buttons
            self.guess_button.pack(side='left')
            self.giveup_button.pack(side='left')
            self.quit_button.pack(side='left')

            #Pack the frames
            self.upper_frame.pack()
            self.top_frame.pack()
            self.mid_frame.pack()
            self.bottom_frame.pack()
            
            #Enter the tkinter main loop.
            tkinter.mainloop()
        except:
            print("There was an error.")

    #this function keeps track of the number of guesses the user has
    #made and determines whether or not the user has won, and if the
    #game should conclude
    def guess(self):
        #Exception handling
        try:
            #get the guess the user entered
            guess = self.guess_entry.get()
            #add to the number of attempts
            self.attempts += 1
            MAX = 5
            #If guess is right, tell user they won
            if guess == self.word:
                self.value.set("You win! " + "The word is " + self.word \
                               + '.' + '\n' + 'It took you ' + \
                               str(self.attempts) + " guesses.")
                self.giveup_button.config(state = "disabled")
                self.guess_button.config(state = "disabled")
            #If the user is wrong and still has attempts left, tell them
            #what guess they are on and what their guess was
            elif guess != self.word and self.attempts < MAX:
                self.value.set("Guess " + str(self.attempts) + ": " + \
                               guess + " is not correct.")
            #If the user is incorrect for the fifth time, they lose
            elif guess != self.word and self.attempts == MAX:
                self.guess_button.config(state = "disabled")
                self.giveup_button.config(state = "disabled")
                self.value.set("You are out of guesses, the word is " + \
                               self.word + '.')
        except:
            self.value.set("Error.")

    #This function will display the correct answer if the user gives up
    def giveup(self):
        
        self.value.set("The word is " + self.word + '.')
        self.guess_button.config(state = "disabled")
        self.giveup_button.config(state = "disabled")

#This function gets a word from the file and scrambles it
def get_scrambled_word():
    #Exception handling
    try:
        #open file
        all_words = open('dict.txt','r')
        #make a dictionary of the words assigning each one a value
        dictionary = {}
        number_label = 0
        for word in all_words:
            dictionary[number_label] = word
            number_label += 1
        #choose a random one
        FIRST = 0
        LAST = 19914
        random_key = random.randint(FIRST, LAST+1)
        value = dictionary.get(random_key)
        word = value.strip()
        #make the word into a list
        letter_list = []
        for letter in word:
            letter_list.append(letter)
        #shuffle the list
        random.shuffle(letter_list)
        scrambled = ''
        for letter in letter_list:
            scrambled += letter
        if scrambled == word:
            random.shuffle(letter_list)
            scrambled = ''
            for letter in letter_list:
                scrambled += letter
        #return the values
        return word, scrambled
    except:
        print('Error!')

# Create an instance of the WordGameGUI class.
word_game = WordGameGUI()

