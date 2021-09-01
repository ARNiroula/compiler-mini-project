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
    # print(dictionary)
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
    print("\t\t\t\t",end = "")
    for terminal in terminals:
        print(terminal+"\t\t", end = "")
    print("\n\n")
    
    for non_terminal in non_terminals:
        print("\t\t"+non_terminal+"\t\t", end = "")
        for terminal in terminals:
            print(parse_table[non_terminals.index(non_terminal)][terminals.index(terminal)]+"\t\t", end = "")
        print("\n")

