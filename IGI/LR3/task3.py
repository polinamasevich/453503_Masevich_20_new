import ui

def run():
  """
  Main runner of third task, requests string from user and counts
  number of digits and uppercase english letters. Displays the result
  """
      
  st = ui.read_str("Enter string: ")
  count_digit = 0
  count_upperalpha = 0
  for c in st:
    if c.isdigit():
      count_digit += 1
    
    if c.isupper() and c.isalpha():
      count_upperalpha += 1

  print(f"Number of digits: {count_digit}")
  print(f"Number of uppercase letters: {count_upperalpha}")
  print(f"Total: {count_digit + count_upperalpha}")