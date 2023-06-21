firstD = {}
followD = {}
eps = "Є"

def CaluclateFirst(start):
    first = set()

    for v in rules[start]:
        for each in v:
            if eps in first:
                first.remove(eps)

            if each in ter:
                first.add(each)

            elif each == eps:
                first.add(eps)

            elif each in non_ter:
                first = first.union(CaluclateFirst(each))

            if eps not in first:
                break


    firstD[start] = first
    return first


def CalculateFollow(start):
    follow = set()
    if start == start_symbol:
        follow.add("$")
    for k, r in rules.items():
        #print(start,'\t', r)
        for each in r:
            if start in each:
                index = each.index(start)
                if index != len(each)-1:
                    for i in range(index+1, len(each)):
                        if eps in follow:
                            follow.remove(eps)
                            followD[start] = follow
                        if each[i] in ter:
                            follow = follow.union(each[i])
                            followD[start] = follow
                        else:
                            follow = follow.union(firstD[each[i]])
                            followD[start] = follow
                        if eps not in follow:
                            break
                else:
                    if k not in followD:
                        follow = follow.union(CalculateFollow(k))
                        followD[start] = follow
                    else:
                        follow = follow.union(followD[k])
                        followD[start] = follow
                if eps in follow or len(follow) == 0:
                    if eps in follow:
                        follow.remove(eps)
                    follow = follow.union(CalculateFollow(k))
                    followD[start] = follow
    followD[start] = follow
    return follow


#input terminal symbols
# print("==========================================================================")
print("Enter terminals:")
ter = list(map(str, input().split()))
# print("==========================================================================")
#input non terminal symbols
print("Enter non terminals:")
non_ter = list(map(str, input().split()))
# print("==========================================================================")
#input start symbol
start_symbol = input("Enter the starting symbol: ")
# print("==========================================================================")
#input all production rules
no_of_productions = int(input("Enter no of productions: "))
productions = []
# print("==========================================================================")
print("Enter the production rules:")
for _ in range(no_of_productions):
    productions.append(input().replace("#", eps))

rules = {}
for p in productions:
    r = p.split("->")
    rules[r[0]] = r[1].split('|')
print(rules)


CaluclateFirst(start_symbol)


for start in non_ter:
    CaluclateFirst(start)
# print("==========================================================================")
print("\tFIRST SET COMPUTATION TABLE\n")
print("TERMINAL\t\t FIRST")
for F in sorted(firstD):
    print("  ",F,"\t:\t",firstD[F])


for start in non_ter:
    CalculateFollow(start)
# print("==========================================================================")
print("\n\tFOLLOW SET COMPUTATION TABLE\n")
print("TERMINAL\t\t FOLLOW")
for F in sorted(followD):
    print("  ",F,"\t:\t",followD[F])


def parsingTable(rules):
    for symbol, prod in rules.items():
        for each in prod:
            t = set()
            for e in each:
                if e in non_ter:
                    if eps in t:
                        t.remove(eps)
                    t = t.union(firstD[e])
                    if eps not in t:
                        break
                else:
                    t = t.union(e)
                    break
            if eps in t:
                t.remove(eps)
                t = t.union(followD[symbol])
            table[symbol].append([{symbol+'->'+each: t}])



table = dict()
for each in non_ter:
    table[each] = []

parsingTable(rules)
# print("==========================================================================")
print("\t\tParsing Table")
for row in table:
    print(row, table[row])
# print("==========================================================================")