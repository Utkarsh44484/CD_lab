def First(start):
    first = set()
    for i in production_rhs[start]:
        for char in i:
            if('#' in first):
                first.remove('#')
            if char in terminal:
                first.add(char)
            elif char in nonTerminal:
                first = first.union(First(char))
            elif char == '#':
                first.add(char)
            if '#' not in first:
                break

    # Printing
    dict[start] = first
    return first

terminal=[]
nonTerminal=[]
production=[]
dict=dict()

terminal = list(input("Enter Terminals :").split())
nonTerminal = list(input("Enter Non Terminals :").split())

# print(terminal,'\n',nonTerminal)

p = int(input("Enter No. of production rules :"))
for i in range(p):
    production.append(input())

start_symb = input("Enter start Symbol :")
production_rhs = {}
for i in production :
    rhs = i.split("->")
    production_rhs[rhs[0]] = rhs[1].split('|')

# print(production_rhs)
First(start_symb)
print(dict)