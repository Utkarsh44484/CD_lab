hinglish = {
    "What": "क्या",
    "Where": "कहां",
    "are": "हैं",
    "is": "है",
    "you": "तुम",
    "he": "वह",
    "I": "मैं",
    "going": "जा रहे",
    "am": "हूँ",
}

pronoun = ["you", "I", "he"]
que = ["What", "Where"]
verb = ["is", "are", "am"]
object = ["going"]

def reader():
    print("===================================================================")
    sentence = input("Enter the sentence to be translated: ")
    tokens = sentence.split()
    return tokens


def translate(s):
    tr = []
    strr = []
    vtr = []
    otr = []
    for i in s:
        if (i in hinglish):
            if (i in pronoun or i in que):
                strr.append(hinglish[i])
            elif (i in verb):
                vtr.append(hinglish[i])
            else:
                otr.append(hinglish[i])
    for i in strr:
        tr.append(i)
    for i in otr:
        tr.append(i)
    for i in vtr:
        tr.append(i)
    return tr


# Main
sent = reader()
trd = translate(sent)
print("===================================================================")
print("Translated sentence :")
for i in trd:
    print(i, end=" ")
print("\n===================================================================")
