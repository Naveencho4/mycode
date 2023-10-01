def take_input_array():
  """Takes input array from the user.

  Returns:
    A list containing the user input array elements.
  """

  # Ask the user for the size of the array.
  size = int(input("Enter the size of the array: "))

  # Create an empty array to store the user input.
  array = []

  # Iterate over the array and take input from the user for each element.
  for i in range(size):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)

  # Return the array.
  return array


# Example usage:
array = take_input_array()

print("The input array is:", array)
