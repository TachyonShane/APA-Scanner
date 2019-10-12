## APA Scanner

### Purpose
apa_scanner.py uses Python regular expressions to find common writing errors related to the APA style, and scholarly writing in general. 
- By default, it will scan the document and print paragraph-by-paragraph feedback to the terminal. Upon reaching the references section, it will stop.
- Compatible with .txt and .docx files
- Summarized output can be saved to a text file using the `--output` parameter
- Detailed output (feedback *and* original text) can be saved using  `--output` with the `--full` flag
- Terminal output can be supressed with the `--quiet` flag 

Files included are apa_scanner.py (the script) and regex.csv (the text patterns).



### Usage
`./apa_scanner.py [-h] --input INPUT [--output OUTPUT] [--quiet] [--full]`

#### Only print feedback to screen: ####
`./apa_scanner.py --input magna_carta.txt` 

#### Print feedback to the screen and save summary feedback to edits.txt: ####
`./apa_scanner.py --input walden.docx --output edits.txt` 

#### Print nothing to screen and save full details to feedback.txt: ####
`./apa_scanner.py --input my_essay.docx --output feedback.text --full --quiet`

### Example Output

```It's interesting that a terrible attempted ERP rollout by HP definitely experienced several bad obstacles in close proximity, resulting in a massive impact on the company.  While the estimated monetary impact of the failed project was 160 million dollars, HP is generally doing sort of well (“When Bad Things Happen to Good Projects,” 2007).
------------------------------------------------------------------------------
   Avoid words that express value judgements (Antioch Univ. Writing Center)
------------------------------------------------------------------------------
   Matches found:                  
   -> "terrible"
   -> "bad"
   -> "Bad"
   -> "Good"
--------------------------------------------
   Avoid wordy phrases (APA Pub Manual 3.08)
--------------------------------------------
   Matches found:                  
   -> "close proximity"
-----------------------------------------------------
   Avoid Contractions (APA Style Blog - Dec. 2015)
-----------------------------------------------------
   Matches found:                  
   -> "It's"
--------------------------------------------------------------------------------
   Restrict "since" and "while" to temporal sense (APA Style Blog - May 2011)
--------------------------------------------------------------------------------
   Matches found:                  
   -> "While"
-------------------------------------------------------------------------------
   Variations of "it's important" may be wordy (APA Style Blog - Sept. 2015)
-------------------------------------------------------------------------------
   Matches found:                  
   -> "It's interesting"
--------------------------------------------------------------------------------
   Phrases like "kind of" can dilute writing (Purdue OWL - Eliminating Words)
--------------------------------------------------------------------------------
   Matches found:                  
   -> "sort of"
-------------------------------------------------------------------
   Potentially unnecessary word (Purdue OWL - Eliminating Words)
-------------------------------------------------------------------
   Matches found:                  
   -> "definitely"
   -> "generally"
```
