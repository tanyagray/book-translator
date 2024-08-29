import os

'''
========================
SETTINGS
========================

Replace the values with your own.
See the README file for details on each setting.
'''

INPUT_FILE = "input/sample.txt"
OUTPUT_FILE = "output/sample.csv"

OPENAI_API_KEY = ""
CLAUDE_API_KEY = ""

'''
========================
SET UP FILES
========================
'''

# Create a reference to the input file in "read" mode
input_file = open(INPUT_FILE, "r")

# Delete previous output file if it exists
if os.path.exists(OUTPUT_FILE):
  os.remove(OUTPUT_FILE)

# Create a new output file in "append" mode
output_file = open(OUTPUT_FILE, "a")

'''
========================
SPLIT INTO CHUNKS
========================
'''

content_chunk = ""

while True:
    # read one letter/character at a time.
    # includes spaces, newlines ("enter"), tabs etc
    current_character = input_file.read(1)

    # if we read a character and it has no value,
    # we've finished the file and gone past the end
    # of the content.
    if not current_character:
        if len(content_chunk) > 0:
          output_file.write(content_chunk + "\n")
        print("End of file")
        break
    
    # if the current character is a "new line",
    # then we can treat this as the end of a paragraph.
    elif current_character == "\n":
        if len(content_chunk) > 0:
          output_file.write(content_chunk + "\n")
          content_chunk = ""

    # for all other characters, we should add it
    # to the content chunk we are currently collecting.
    else:
        content_chunk = content_chunk + current_character

