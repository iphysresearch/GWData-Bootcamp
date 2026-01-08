import re

# re module in Python provides support for regular expressions, which
# is a powerful way to search, match, and manipulate strings based on
# pattern 
def extract_choices(markdown_content):
    pattern = re.compile(r'^## (\d+\. [A-Z])', re.MULTILINE)
    matches = pattern.findall(markdown_content)
    # here matches is a list

    choices = {}
    for match in matches:
        # match can be changed to any name, only it matches the following name
        parts = match.split('. ')
        if len(parts) == 2:
            number = int(parts[0])
            choice = parts[1]
            choices[number] = choice

    return choices



def extract_choices_from_file(inputfile_path,outputfile_path):
    with open(inputfile_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()


    choices = extract_choices(markdown_content)

    with open(outputfile_path, 'w', encoding='utf-8') as output_file:
        for number, choice in choices.items():
            output_file.write(f"{choice}\n")




# example
inputfile_path = './231203_pandas/choose.md'  
outputfile_path = './231203_pandas/pandas_submit.txt'
result = extract_choices_from_file(inputfile_path,outputfile_path)

