def getLargestSequence (list, comparator):
  largestSequence = []
  currentSequence = [list[0]]

  for i in range (1, len (list)):
    if comparator (list[i], currentSequence[len (currentSequence) - 1]):
      currentSequence.append (list[i])
    else:
      if len (currentSequence) > len (largestSequence):
        largestSequence = currentSequence

      currentSequence = [list[i]]

  if len (currentSequence) > len (largestSequence):
    largestSequence = currentSequence

  return largestSequence


inputList = [int (x) for x in input ().split ()]

list2 = getLargestSequence (inputList, lambda x, y: x >= y)
list3 = getLargestSequence (inputList, lambda x, y: x <= y)

print (list2 if len (list2) >= len (list3) else list3);