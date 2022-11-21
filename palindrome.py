
def palidrome_search_game():
  print('...Booting up our palindrome search game...')
  on = True
  while on == True:
    b = input('I am looking for palindromes...\n')
    result = b==b[::-1]
    if result == False:
      print('Oof! Try again!')
    else:
      print(f'You did it! This is a {result} palindrome.')
      print('Thanks for playing!!')
      on = False