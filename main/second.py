#import pandas as pd

# i think this is correct
#def load_data(file_path):
#    data = pd.read_csv(file_path)
#    return data

# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Example usage
if __name__ == "__main__":
    test_string = "madam"
    if is_palindrome(test_string):
        print(f"'{test_string}' is a palindrome.")
    else:
        print(f"'{test_string}' is not a palindrome.")
