#!/usr/bin/env python3

""" APA Style Scanner """

import argparse
import csv
import os.path
import re
import textwrap
import time
import docx


#######################
###### FUNCTIONS ######
#######################


#
# Print messages related to regex matches
#

def print_match(message, matches, source="", quiet="False"):
    # Create horizontal line a bit longer than the the message
    if source:
        message += " ({src})".format(src=source)
    hline = "-" * (len(message) + 6)
    # If there are matches, print them
    if matches:
        # Create formatted message
        output = '''\
        {topline}
           {msg}
        {bottomline}
           Matches found:\
                  '''.format(topline=hline, msg=message, bottomline=hline)

        if not quiet:
           # Output formatted message (sans indents)
            print(textwrap.dedent(output))

            # Output match(es)
            for match in matches:
                print("   -> \"", match, "\"", sep='')


#
# Add paragraphs to output file
#

def save_paragraphs(file_obj, para):
    try:
        file_obj
        file_obj.write(paragraph)
    except:
        print("Please specify an output file name.")
        quit()


#
# Add the feedback to a file, if specified
#

def append_file(message, matches, source="", file_obj=""):
# Create horizontal line a bit longer than the the message
    if source:
        message += " ({src})".format(src=source)

    hline = "-" * (len(message) + 6)
    # If there are matches, print them
    if matches:
        # Create formatted message
        output = '''
        {topline}
           {msg}
        {bottomline}
           Matches found:\n
                  '''.format(topline=hline, msg=message, bottomline=hline)

        output_message = textwrap.dedent(output)

        #Print message
        file_obj.write(output_message)
        # Output match(es)
        for match in matches:
            match = "\t -> " + match + "\n"
            file_obj.write(match)


#
# Place bookmarks in terminal and file output
#

def place_bookmarks(paragraph_num, content, quiet, output, file_obj):
    text_location = "ITEM " + str(paragraph_num) + "/" + str(len(content))
    newfile = True
    if not quiet:
        hline = "*" * (len(text_location) + 6)
        bookmark = '''\
        {topline}
           {msg}
        {bottomline}
                  '''.format(topline=hline, msg=text_location, bottomline=hline)
        print(bookmark)

    if output and file_obj:
        spaces = " " * (16)
        text_location = spaces + " " * 3 + text_location
        hline = spaces + "*" * 21
        bookmark = '''\
        \n{topline}
           \n   {msg}
        \n{bottomline} 
'''.format(topline=hline, msg=text_location, bottomline=hline)

        #Skip newlines on blank files
        if newfile:
            newfile = False
        elif not newfile:
            file_obj.write("\n\n\n")
        file_obj.write(bookmark)


#
# Recieve a file name, open it, and return a list of its contents
#

def import_csv(file):
    # Open file and map contents to list
    with open(file) as regex_file:
        reader = csv.reader(regex_file)
        next(reader)
        data = []
        for row in reader:
            data.append(row)
    return data


#
# Open a .txt or .docx doc and parses it
#

def open_target_paper(targ_paper):
    # Open target paper if .txt
    if targ_paper.endswith(".txt"):
        with open(targ_paper) as paper:
            content = paper.read()
            paragraphs = content.split("\n")
    # Else, if .docx, open and parse
    elif targ_paper.endswith(".docx"):
        paper = docx.Document(targ_paper)
        paragraphs = []
        for para in paper.paragraphs:
            if para.text:
                if bool(re.search(r'^\s*[Rr]eferences\s*$', para.text)):
                    break
                else:
                    paragraphs.append(para.text)
    else:
        print("Supported file types: .docx and .txt")
        quit()
    return paragraphs


#
# Parse command-line arguments
#

def invoke_parser():
    parser = argparse.ArgumentParser(description='Scan for common APA style errors')
    parser.add_argument("--input", type=str, required=True, help="Specify input file")
    parser.add_argument("--output", type=str, help="Specify input file")
    parser.add_argument("--quiet", default=False, action="store_true", help="Suppress terminal output")
    parser.add_argument("--full", default=False, action="store_true", help="Include input text with file output")
    return parser.parse_args()





##########################
######  MAIN BLOCK  ######
##########################

# Invoke the parser
args = invoke_parser()

# Open rules dictionary and move to array
regex_list = import_csv("regex.csv")

# Open paper and split into array of paragraphs
paragraphs = open_target_paper(args.input)

# Placeholder for file_object
file_object = None

# Create output file (append time if one already exists)
if args.output:
    if os.path.isfile(args.output):
        args.output = args.output.rstrip(".txt") + time.strftime("%m%d%y-%S", time.localtime()) + ".txt"
    file_object = open(args.output, "a+")

# Paragraph counter
para_number = 0

# Iterate through each paragraph
for paragraph in paragraphs:

    # Strip junk
    paragraph = paragraph.replace('•', '').strip()
    # Count paragraphs   
    para_number += 1
    # Print paragraph markers
    place_bookmarks(para_number, paragraphs, args.quiet, args.output, file_object)
    # Save paragraphs to file
    if args.full:
        save_paragraphs(file_object, paragraph)
    # Print to screen unless user specifies others
    if not args.quiet:
        print(paragraph)

# In each paragraph, iterate through regex list, find all matches, and print information
    for row in regex_list:
        match = re.findall(row[0], paragraph)
        if match and row[2]:
            print_match(row[1], match, row[2], args.quiet)
            if args.output:
                append_file(row[1], match, row[2], file_object)
        elif match and not row[2]:
            print_match(row[1], match, "", args.quiet)
            if args.output:
                append_file(row[1], match, "", file_object)