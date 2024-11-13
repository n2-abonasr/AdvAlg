def longest_substrings_with_k_repeats(input_string, k):
    n = len(input_string)
    longest_substrings = []
    max_length = 0
    
    # Iterate over all possible starting indices of substrings
    for start in range(n):
        char_count = {}
        
        # Iterate over all possible ending indices of substrings
        for end in range(start, n):
            char = input_string[end]
            char_count[char] = char_count.get(char, 0) + 1

            # Check if there are exactly k characters with counts greater than or equal to 2
            valid_chars = [char for char, count in char_count.items() if count >= 2]
            if len(valid_chars) == k:
                substring_length = end - start + 1
                # Update the longest substrings found
                if substring_length > max_length:
                    max_length = substring_length
                    longest_substrings = [(input_string[start:end + 1], {char: char_count[char] for char in valid_chars})]
                elif substring_length == max_length:
                    longest_substrings.append((input_string[start:end + 1], {char: char_count[char] for char in valid_chars}))
    
    return longest_substrings, max_length

def main():
    try:
        file_path = "letters.txt"
        
        with open(file_path, "r") as file:
            input_string = file.read().strip()
        
        if not input_string:
            print("Input string is empty.")
            return
        
        k = int(input("Enter the value of k: "))
        longest_substrings, max_length = longest_substrings_with_k_repeats(input_string, k)
        
        if longest_substrings:
            print(f"Longest substrings with exactly {k} repeated elements . Longest Substring is {max_length} ")
            for substring, freq in longest_substrings:
                # Convert substring to list of characters for output
                chars_list = list(substring)
                freq_list = list(freq.items())
                print(chars_list, "with the frequency", freq_list)
        else:
            print(f"No valid substrings found with exactly {k} repeated elements.")
    
    except ValueError:
        print("Invalid input for k. Please enter a valid integer.")

if __name__ == "__main__":
    main()
