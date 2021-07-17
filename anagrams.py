 anagrams = {}

  #how to sort letters in word
  def sorted(string):
      letters = []
      str = ''
      for s in string:
          letters.append(s)
      letters.sort()
      letters_new = ''.join(letters)
      return letters_new


  #import dictionary of all words
  valid_words = []
  with open('words_alpha.txt') as word_file:
      valid_words = (word_file.read().split())    

  #make dictionary of sorted words 
  for i in range (0,len(valid_words)):
      alpha_order = sorted(valid_words[i])
      if alpha_order not in anagrams: 
          anagrams[alpha_order] = []
          anagrams[alpha_order].append(valid_words[i])
      else:
          anagrams[alpha_order].append(valid_words[i])


  word = input("enter a word: ")

  #check for anagrams
  word_sorted = sorted(word)
  if word_sorted in anagrams and len(anagrams[word_sorted]) > 1: 
      print("anagrams: ")
      for i in range(0, len(anagrams[word_sorted])):
          if anagrams[word_sorted][i] != word:
              print(anagrams[word_sorted][i])
  else: 
      print("no anagrams")
