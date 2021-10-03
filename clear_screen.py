import os
from time import sleep
# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
   # print out some text
print("The platform is: ", os.name)
print("big output\n"* 5)
# wait for 5 seconds to clear screen
sleep(5)
# now call function we defined above
screen_clear()