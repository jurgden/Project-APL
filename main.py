import palindrome
import str2int
import pystring
import file2list
import art 
import datetime
import time
import os
# 1)  This one liner will be dedicated to reversing lists followed by a palindrome detector

# a = [i+i*2 for i in range(8)]
# This line below completely reverses our list from front to back
# a = a[::-1]
# End of our one liner 
print(str(datetime.datetime.now()))
art.tprint('coolKIT', font='roman')
time.sleep(2.2)
os.system('clear')
art.tprint('-JJ  Futures')
time.sleep(1)
os.system('clear')
def main():
  # 1 for on / 0 for off
  xx01 = 1

  while xx01 == 1:
    a001 = input('Select your subroutine: [palidrome, pystring, file2list]\n')
    if a001 == 'palindrome':
      palindrome.palidrome_search_game()
      a002 = input('Would you like to return to the main menu? Y/N?\n')
      if a002 == 'Y':
        pass
      elif a002 == 'N':
        a003 = input('Exit program? Y/N?\n')
        if a003 == 'Y':
          break
      else: 
        break
    elif a001 == 'str2int':
      str2int.str2int()
      a002 = input('Would you like to return to the main menu? Y/N?\n')
      if a002 == 'Y':
        pass
      elif a002 == 'N':
        a003 = input('Exit program? Y/N?\n')
        if a003 == 'Y':
          break
      else: 
        break
    elif a001 == 'pystring': 
      print('...Please give me the integers that you would like to multiply by pi..')
      pystring.pystring(str2int.str2int())
      a002 = input('Would you like to return to the menu? Y/N?\n')
      if a002 == 'Y':
        pass
      elif a002 == 'N':
        a003 = input('Exit program? Y/N?\n')
        if a003 == 'Y':
          break
      else:
        break
    elif a001 == 'file2list':
      file2list.file2list()
      a002 = input('Would you like to return to the menu? Y/N?\n')
      if a002 == 'Y':
        pass
      elif a002 == 'N':
        a003 = input('Exit program? Y/N?\n')
        if a003 == 'Y':
          break
if __name__ == '__main__':
  main()