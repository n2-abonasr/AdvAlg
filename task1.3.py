import concurrent.futures
import re

def count_name(name, text):
    # Count the frequency of each name in the text
    return name, len(re.findall(name, text, re.IGNORECASE))

def main():
    # Read the names from the file
    with open('task1_3_names.txt', 'r', encoding='utf-8') as f:
        names = [name.strip() for name in f.readlines()]

    # Read the text from the file
    with open('task1_3_text.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    # Use a ThreadPoolExecutor to count the names in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(count_name, names, [text]*len(names)))

    # Write the results to a new file
    with open('results.txt', 'w', encoding='utf-8') as f:
        for name, count in results:
            f.write(f"{name}: {count}\n")

if __name__ == "__main__":
    main()