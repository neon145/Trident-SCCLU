import re
import os
from termcolor import colored,cprint
import sys
from emoji import emojize
commands = [{"name": "add","desc":"Adds a task","flags": {"f":"*"}}]
class Engine:
    def __init__(self):
        self.commands = []
        self.commandHistory = []
        self.bootMessage = emojize(f"Initiating {colored('Trident','light_cyan',attrs=['bold'])} CLI Engine...")
        self.active = False

    def listCommands(self):
        print(colored("AVAILABLE COMMANDS",attrs=["bold"]).center(getattr(os.get_terminal_size(),'columns')//2))
    def activatePortal(self):
        self.active = True
        print(self.bootMessage)
def commandParser (s):
    flags = []
    content = ""
    command = ""
    data = ""
    arguments = []
    for i in commands:
        command = re.sub(r'^.*?/', '/', s) #removes text before /
        if re.search(i, command):
            
            data = command.replace(i, "")
            data = data+" " if not data.endswith(' ') else data
            flags = re.findall(r'\-(.\w*?)\s',data) # getting the flag
            args = re.findall(r'(?<=\[)(.+)(?=\])', data)[0].split(',')
            for arg in args:
                key = re.findall(r'([A-Z]|\_|\d).*(?=\=)',arg)[0]
                val = re.sub(r'([A-Z]|\_|\d).*(?=\=)','',arg).replace('=', '')
                arguments.append({'key':key, 'val':val})
            content = re.sub(r'\-(.\w*?)\s','',data).strip()
        return arguments

# k = input("Enter command: ")
# print(commandParser(k))
k = Engine()
k.activatePortal()
k.listCommands()