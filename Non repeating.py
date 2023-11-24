def first_non_repeating(nums):
  #Empty dictionary to store the frequency elements
  freq = {}
  # Loop through the list of numbers
  for num in nums:
    # If the number is already in the dictionary, increment its frequency by one
    if num in freq:
      freq[num] += 1
    # Otherwise, set its frequency to one
    else:
      freq[num] = 1
  # Loop through the list of numbers again
  for num in nums:
    # If the number has a frequency of one, return it as the first non-repeating element
    if freq[num] == 1:
      return num
  # If no such element is found, return -1
  return None

#example
print(first_non_repeating([1, 2, 3, 4, 4, 5,1,2,3]))