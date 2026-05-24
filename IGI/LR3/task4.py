import ui

def list_odds(arr):
  """
  Returns list of odd values from input list
  """

  return [x for i, x in enumerate(arr) if i % 2 == 1]

def run():
  """
  Main runner of third task, requests string from user, counts words
  finds longest word and displays results.
  """

  st = ui.read_str("Enter string: ")
  words = st.split()

  print("Word count: ", len(words))

  longest_word_i, longest_word = max(enumerate(words), key=lambda x: len(x[1]))

  print(f"Longest word: {longest_word}")
  print(f"Longest word index: {longest_word_i}")

  print(f"All odd words", " ".join(list_odds(words)))