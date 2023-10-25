import random

sentenceStructures = ["The <*noun> was <*adjective>","<*pronoun> was <*adjective>","<*noun*plural>"]
partsOfSpeech = {"noun":["ball","cat","dog"],"pronoun":["it","he","she","they"], "adjective":["happy","sad","disapointed",]}
sentence = random.choice(sentenceStructures)
atributes = []

def sentenceEditor(sentence):
    atributes = []
    tag = ""
    x = 0
    i = -1
    while i < len(sentence):
        i += 1
        #find tags
        try:
            if sentence[i] == "<":
                x = i
                while sentence[x] != ">":
                    x += 1
                tag = sentence[i:x+1]
        except:
            break
        print(tag)
        #find atributes
        if tag != "":
            #identify atributes
            currentAtribute = ""
            for y in range(len(tag)):
                if tag[y] == "*":
                    y += 1
                    while tag[y] not in ["*",">"]:
                        currentAtribute += tag[y]
                        y += 1
                    atributes.append(currentAtribute)
                    currentAtribute = ""
            sentence = sentence[0:i] + random.choice(partsOfSpeech[atributes[0]]) + "s" if sentence[-1] in ["a","e","i","o","u"] else "es" if "plural" in atributes else "" + sentence[x+1:len(sentence)]
            print(atributes)
            print(random.choice(partsOfSpeech[atributes[0]]))
            print("-"+sentence[0:i]+"-")
            print("-"+sentence[x:len(sentence)]+"-")
            tag = ""
            currentAtribute = ""
            atributes = []

print("suffer")
sentenceEditor(sentence)