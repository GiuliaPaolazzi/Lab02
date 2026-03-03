class Dictionary:
    def __init__ (self,file_name= "dictionary.txt"):
        self.file_name=file_name
        self.dizionario={}
        self.chiavi=[]
        try:
            with open (file_name,"r", encoding="utf-8") as f:
                for riga in f:
                    campi=riga.strip().split(" ")
                    aliena=campi[0].lower()
                    umana=campi[1].lower()
                    umane=[]
                    umane.append(umana)
                    self.dizionario[aliena]=umane
                    self.chiavi.append(aliena)
        except FileNotFoundError:
            ...

    def addWord(self, campi):
        aliena = campi[0].lower()
        umane = campi[1].lower().strip().split()
        if aliena.isalpha() and campi[1].isalpha():
            if aliena in self.dizionario:
                self.dizionario[aliena].append(umane)
            else:
                self.dizionario[aliena]=umane


    def translate(self, aliena):

        return self.dizionario.get(aliena.lower(),"parola non trovata")

    def translateWordWildCard(self):
        pass