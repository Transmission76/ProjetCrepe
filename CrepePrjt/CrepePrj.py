from os import system

print("\n\n\t\t\t\t\033[1;34;49m=== Projet - Crepe's Store ===\033[0;37;49m\n\n")

# Declare variables
list_crepe =[{"nom":"Crepe Bonanza",
                "prix":25.99,
                "type":"Salée"},
             
             {"nom":"Crepe Confiture de Pomme",
                "prix":3.99,
                "type":"Sucrée"},
             
             {"nom":"Crepe Jambon & Fromage",
                "prix":16.99,
                "type":"Salée"},
             
             {"nom":"Crepe Salade Cesar",
                "prix":48.99,
                "type":"Salée"}]
 
 
list_crepeType = ["Salé", "Sucré","Végetarien"]

list_ingreSalty = [{"nom":"Jambon",
                    "prix":5.99},
                   
                  {"nom":"Poulet",
                    "prix":5.99},

                  {"nom":"Fromage",
                   "prix":1.99}]

list_ingreSweet = [{"nom":"Confiture de Fraises",
                    "prix":12.99},
                  
                  {"nom":"Confiture de Pommes",
                    "prix":775.99},
                    
                  {"nom":"Sucre",
                    "prix": 700}]

list_ingreVege = [{"nom" :"Tomates",
                    "prix": 6.99},
                    
                    {"nom":"Onions",
                    "prix": 4.99},
                    
                    {"nom": "Brocoli",
                    "prix":3.99}]



# Functions                       
def showList_alpha(): # Show crepes by alphabeticalby. checking every character (len) in the list. then uses tri_selection function and prints variables in order.
    
    print ("\n\n\t\033[1;34;49m La liste de crêpes par ordre alphabétique (croissant): ")

    nm = 1
    for i in range (len(list_crepe)):
        tri_selectionUp(list_crepe,"nom")
        print ("\t\t\033[0;33;49m", nm,". ",list_crepe[i]["nom"],list_crepe[i]["prix"],list_crepe[i]["type"])
        nm += 1

    print ("\n\n")
    
    

def showList_price(): # Show crepes by price (Cheapest to Most Expensive.) by checking every character (len) in the list. then uses tri_selection function and prints variables in order.
    
    print ("\n\n\t\033[1;34;49m La liste de crêpes par prix croissant : ")

    nm = 1        
    for i in range (len(list_crepe)):
        tri_selectionDown(list_crepe,"prix")
        print ("\t\t\033[0;33;49m", nm,". ",list_crepe[i]["nom"],list_crepe[i]["prix"],list_crepe[i]["type"])
        nm += 1

    print ("\n\n")




def showList_expen(): # Show crepes most expensive by checking every character (len) in the list. then uses tri_selection function and prints variables in order.
    tri_selectionDown(list_crepe,"prix")
    
    print ("\n\n\t\033[1;34;49m Crêpe la plus chère : ")
      

    print ("\t\t\033[0;33;49m",list_crepe[0]["nom"],list_crepe[0]["prix"],list_crepe[0]["type"])
    print ("\n\n")



def showList_cheap(): # Show the cheapest Crepes by checking every character (len) in the list. then uses tri_selection function and prints variables in order.
    tri_selectionUp(list_crepe,"prix")
    
    print ("\n\n\t\033[1;34;49m Crêpe la moins chère : ")
      

    print ("\t\t\033[0;33;49m",list_crepe[0]["nom"],list_crepe[0]["prix"],list_crepe[0]["type"])
    print ("\n\n")


def tri_selectionUp(tab,arg): #all tri_selection functions are similar. Only difference is that each one sorts in a different manner.
    for i in range (len(tab)):
       
      # Find min by checking the variables i and j, i+1 exists to compare each caractere in the variable and comparing it with j. if i is bigger than j; then j becomes the new min (the smallest variable)
        min = i
        for j in range (i+1, len(tab)):
           if tab[min][arg] > tab[j][arg]:
               min = j
        
        #Exchange between tab[i] and tab[min]. tmp exists to stock the variables to exchange them temporarly.      
        tmp = tab[i]
        tab[i] = tab[min]
        tab[min] = tmp
    return tab



def tri_selectionDown(tab,arg):
    for i in range (len(tab)):
       
      # Find min by checking the variables i and j, i+1 exists to compare each caractere in the variable and comparing it with j. if i is bigger than j; then j becomes the new min (the smallest variable)
        min = i
        for j in range (i+1, len(tab)):
           if tab[min][arg] < tab[j][arg]:
               min = j
        
        #Exchange between tab[i] and tab[min]. tmp exists to stock the variables to exchange them temporarly.      
        tmp = tab[i]
        tab[i] = tab[min]
        tab[min] = tmp
    return tab

def tri_bubble(tab,arg):
    n = len(tab)
    # Traverser tous les éléments du tableau
    for i in range(n):
         for j in range(0, n-i-1):
             
            # Échanger si l'élément trouvé est plus grand que le suivant
            if tab[j][arg] > tab[j+1][arg] :
                tab[j], tab[j+1][arg] = tab[j+1][arg], tab[j][arg]
    return tab



