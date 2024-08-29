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
RE-USABLE FUNCTIONS
========================
'''

def get_text_chunk_from_file(file):

  text_chunk = ""

  while True:
    # read one letter/character at a time
    # includes spaces, newlines ("enter"), tabs etc
    current_character = file.read(1)

    # if we read a character and it has no value,
    # we've finished the file and gone past the end
    # of the content.
    # we should return the text_chunk because it
    # will contain the final paragraph of the text.
    if not current_character:
      if len(text_chunk) > 0:
        break
      else:
        text_chunk = None
        break

          
    # if the current character is a "new line",
    # then we can treat this as the end of a paragraph.
    elif current_character == "\n":
      if len(text_chunk) > 0:
        break

    # for all other characters, we should add it
    # to the content chunk we are currently collecting.
    else:
      text_chunk = text_chunk + current_character

  return text_chunk


'''
========================
PROCESS THE FILE
========================
'''

while True:

  chunk = get_text_chunk_from_file(input_file)

  if chunk:
    output_file.write(chunk + "\n")

  else:
    print("\nDone")
    break



