# pass me your intergers and i will convert them from string to real integers
def str2int():
  print('...Preparing receptors for user input...')
  userA = input('...Please give me the desired integers...\n')
  list_of_ints = list(map(int, userA.split()))
  print(f'Here is our list of integers: {list_of_ints}\n')
  return list_of_ints
