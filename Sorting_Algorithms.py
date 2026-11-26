# Student: URIEL JAMES O CABUGNASON
# Algorithm: Bubble Sort

full_name = "URIEL JAMES O CABUGNASON"
unsorted_array = []

for letter in full_name.upper():
    if letter.isalpha() and letter not in unsorted_array:
        unsorted_array.append(letter)

sorted_array = unsorted_array.copy()
n = len(sorted_array)

for i in range(n):
    for j in range(0, n - i - 1):

        if sorted_array[j] > sorted_array[j + 1]:
            # Swap adjacent elements
            sorted_array[j], sorted_array[j + 1] = (
                sorted_array[j + 1],
                sorted_array[j]
            )

print("===================================")
print("       SORTING ALGORITHMS")
print("===================================")

print("Student Name:", full_name)

print("\nUnsorted Array:")
print(unsorted_array)

print("\nSorted Array (A-Z):")
print(sorted_array)

print("\nTotal Unique Letters:", len(unsorted_array))
print("===================================")
