# -EDM5240-devoir-1.

#coding: utf-8

permis = list(range(30000,99999+1,1)) # Pas besoin d'écrire «,1» à la fin; un «range» est construit, par défaut, par sauts de 1
print(permis)

permis2 = list(range(00000,18000,1))
print(permis2)

# Tu as bien créé deux listes de nombres correspondant aux numéros de permis possibles du Collège des médecins.
# Sauf pour l'infâme décennie 2000 à 2009 où il manque les zéros précédant les numéros qu'on cherche.

# Une des façons d'y arriver est de faire une liste qui va de 2000 à 2017:

annees = list(range(2000,2018))

# Puis de faire une boucle afin de convertir chaque année en chaîne de caractères, pour ensuite ne conserver que les deux derniers caractères (avec 2002, par exemple, on obtient ainsi 02):

for annee in annees:
	codeDeDeuxChiffres = str(annee)[2:]
	# print(codeDeDeuxChiffres) # J'ai imprimé ma variable pour vérifier; ça marche

# Après, on utilise la même technique pour les trois derniers chiffres des numéros de permis avec, une façon parmi d'autres, une liste qui va de 1000 à 1999:

num = list(range(1000,2000))

# Puis, à l'aide d'une deuxième boucle, on peut convertir chacun des nombres qu'elle contient en chaîne de caractères et de ne conserver que les 3 derniers caractères, transformant ainsi 1001 en 001, par exemple

for n in num:
	codeDeTroisChiffres = str(n)[1:]
	# print(codeDeTroisChiffres) # Autre vérification. Succès!

# Pour coller les deux ensemble, on peut imbriquer la 2e boucle dans la première, ainsi:

for annee in annees:
	codeDeDeuxChiffres = str(annee)[2:]
	for n in num:
		codeDeTroisChiffres = str(n)[1:]
		numeroDePermis = codeDeDeuxChiffres + codeDeTroisChiffres
		print(numeroDePermis)

# Pour couvrir de 1930 à 2017, on peut changer le «range» de notre liste années : list(range(1930,2018)) et bingo!