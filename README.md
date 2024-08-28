# book-translator

Takes a plain text document and outputs a CSV of the translation broken into chunks.

## Usage

1. Export your Word document as plain text so that it is a `.txt` file
2. Copy the file into the `input` folder in this project
3. Edit the settings at the top of `src/translate.py` to reference your preferred input and output files
4. Open a console/terminal in the `book-translator` folder
5. Type `python3 src/translate.py` and press **Enter** (may just be `python src/translate.py` on Windows)
6. Look in the `output` folder for the CSV file you specified as `OUTPUT_FILE`
