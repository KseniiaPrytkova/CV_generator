#!/bin/python3

import sys
import os
import re

def if_match(line, dict):
    match = re.search(r"\{([^}]+)\}", line)
    if match:
        var = match.group(1)
        if var:
            for key in dict:
                if key == var:
                    var = dict.get(key)
                    new_line = re.sub(r'\{([^}]+)\}', var.strip("\n"), line)
                    return(new_line)
    return(None)

def generate_new_html(file_from, dict):
    name = str(file_from.split('.')[0]) + ".html"
    file_to = open(name, "w")
    with open(file_from) as f:
        for line in f:
            new_line = if_match(line, dict)
            if new_line == None:
                new_line = line
            file_to.write(new_line)
    file_to.close()

def get_values(dictionary):
    with open("settings.py") as f:
        for line in f:
            (key, val) = line.split(' = ')
            dictionary[key] = val
    return(dictionary)

def find_template_file(argument):
    templ_files = [f for f in os.listdir('.') if f.endswith('.template')]
    # print(type(templ_files)) ---> <class 'list'>
    # print(templ_files)  ---> ['file.template', 'myCV.template']
    if (len(templ_files) == 0):
        print("Error: I can't find files with this extension!")
        exit()
    for ff in templ_files:
        if(ff == argument):
            template_file = ff
            break
        else:
            template_file = None
    if(template_file == None):
        print("Error: I can't find such file with this name!")
        exit()
    return(template_file)   

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: I need 1 agument to work with!")
        exit()
    full_dict = {}
    template_file = find_template_file(sys.argv[1])
    full_dict = get_values(full_dict)
    generate_new_html(template_file, full_dict)
