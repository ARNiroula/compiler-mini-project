from utils import get_rule

def generate_parse_table(terminals, non_terminals, grammar, grammar_first, grammar_follow):
    parse_table = [[""]*len(terminals) for i in range(len(non_terminals))]
    
    for non_terminal in non_terminals:
        for terminal in terminals:
            if terminal in grammar_first[non_terminal]:
                rule = get_rule(non_terminal, terminal, grammar, grammar_first)
                
            elif("`" in grammar_first[non_terminal] and terminal in grammar_follow[non_terminal]):
                rule = non_terminal+"~`"
                
            elif(terminal in grammar_follow[non_terminal]):
                rule = "Sync"
                
            else:
                rule = ""
                
            parse_table[non_terminals.index(non_terminal)][terminals.index(terminal)] = rule

    return(parse_table)

def parse(expr, parse_table, terminals, non_terminals):
    original=expr
    stack = ["$"]
    stack.insert(0, non_terminals[0])

    orig_expr = expr+""

    print("\t\t\tMatched\t\t\tStack\t\t\tInput\t\t\tAction\n")
    print("\t\t\t-\t\t\t", end = "")
    for i in stack:
        print(i,  end = "")
    print("\t\t\t", end = "")
    print(expr+"\t\t\t", end = "")
    print("-")

    matched = "-"
    while(True):
        action = "-"
        try:
            if(stack[0] == expr[0] and stack[0] == "$"):
                flag=True
                break
            elif(stack[0] == expr[0]):
                if(matched == "-"):
                    matched = expr[0]
                else:    
                    matched = matched + expr[0]
                action = "Matched "+expr[0]
                expr = expr[1:]
                stack.pop(0)
            else:
                action = parse_table[non_terminals.index(stack[0])][terminals.index(expr[0])]
                stack.pop(0)            
                i = 0
                flag=False
                if action=='Sync':
                    stack=['$']
                    flag=True
                for item in action[2:]:
                    if flag:
                        action='Matched $'
                        break
                    if(item != "`"):
                        stack.insert(i,item)
                    i+=1

            print("\t\t\t"+matched+"\t\t\t", end = "")
            for i in stack:
                print(i,  end = "")
            print("\t\t\t", end = "")
            print(expr+"\t\t\t", end = "")
            print(action)
        except:
            flag = False
            break

    if flag:
        print("\n\nInput '{input}' is accepted".format(input=original[:-1]))
    else:
        print("\n\nInput '{input}' is not accepted".format(input=original[:-1]))
