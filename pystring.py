import math 
def pystring(list):
  print('...Loading up pystring...')
  pied_list = [round(i ** math.pi, 2) for i in list]
  print(f'Here is your list after every element has been squared by Pi: {pied_list}\n')
  usr001 = input('Would you like to add the list items up to a total? Y/N?\n')
  total = 0
  if usr001 == 'Y':
    for i in pied_list:
      total += i
      print(f'Total: {total}')
  elif usr001 == 'N':
    pass
  print(f'Your final sum for your pied list is {total}')
  return pied_list, total