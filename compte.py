class Compte:
    nb=0
    def __init__(self, numc, nomt, solde):
        self.__numc = numc
        self.__nomt = nomt
        self.__solde = solde
        self.__historique = []      # liste des opération
        Compte.nb=Compte.nb+1

    #_________________________getters & setters _________________
    def getNumc(self):
        return self.__numc

    def setNumc(self, num):
        self.__numc = num

    def getNomt(self):
        return self.__nomt

    def setNomt(self, nom):
        self.__nomt = nom

    def getSolde(self):
        return self.__solde

    def setSolde(self, solde):
        self.__solde = solde

    def getHistorique(self):
        return self.__historique

    #____________________les autres foncions __________________________
    def creer(self):
        self.__historique.append(f"Création du compte - Solde initial : {self.__solde} DH")

    def __str__(self):
        return "numero de compte: " + self.__numc + "\nnom titulaire: " + self.__nomt + "\nsolde de compte : " + str(self.__solde)
    

    def deposerArgent(self, montant):
        if montant > 0:
            self.__solde += montant
            self.__historique.append(f"Dépôt sur le compte - Solde actuel : {self.__solde} DH")
            return self.__solde
        else : 
            print("le montant doit être positif !")
            return self.__solde
            
    def retirerArgent(self, montant):
        if montant > 0 and self.__solde >= montant:
            self.__solde -= montant
            self.__historique.append(
                f"Retrait : -{montant} DH | Solde actuel : {self.__solde} DH"
            )
        else:
            print("Solde insuffisant ou montant invalide.")

    def virement (self, compteDestination, montant):
        if self.__solde >= montant and montant > 0:
            self.__solde -= montant
            compteDestination.deposerArgent(montant)
            # Historique du compte émetteur
            self.__historique.append(f"Virement envoyé : -{montant} DH vers le compte {compteDestination.getNumc()} | Solde actuel : {self.__solde} DH")
            # Historique du compte destinataire
            compteDestination._Compte__historique.append(f"Virement reçu : +{montant} DH depuis le compte {self.getNumc()} | Solde actuel : {compteDestination.getSolde()} DH")

            print(f"Transfert de {montant} DH effectué avec succès.")

        else:
            print("votre solde est insufisant !")


    def consultersolde(self):
        print(f"votre solde : {self.__solde}")
        
    
    def historiqueOperation(self):
        print("Historique des opérations :")
        for op in self.__historique:
            print(op)

class gestioncompte:
    def __init__(self):
        self.__comptes=[]

    def getComptes(self):
        return self.__comptes
    
    def ajouterCompte(self, c):
        if self.chercherCompte(c.getNumc()):
            print("Ce numéro de compte existe déjà.")
        else:
            self.__comptes.append(c)
    

    def afficher(self):
        print("\n=========== Liste des compte ========")
        for c in self.__comptes:
            print("les informations du compte : ")
            print(c)
            print("\n")

    def chercherCompte(self, num):
        for c in self.__comptes:
            if c.getNumc() == num:
                return c
        return None

        
    def afficheMenu(self):
            print (" =====================================")
            print ("     système bancaire simplifié    ")
            print (" =====================================")
            print (" 1• création du compte ")
            print (" 2• diposer un montant ")
            print (" 3• retrait du montant ")
            print (" 4• virement ")
            print (" 5• Consultation du solde ")
            print (" 6• Afficher la liste des comptes existent ")
            print (" 7• afficher l'historique des opeartions ")
            print (" 8• quitter ")
            print (" =====================================")
if __name__=="main":
    g=gestioncompte()

    while True :

        g.afficheMenu()
        choix=int(input(" votre choix :"))
        
        match choix:
            case 1:
                num = int(input("entrer le numero de compte à créer"))
                nom =input("entrer le nom de compte à créer")
                solde = float(input("entrer le solde de compte à créer"))

                c = Compte(num, nom, solde)

                c.creer()
                g.ajouterCompte(c)

            case 2:
                num = str(input("Entrer le numéro du compte pour déposer l'argent  : "))
                compte = g.chercherCompte(num)
            
                if compte:
                    montant = float(input("Entrer le montant : "))
                    compte.deposerArgent(montant)
                else:
                    print("Compte introuvable.")

            case 3:
                num = str(input("Entrer le numéro du compte pour retirer l'argent : "))
                compte = g.chercherCompte(num)
                if compte:
                    montant = float(input("Entrer le montant : "))
                    compte.retirerArgent(montant)
                else:
                    print("Compte introuvable.")

            case 4:
                numSource = input("Numéro du compte source : ")
                source = g.chercherCompte(numSource)

                numDest = input("Numéro du compte destinataire : ")
                destination = g.chercherCompte(numDest)

                if source and destination:
                    montant = float(input("Montant : "))
                    source.virement(destination, montant)
                else:
                    print("Compte introuvable.")

            case 5:
                num = str(input("Entrer le numéro du compte pour consulter le solde : "))
                compte = g.chercherCompte(num)

                if compte:
                    compte.consultersolde()
                else:
                    print("Compte introuvable.")


            case 6:
                print(f"le nombre totale de comptes creer est : {Compte.nb}")
                g.afficher()

            case 7:
                num = str(input("Entrer le numéro du compte : "))
                compte = g.chercherCompte(num)
                if compte:
                    compte.historiqueOperation()
                else:
                    print ("compte introuvable.")
            case 8:
                break
            case _:
                print("choix invalide ")
                break
