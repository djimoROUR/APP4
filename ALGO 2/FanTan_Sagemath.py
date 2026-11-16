G = DiGraph()
G.add_vertex((3,3))
d_vu = {(3,3) : False}                  # dictionnaire des sommets déjà traités
new = True
while new:
    new = False                         # a-t'on ajouté des sommets ?
    for (a,b) in G.vertices():
        if d_vu[(a,b)] == False :       # si un sommet est non traité
            d_vu[(a,b)] = True          # maintenant il le sera
            L = [(a-1, b), (a-2,b), (a,b-1), (a, b-2)]  # tous les possibles
            for (c,d) in L:
                if c>=0 and d>=0 :
                    M = max(c,d)
                    m = min(c,d)
                    if (M,m) not in G.vertices():
                        G.add_vertex((M,m))
                        d_vu[(M,m)] = False
                        new = True
                    if ((a,b),(c,d)) not in G.edges() and ((a,b),(d,c)) not in G.edges():
                        G.add_edge(((a,b),(M,m)))

G.show(vertex_size=1000, dist = 50)