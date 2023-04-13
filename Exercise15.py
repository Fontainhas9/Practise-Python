def reverse_words(string):
  words = string.split()
  return ' '.join(words[::-1])

string = input("Enter a long string containing multiple words: ")

print(reverse_words(string))