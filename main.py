from collections import OrderedDict
from utils import show_dict, isterminal, display_parse_table, insert
from first import first
from follow import follow
from ll1 import generate_parse_table, parse

DEBUG_MODE = True

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


    non_terminals = list(grammar.keys())
    terminals = []

    for i in grammar:
        for rule in grammar[i]:
            for char in rule:
                
                if(isterminal(char) and char not in terminals):
                    terminals.append(char)

    terminals.append("$")

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
