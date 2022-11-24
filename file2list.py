


def file2list():
  filename = input('Please enter the filename:\n')
  new_list = [line.strip() for line in open(f'{filename}', 'r')]
  print(f'Here are the results from your file:\n{new_list}')
  return new_list