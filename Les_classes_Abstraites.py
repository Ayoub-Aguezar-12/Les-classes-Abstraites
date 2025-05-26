from abc import ABC, abstractmethod

class Vehicule(ABC):
    def __init__(self, marque, modele, annee, kilometrage, en_panne=False):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
        self.en_panne = en_panne
    
    @abstractmethod
    def type_vehicule(self):
        pass
    
    @abstractmethod
    def calculer_prix_reparation(self):
        pass
    
    def afficher_info(self):
        return (f"{self.type_vehicule()} {self.marque} {self.modele} ({self.annee}) - "
                f"Kilométrage: {self.kilometrage} km - "
                f"En panne: {'Oui' if self.en_panne else 'Non'}")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, kilometrage, nb_portes, en_panne=False):
        super().__init__(marque, modele, annee, kilometrage, en_panne)
        self.nb_portes = nb_portes
    
    def type_vehicule(self):
        return "Voiture"
    
    def calculer_prix_reparation(self):
        return 200 + (50 * self.nb_portes)

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, kilometrage, cylindree, en_panne=False):
        super().__init__(marque, modele, annee, kilometrage, en_panne)
        self.cylindree = cylindree
    
    def type_vehicule(self):
        return "Moto"
    
    def calculer_prix_reparation(self):
        return 150 + (0.1 * self.cylindree)

class Camion(Vehicule):
    def __init__(self, marque, modele, annee, kilometrage, charge_max, en_panne=False):
        super().__init__(marque, modele, annee, kilometrage, en_panne)
        self.charge_max = charge_max
    
    def type_vehicule(self):
        return "Camion"
    
    def calculer_prix_reparation(self):
        return 500 + (100 * self.charge_max)

class Reparation:
    def __init__(self, vehicule, description, duree_heures, terminee=False):
        self.vehicule = vehicule
        self.description = description
        self.duree_heures = duree_heures
        self.terminee = terminee
    
    def calculer_cout(self):
        return self.vehicule.calculer_prix_reparation() + (50 * self.duree_heures)
    
    def afficher_details(self):
        return (f"Réparation pour {self.vehicule.afficher_info()}\n"
                f"Description: {self.description}\n"
                f"Durée: {self.duree_heures} heures\n"
                f"Coût total: {self.calculer_cout()}€\n"
                f"Statut: {'Terminée' if self.terminee else 'En cours'}")

if __name__ == "__main__":
    voiture = Voiture("Toyota", "Corolla", 2020, 45000, 5, True)
    moto = Moto("Yamaha", "MT-07", 2019, 12000, 700)
    camion = Camion("Volvo", "FH16", 2018, 150000, 20)
    
    rep1 = Reparation(voiture, "Changement courroie de distribution", 3)
    rep2 = Reparation(moto, "Révision complète", 2, True)
    rep3 = Reparation(camion, "Remplacement freins arrière", 5)
    
    print("=== Détails des réparations ===")
    print(rep1.afficher_details())
    print(rep2.afficher_details())
    print(rep3.afficher_details())
    
    vehicules = [voiture, moto, camion]
    print("\n=== Véhicules en panne ===")
    for v in vehicules:
        if v.en_panne:
            print(v.afficher_info())
