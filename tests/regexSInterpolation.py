import re
# Get usable input from inputed slash commands
# command pattern
str = '/echo asdf,123 -f'
cp = r'(?<=\/).*(?=\s\w|\n)'
command = re.search(cp ,str)
ap = r'(?<=\w\s).*(?=\s|\n)'
fp = r'(?<=\-).*'
attr = re.search(ap ,str)
flag = re.search(fp ,str)
print (command.group(0))
print (attr.group(0))
print (flag.group(0))