from texttable import Texttable
from collections import OrderedDict

def isterminal(char):
    if(char.isupper() or char == "`"):
        return False
    else:
        return True

def insert(grammar, lhs, rhs):
    if(lhs in grammar and rhs not in grammar[lhs] and grammar[lhs] != "null"):
        grammar[lhs].append(rhs)
    elif(lhs not in grammar or grammar[lhs] == "null"):
        grammar[lhs] = [rhs]
    return grammar

def show_dict(dictionary):
    for key in dictionary.keys():
        print(key+"  :  ", end = "")
        for item in dictionary[key]:
            if(item == "`"):
                print("ε, ", end = "")
            else:
                print(item+", ", end = "")
        print("\b\b")

def get_rule(non_terminal, terminal, grammar, grammar_first):
    for rhs in grammar[non_terminal]:
        #print(rhs)
        for rule in rhs:
            if(rule == terminal):
                string = non_terminal+"~"+rhs
                return string
            
            elif(rule.isupper() and terminal in grammar_first[rule]):
                string = non_terminal+"~"+rhs
                return string

def display_parse_table(parse_table, terminals, non_terminals):
    print("\nParsing table:")
    table = Texttable(max_width=0)
    table.header([""]+terminals)
    for non_terminal in non_terminals:
        row = [non_terminal] + parse_table[non_terminals.index(non_terminal)]
        table.add_row(row)

    print(table.draw())

def readFile(file_path):
    f = open(file_path)
    g= OrderedDict()
    g_first = OrderedDict()
    g_follow = OrderedDict()
    # iterate each line and generate grammar dictionary
    for i in f:
        # replace end line symbol
        i = i.replace("\n", "")
        lhs, rhs = i.split(sep="~")
        g = insert(g, lhs, rhs)
        g_first[lhs] = "null"
        g_follow[lhs] = "null"
    f.close()
    return g, g_first, g_follow



def getUserInput(debug=False):
    if(debug):
        file_path = "grammar.txt"
        test_str = "abbcc"
    else:
        file_path = input("Enter file path, relative to the main.py\n")
        test_str = str(
            input("Enter test string, terminals seperated by space and appending $ eg abbcc\n"))

    test_str=test_str+'$'

    print()

    return file_path, test_str

def generateNonTerminals(grammar):
    return list(grammar.keys())

def generateTerminals(grammar):
    allLexemes = {char for values in grammar.values() for item in values for char in item}
    terminals = list(filter(isterminal, allLexemes)) + ["$"]
    return terminals

def print_result(is_parsed, test_str):
    if is_parsed:
        print("\n\nInput expression '{input}' is accepted.".format(input=test_str[:-1]))
    else:
        print("\n\nInput expression '{input}' is NOT accepted.".format(input=test_str[:-1]))
