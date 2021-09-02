from utils import get_rule
from texttable import Texttable

def generate_parse_table(terminals, non_terminals, grammar, grammar_first, grammar_follow):
    parse_table = [[""]*len(terminals) for i in range(len(non_terminals))]
    
    for non_terminal in non_terminals:
        for terminal in terminals:
            if terminal in grammar_first[non_terminal]:
                rule = get_rule(non_terminal, terminal, grammar, grammar_first)
                
            elif("`" in grammar_first[non_terminal] and terminal in grammar_follow[non_terminal]):
                rule = non_terminal+"~`"
                
            else:
                rule = ""

            parse_table[non_terminals.index(non_terminal)][terminals.index(terminal)] = rule

    return(parse_table)

def parse(expr, parse_table, terminals, non_terminals):
    original=expr
    stack = ["$"]
    stack.insert(0, non_terminals[0])

    table = Texttable(max_width=0)
    table.header(['Matched', 'STACK', 'INPUT', 'ACTION'])
    table.add_row(['-', ''.join(stack), expr, '-'])

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
                if(len(action)==0):
                    flag = False
                    break
                stack.pop(0)            
                i = 0
                flag=False
                for item in action[2:]:
                    if(item != "`"):
                        stack.insert(i,item)
                    i+=1

            table.add_row([matched, ''.join(stack), expr, action])
        except:
            flag = False
            break
    print(table.draw())
    if flag:
        print("\n\nInput expression '{input}' is accepted.".format(input=original[:-1]))
    else:
        print("\n\nInput expression '{input}' is NOT accepted.".format(input=original[:-1]))
