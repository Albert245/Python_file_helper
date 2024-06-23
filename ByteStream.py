def process_line(line):
    """Process each line by adding required characters and formatting."""
    # Add '0' and the length divided by 2 (as a character)
    length_div_2 = len(line) // 2
    formatted_line = f"0{length_div_2}{line}"
    
    # Ensure the length is 16 characters, pad with '0' if necessary
    if len(formatted_line) < 16:
        formatted_line = formatted_line.ljust(16, '0')
    
    # Insert a colon after every 2 characters
    formatted_line = ':'.join(formatted_line[i:i+2] for i in range(0, len(formatted_line), 2))
    
    
    
    return formatted_line

def process_text(text):
    """Process each line of the text."""
    lines = text.splitlines()
    processed_lines = [process_line(line) for line in lines]
    return '\n'.join(processed_lines)

# Example usage
input_text = """123456
abcdef
987654"""

processed_text = process_text(input_text)
print(processed_text)