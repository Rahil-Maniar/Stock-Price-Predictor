# Checks for duplicate lines in a text file and removes them, keeping only the first instance of each line.
def remove_duplicates(file_path, output_path=None):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    seen_lines = set()
    unique_lines = []
    duplicates = {}

    for i, line in enumerate(lines):
        line_content = line.strip()
        if line_content in seen_lines:
            if line_content not in duplicates:
                duplicates[line_content] = []
            duplicates[line_content].append(i + 1)
        else:
            seen_lines.add(line_content)
            unique_lines.append(line)
    
    # Writing the unique lines back to the file or to a new file
    output_file_path = output_path if output_path else file_path
    with open(output_file_path, 'w') as file:
        file.writelines(unique_lines)

    if duplicates:
        print("Removed duplicate lines. The following lines had duplicates and were reduced to single instances:")
        for line, nums in duplicates.items():
            print(f"Line: '{line}' found at line numbers: {nums}. Only the first instance was kept.")
    else:
        print("No duplicate lines found.")

# Example usage
file_path = 'C:/Users/Rahil Maniar/Desktop/Stock Market Predictor/s1.txt'  # Replace with the path to your text file
output_path = 'C:/Users/Rahil Maniar/Desktop/Stock Market Predictor/s1_cleaned.txt'  # Optional: Replace with the path to save the cleaned file
remove_duplicates(file_path, output_path)
