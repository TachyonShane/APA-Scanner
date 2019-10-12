## APA Scanner

### Purpose
apa_scanner.py uses Python regular expressions to find common writing errors related to the APA style, and scholarly writing in general. 
- By default, it will scan the document and print paragraph-by-paragraph feedback to the terminal. Upon reaching the references section, it will stop.
- Compatible with .txt and .docx files
- Summarized output can be saved to a text file using the `--output` parameter
- Detailed output (feedback *and* original text) can be saved using  `--output` with the `--full` flag
- Terminal output can be supressed with the `--quiet` flag 


### 
Files included are apa_scanner.py (the script) and regex.csv (the text patterns).



### Usage
`./apa_scanner.py [-h] --input INPUT [--output OUTPUT] [--quiet] [--full]`

#### Only print feedback to screen: ####
`./apa_scanner.py --input magna_carta.txt` 

#### Print feedback to the screen and save summary feedback to edits.txt: ####
`./apa_scanner.py --input walden.docx --output edits.txt` 

#### Print nothing to screen and save full details to feedback.txt: ####
`./apa_scanner.py --input my_essay.docx --output feedback.text --full --quiet`