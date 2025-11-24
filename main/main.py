# Function to select numbers and sort them
def select_and_sort_numbers(numbers):
    """
    Takes a list of numbers, filters out non-numeric values, and returns a sorted list.
    """
    # Filter out non-numeric values
    numeric_values = [num for num in numbers if isinstance(num, (int, float))]
    # Sort the numeric values
    return sorted(numeric_values)

# Example usage
if __name__ == "__main__":
    sample_data = [10, "hello", 3.5, 7, "world", 2]
    sorted_numbers = select_and_sort_numbers(sample_data)
    print("Sorted numbers:", sorted_numbers)