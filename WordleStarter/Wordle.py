# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
import string

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    #return a random word for the FIVE_LETTER_WORDS
    def set_answer() -> string:
        return random.choice(FIVE_LETTER_WORDS)
    
    #Returns a list of green tiles and potential yellows
    def check_for_green(guess: string, answer: string) -> list:
        green_pos = []
        yellow_candidates = []

        for n in range(0, 5):
            if guess.lower()[n] == answer[n]:
                green_pos.append(n)

            else:
                yellow_candidates.append(n)

        return green_pos, yellow_candidates

    #recieves the potentail yellows from the check_for_greens function and returns a list of yellows and by elimination grays
    def check_for_yellow(guess: string, answer:string, yellow_cands: list) -> list:
        yellow_pos = []
        ans_left = []
        guess_left = []

        for n in yellow_cands:
            ans_left.append(answer[n])
            guess_left.append(guess.lower()[n])

        for i in yellow_cands:
            if guess.lower()[i] in ans_left:
                yellow_pos.append(i)
                ans_left.remove(guess.lower()[i])
        
        return yellow_pos
        

    def milestone_one() -> string:
        answer = random.choice(FIVE_LETTER_WORDS)
        for col, l in enumerate(answer):
            gw.set_square_letter(0,col,l)


    def enter_action(s):
        #check if the guess not a real word
        if s.lower() not in FIVE_LETTER_WORDS:
            gw.show_message(f'{s} is not a real word, ')

        else:
            #check if the answer is correct
            if s.lower() == answer:
                for col in range(0, 5):
                    gw.set_square_color(gw.get_current_row(), col, "#66BB66") 
                    gw.show_message(f'You Won! It took you {gw.get_current_row() + 1} trie(s)')
            
            #check for greens, yellow, and grays
            else:
                #finds greens and possible yellow
                green_positions, yellow_cands = check_for_green(s, answer)

                #finds yellows
                yellow_positions = check_for_yellow(s, answer, yellow_cands)

                #set tiles to their proper color
                for pos in range(0, 5):
                    #make tile and key green
                    if pos in green_positions:
                        gw.set_square_color(gw.get_current_row(), pos, "#66BB66")
                        gw.set_key_color(s[pos], "#66BB66")

                    #make tile and key yellow  - unless key is already green
                    elif pos in yellow_positions:
                        gw.set_square_color(gw.get_current_row(), pos, "#CCBB66")

                        if gw.get_key_color(s[pos]) != "#66BB66":
                            gw.set_key_color(s[pos], "#CCBB66")

                    #make tile and key gray if they are not in the answer
                    #key and tile have different conditions to deal with multiple occurance of the same letter
                    else:
                        gw.set_square_color(gw.get_current_row(), pos, "#999999")
                        if s[pos] not in answer:
                            gw.set_key_color(s[pos], "#999999")

                #go to the next row
                gw.set_current_row(gw.get_current_row() + 1)

                #message
                gw.show_message('Good try, but wrong')

            

    gw = WordleGWindow()
    answer = set_answer()
    gw.show_message('take a guess')
    gw.add_enter_listener(enter_action)
    #milestone_one()

# Startup code

if __name__ == "__main__":
    wordle()
