from collections import OrderedDict
from utils import show_dict, isterminal, display_parse_table, insert
from first import first
from follow import follow
from ll1 import generate_parse_table, parse

if __name__ == "__main__":
    grammar = OrderedDict()
    grammar_first = OrderedDict()
    grammar_follow = OrderedDict()

    file_path = input("Enter file path, relative to the main.py\n")
    # file_path = "grammar.txt"

    test_str = str(
        input("Enter test string, terminals seperated by space and appending $ eg abbcc\n"))
    # test_str = "abbcc"
    test_str=test_str+'$'
    print()

    f = open(file_path)
    for i in f:
        i = i.replace("\n", "")
        lhs = ""
        rhs = ""
        flag = 1
        for j in i:
            if(j=="~"):
                flag = (flag+1)%2
                continue
            if(flag==1):
                lhs += j
            else:
                rhs += j
        grammar = insert(grammar, lhs, rhs)
        grammar_first[lhs] = "null"
        grammar_follow[lhs] = "null"

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
