import random

sentenceStructures = ["<*article*singular> <*noun*singular> was <*adjective*singular>","<*pronoun*singular> was <*adjective*singular>","<*noun*plural>"]
partsOfSpeech = {"article":{"singular":["the","that","this"],"plural":["those","these"]}, "noun": {"singular":["ball","cat","dog"], "plural":["balls","cats","dogs"]},"pronoun": {"singular":["it","he","she"], "plural":["they"]}, "adjective":{"singular":["happy","sad","disapointed",]}}
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
            sentence = sentence[0:i] + random.choice(partsOfSpeech[atributes[0]][atributes[1]]) + sentence[x+1:len(sentence)]
            tag = ""
            currentAtribute = ""
            atributes = []
    print(sentence)

print("suffer")
sentenceEditor(sentence)