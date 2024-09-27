lonr = [1, 2, 3] # henter inn data, definerer l

def my_sum(l : list) -> int:
    """ my-sum summer tall i en liste med tall """
    total = 0
    for elt in l:
        total += elt # total = total + elt
    return total

# Kombinere strenger og tall i print-funksjonen
print("Summen er:", my_sum(lonr))

# Referere til variabler i print-funksjonen (formattert output)
print(f'Summen av tallene i liste {lonr} er:', my_sum(lonr))


""" dette er et kommentar over flere linjer

# Implementasjon i Pyret
fun my-sum(l):
    case (List) l:
      | empty => 0
      | link(f, r) => f + my-sum(r)
    end
end
    
slutt på kommentar over flere linjer """