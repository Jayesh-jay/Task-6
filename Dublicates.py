# Define three lists
list1 = [1, 2, 3, 4, 5, 7]
list2 = [2, 4, 7, 6, 8, 10]
list3 = [3, 4, 9, 12, 7, 15]

# Create an empty set to store the duplicates
duplicates = set()

# Loop through the first list
for num in list1:
  # Check if the number is in the second and third list
  if num in list2 and num in list3:
    # Add it to the set of duplicates
    duplicates.add(num)

# Convert the set to a list
duplicates = list(duplicates)

# Print the list of duplicates
print("Dublicates Numbers:", duplicates)