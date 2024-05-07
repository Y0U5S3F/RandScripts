def bfs(graph, start, end):
    file = [[start]]# initialisation file
    while file:#tant que file nest pas vide
        chemin = file.pop(0)#premier element de la file
        element = chemin[-1]#dernier noeud du chemin
        if element == end:
            return chemin#si on est a end(qui est 5,5), on retourne le chemin(on est a la fin cbn)
        for adjacent in graph.get(element, []):#pour chaque noeud current ou voisin
            nvchemin = list(chemin)#un nouveau chemin en ajoutant le noeud voisin au chemin current
            nvchemin.append(adjacent)
            file.append(nvchemin)#ajouter le nouveau chemin a file

#graph
graph = {
   (1,1): [(1,2),(2,1)],
   (1,2): [(1,1),(1,3)],
   (1,3): [(1,2),(1,4),(2,3)],
   (1,4): [(1,3),(2,4)],
   (1,5): [(2,5)],
   (2,1): [(1,1),(2,2)],
   (2,2): [(2,1),(3,2),(2,3)],
   (2,3): [(2,2),(1,3)],
   (2,4): [(1,4),(2,5)],
   (2,5): [(1,5),(2,4),(3,5)],
   (3,1): [(3,2),(4,1)],
   (3,2): [(2,2),(3,1),(3,3)],
   (3,3): [(3,2),(3,4)],
   (3,4): [(3,3),(4,4),(4,5)],
   (3,5): [(3,4),(2,5)],
   (4,1): [(3,1),(4,2),(5,1)],
   (4,2): [(4,1),(4,3)],
   (4,3): [(4,2),(4,4),(5,3)],
   (4,4): [(3,4),(4,3),(4,5)],
   (4,5): [(4,4),(5,5)],
   (5,1): [(4,1),(5,2)],
   (5,2): [(5,1),(5,3)],
   (5,3): [(5,2),(4,3),(5,4)],
   (5,4): [(5,3),(5,5)],
   (5,5): [(4,5),(5,4)],
}

#declaration debut et fin
start = (1,1)
end = (5,5)
#on utilise bfs car elle est par une file
chemin = bfs(graph, start, end)
#affichage
print(f"chemin de {start} to {end} est {chemin}")