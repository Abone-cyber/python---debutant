class Eleve:
    def __init__(self, nom):
        self.nom = nom
        self.notes = []

    def ajouter_note(self, note):
        self.notes.append(note)
        
    def moyenne(self):
        if self.notes:
            return sum(self.notes) / len(self.notes)
        return 0
    
    def __str__(self):
        notes_str = ", ".join(str(n) for n in self.notes)
        return f"{self.nom} : {notes_str} | Moyenne : {self.moyenne(): .2f}"


