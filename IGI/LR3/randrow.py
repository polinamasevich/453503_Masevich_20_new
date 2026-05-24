import random

def random_row(N):
  """ 
  Generator of N random ints from -10 to 10
  """
  for i in range(N):
    yield random.randint(-10, 10)