import os

liste1 = os.listdir("data_storing/database")

liste2 = ["2.h5", "3.h5"]

gemeinsame_elemente = set(liste1) & set(liste2)

# Entfernen der gemeinsamen Elemente aus beiden Listen
liste1 = [element for element in liste1 if element not in gemeinsame_elemente]
print("Liste 1 nach Entfernung:", liste1)
