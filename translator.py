import dictionary as dic
class Translator:

    def __init__(self,file_name):
        self.dizionario=dic.Dictionary(file_name)

    def printMenu(self):
        print(f"1. Aggiungi nuova parola\n2. Cerca una traduzione\n3. Cerca con wildcard\n4. Exit")
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit

    #def loadDictionary(self, dict):
       # dic.Dictionary(dict)
        # dict is a string with the filename of the dictionary


    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        campi= entry[1].strip().split()
        for i in campi:
            tupla = (entry[0], i)
            self.dizionario.addWord(tupla)

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        for chiave in self.dizionario.chiavi:
            if chiave == query.lower():
                return self.dizionario[chiave]


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        b = True
        risultato=[]
        for chiave in self.chiavi:
            i = 0
            for lettera in chiave:
                if i != chiave.lenght():
                    if lettera==chiave[i] or lettera=="?":
                        i+=1
                    else: b = False
                else: risultato.append(chiave)
        if risultato.lenght()==0:
            return f"Nessun Match"
        else:
         return risultato