def persoCrepe(): #allows user to choose different ingredients from the list inside the type they chose.

    crepeIngredients = []
    crepeType = ""
    crepePrice = 0.0
    
    while crepeType != "Salé" and crepeType != "Sucrée" and crepeType != "Végé" :
        crepeType = input("Voulez vous une crepe Salé, Sucrée ou Végé?: (cancel)\t\t")  
        if crepeType == "cancel": return

#as long as smthElse is true, repeat the crepetype loop. If any of the variables the user inputs are not equal to the ones declared in the loop, repeat the loop. if yeet = non then break loop.
    smthElse = True   
    if crepeType == "Salé":
        while smthElse:
            ingr = ""
            while ingr != "Jambon" and ingr != "Poulet" and ingr != "Fromage":
                ingr = input("Ingrédients: Jambon, Poulet, Fromage: (cancel)\t\t") 
                if ingr == "cancel": return
            crepeIngredients.append(ingr)
            yeet = ""
            while yeet != "Oui" and  yeet != "Non":
                yeet = input("Voulez-vous un/des autre(s) ingrédients (Oui/Non)\t\t")
            smthElse = True if yeet == "Oui" else False 
    elif crepeType == "Sucrée":
        while smthElse:
            ingr = ""
            while ingr != "Confiture de Fraises" and ingr != "Confiture de Pommes" and ingr != "Sucre":
                ingr = input("Ingrédients: Confiture de Fraises, Confiture de Pommes, Sucre: (cancel)\t\t")
                if ingr == "cancel": return
            crepeIngredients.append(ingr)
            yeet = ""
            while yeet != "Oui" and  yeet != "Non":
                yeet = input("Voulez-vous un/des autre(s) ingrédients (Oui/Non)\t\t")
            smthElse = True if yeet == "Oui" else False 
    else:
        while smthElse:
            ingr = ""
            while ingr != "Tomates" and ingr != "Onions" and ingr != "Brocoli":
                ingr = input("Ingrédients: Tomates, Onions, Brocoli: (cancel)\t\t")
                if ingr == "cancel": return
            crepeIngredients.append(ingr)
            yeet = ""
            while yeet != "Oui" and  yeet != "Non":
                yeet = input("Voulez-vous un/des autre(s) ingrédients (Oui/Non)\t\t")
            smthElse = True if yeet == "Oui" else False 

    crepeIngredients = list(set(crepeIngredients))      #declares function as a list then utilises set( ) function to disable any duplicates inputed by user 

    if crepeType == "Salé":
        for i in range(len(crepeIngredients)):
            if crepeIngredients[i] == "Jambon":
                crepePrice += list_ingreSalty[0]["prix"]
            elif crepeIngredients[i] == "Poulet":
                crepePrice += list_ingreSalty[1]["prix"]
            else:
                crepePrice += list_ingreSalty[2]["prix"]
    elif crepeType == "Sucrée":
        for i in range(len(crepeIngredients)):
            if crepeIngredients[i] == "Confiture de Fraises":
                crepePrice += list_ingreSweet[0]["prix"]
            elif crepeIngredients[i] == "Confiture de Pommes":
                crepePrice += list_ingreSweet[1]["prix"]
            else:
                crepePrice += list_ingreSweet[2]["prix"]
    else:
        for i in range(len(crepeIngredients)):
            if crepeIngredients[i] == "Tomates":
                crepePrice += list_ingreVege[0]["prix"]
            elif crepeIngredients[i] == "Onions":
                crepePrice += list_ingreVege[1]["prix"]
            else:
                crepePrice += list_ingreVege[2]["prix"]

    print ("\t\t\033[0;33;49m","Crepe Personalisée:" ,', '.join(crepeIngredients), crepeType, crepePrice)

    
while True:
    try:
        choice = int(input("\n\t\033[0;37;49m Afficher la liste de crêpes par ordre alphabétique \033[1;35;49m (Tapez 1)"
                          " \n\t\033[0;37;49m Afficher la liste de crêpes par prix croissant \033[1;35;49m (Tapez 2)"
                          " \n\t\033[0;37;49m Afficher la crêpe la plus chère \033[1;35;49m (Tapez 3) "
                           "\n\t\033[0;37;49m Afficher la crêpe la moins chère \033[1;35;49m (Tapez 4)"
                           "\n\t\033[0;37;49m Personaliser votre crepe \033[1;35;49m (Tapez 5)"
                           "\n\n\t\033[0;37;49m Terminer la liste \033[1;35;49m (Tapez 6) \t\t\t"))
        
        if choice == 1 :    # Show crepes by alphabetical
            showList_alpha()
            
        elif choice == 2 :  # Show crepes by price (Cheapest to Most Expensive.)
            showList_price()
            
        elif choice == 3 :  # Show crepes most expensive
            showList_expen()

        elif choice == 4 :  # Show the cheapest Crepes
            showList_cheap()
        
        elif choice == 5:
            persoCrepe()

        elif choice == 6:   # Close Menu
            print ("\t\t\t\033[1;31;49m Achats terminés\n\n")
            system("pause")
            print ("\033[0;37;49m")
            break
        
        else :
            print("\t\t\t\033[1;31;49m Saisie Invalide, veuillez réessayer :\n\n")


    except ValueError:
        print("\t\t\t\033[1;31;49m Saisie Invalide, veuillez réessayer :\n\n")