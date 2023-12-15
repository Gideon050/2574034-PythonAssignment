# Define a function to create three-letter abbreviations for words in a line
def create_abbreviations(line):
    words = line.split()  # Split the line into words
    abbreviations = []

    if len(words) >= 1:
        word = words[0]
        abbreviation = word[0].upper()  # First letter of abbreviation
        if len(word) >= 2:
            abbreviation += word[2].upper()  # Second letter of abbreviation
            if len(words) >= 2:
                word = words[1]
                abbreviation += word[0].upper()  # Third letter of abbreviation
            if len(words) >= 3:
                word = words[2]
            if len(word) >= 3:
                abbreviation += word[-1].upper()  # Last letter for abbreviation

    # Ensure the abbreviation is exactly three letters long
    abbreviation = abbreviation[:3]

    return abbreviation

# Function to read values of letters from a file
def read_values_file(values_file):
    letter_values = {}
    try:
        with open(values_file, 'r') as file:
            for line in file:
                letter, value = line.split()
                letter_values[letter] = int(value)
        return letter_values
    except FileNotFoundError:
        print(f"File '{values_file}' not found.")
        return None

def main():
    surname = "samuel"  # Fixed surname for output file name
    input_file_name = input("Enter the input file name: ")  # Prompt user for input file name

    output_file_name = f"{surname}_{input_file_name.split('.')[0]}_abbrevs.txt"  # Generate output file name

    # Values file name remains the same as provided
    values_file_name = "values.txt"

    # Create a dictionary to keep track of abbreviations and their counts
    abbreviation_count = {}

    # Create a dictionary to keep track of abbreviations and their scores
    abbreviation_scores = {}

    try:
        # Read letter values from file
        letter_values = read_values_file(values_file_name)

        if letter_values:
            with open(input_file_name, 'r') as input_file:
                lines = input_file.readlines()

                with open(output_file_name, 'w') as output_file:
                    for line in lines:
                        abbreviation_line = create_abbreviations(line)

                        # Check if the abbreviation is a duplicate
                        if abbreviation_line in abbreviation_count:
                            # Replace the last letter with the last letter of the last word
                            last_word = line.split()[-1]
                            if last_word:
                                abbreviation_line = abbreviation_line[:-1] + last_word[-1].upper()
                            else:
                                # Handle the case where the last word is empty
                                abbreviation_line = abbreviation_line[:-1]  # Remove the last letter

                        # Update the abbreviation count
                        abbreviation_count[abbreviation_line] = abbreviation_count.get(abbreviation_line, 0) + 1

                        # Append the count to the abbreviation if it's a duplicate
                        if abbreviation_count[abbreviation_line] > 1:
                            abbreviation_line += str(abbreviation_count[abbreviation_line])

                        # Ensure the abbreviation is exactly three letters long
                        abbreviation_line = abbreviation_line[:3]

                        # Compute sum of last two letters based on values, considering letter positions in words
                        sum_last_two_letters = 0
                        if len(abbreviation_line) >= 2:
                            last_two_letters = list(abbreviation_line[-2:])
                            words = line.split()
                            for i, letter in enumerate(last_two_letters):
                                for word in words:
                                    if word.endswith(letter):
                                        if letter == 'E':
                                            last_two_letters[i] = '20'
                                        else:
                                            last_two_letters[i] = '5'
                                        break
                                # If the letter is the first letter of any word, set its value to 0
                                if any(word.startswith(letter) for word in words):
                                    last_two_letters[i] = '0'
                            sum_last_two_letters = sum(int(letter_values.get(letter, 0)) for letter in last_two_letters)

                        # Store abbreviation and its score in the dictionary
                        abbreviation_scores[abbreviation_line] = sum_last_two_letters

                        # Write both the original line and the abbreviation to the output file
                        output_file.write(f"{line.strip()}\n")  # Include the original name
                        output_file.write(abbreviation_line + "\n")
                        print(f"Abbreviation: {abbreviation_line}, Score: {sum_last_two_letters}")  # Print the abbreviation and score

            print(f"Output saved to {output_file_name}")

    except FileNotFoundError:
        print(f"File '{input_file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Call the main function to execute the program
if __name__ == "__main__":
    main()

#Gideon Samuel - 2574034 - University of Dundee
