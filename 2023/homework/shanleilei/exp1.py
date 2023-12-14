import re


with open("python_submit.txt","r") as f:
    lines = f.readlines()

new_lines = []

for line in lines:
    new_line = re.sub("[0-9]+\.", "", line)
    new_lines.append(new_line)

with open("text2.txt", "w") as f:
    for new_line in new_lines:
        f.write(new_line)