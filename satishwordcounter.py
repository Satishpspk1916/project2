def count_words(input_text):
    """
    Counts the number of words in the given input text.
    """
    # Check if the input text is empty
    if not input_text:
        print("Error: The input text is empty.")
        return 0

    # Split the input text into words using the space character as a delimiter
    words = input_text.split()

    # Count the number of words
    word_count = len(words)

    return word_count

def main():
    """
    The main function of the Word Counter program.
    """
    # Get user input
    input_text = input("Please enter a sentence or paragraph: ")

    # Count the number of words in the input text
    word_count = count_words(input_text)

    # Display the word count
    print(f"The number of words in the input text is: {word_count}")

main()