from collections import OrderedDict
from utils import show_dict, isterminal, display_parse_table, insert
from first import first
from follow import follow
from ll1 import generate_parse_table, parse

DEBUG_MODE = False

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

if __name__ == "__main__":

    file_path, test_str = getUserInput(DEBUG_MODE)
    grammar,  grammar_first, grammar_follow = readFile(file_path)

    print("Grammar\n")
    show_dict(grammar)

    for lhs in grammar:
        if(grammar_first[lhs] == "null"):
            grammar_first = first(lhs, grammar, grammar_first)
            
    print("\n\n\n")
    print("First\n")
    show_dict(grammar_first)


    start = list(grammar.keys())[0]
    for lhs in grammar:
        if(grammar_follow[lhs] == "null"):
            grammar_follow = follow(lhs, grammar, grammar_follow, start, grammar_first)
            
    print("\n\n\n")
    print("Follow\n")
    show_dict(grammar_follow)


    non_terminals = generateNonTerminals(grammar) 
    terminals = generateTerminals(grammar)

    print(non_terminals)
    print(terminals)

    print("\n\n\n\n\t\t\t\t\t\t\tParse Table\n\n")
    parse_table = generate_parse_table(terminals, non_terminals, grammar, grammar_first, grammar_follow)
    display_parse_table(parse_table, terminals, non_terminals)


#expr = input("Enter the expression ending with $ : ")
    expr = test_str

    print("\n\n\n\n\n\n")
    print("\t\t\t\t\t\t\tParsing Expression\n\n")
    parse(expr, parse_table, terminals, non_terminals)
