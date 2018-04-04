import random
import sys

def pick_word(words):
   return words[random.randrange(len(words))]
   

random.seed()
if len(sys.argv)<2:
   print "File path not specified in command line, aborting!"
   exit()
words=[]
try:
   file_object = open(sys.argv[1], "r")
except IOError:
   print "Can't open requested file, aborting!"
   exit()
for line in file_object:
   words.append(line[:-1])
file_object.close()
word=pick_word(words)
guessing_map=[False]*len(word)
wrong_guesses=[]
chances=3

print "\nWelcome to Hangman game!"
while chances>0 and all(v == True for v in guessing_map)==False:
   print_string=""
   for index, value in enumerate(guessing_map):
      if value==True:
         print_string+=word[index]+' '
      else:
         print_string+='_ '
   print print_string
   if len(wrong_guesses)>0:
      print "Previous wrong guesses:", ', '.join(wrong_guesses)
   guess=raw_input("Guess a letter: ")
   if len(guess)==1 and (guess.isalpha() or guess=='-'):
      index=word.find(guess.lower())
      if index==-1:
         chances-=1
         wrong_guesses+=guess
         print "Bad guess! You have", chances, "chances left"
      else:
         while index!=-1:
            guessing_map[index]=True
            index=word.find(guess, index+1)
            
   else:
      print "You have to guess precisely one letter (a-z or A-Z) or a hyphen (\"-\")"
   
if chances==0:
   print "You lost!"
else:
   print "You won! You guesses wrong letter", 3-chances, "times"
print "The keyword was \"" + word + "\""
