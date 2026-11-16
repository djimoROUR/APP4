Séance 2 : 
Analyse syntaxique : transformer la liste de token en arbre
Analyse sémantique : prend les arbres et 
Génération de code : prend les arbres et les transforme en code machine

Comment on représente ces arbres ? => on fait une structure struct Node
- chaque noeud de l'arbre va avoir un type (on va faire une énumération de tous les types possibles
- /ce qu'on a fait pour les token)

struct Node {
    int type
    int valeur  //ex : on va créer un type de noeud constante, donc on transférera la valeur du token dans le noeud
    string ident
    int ligne 
    int colonne //infos sur la position dans le code : ligne/colonne
    int nbEnfant // ce qui différencie les noeuds des tokens : les arbres ont des enfants
    Node enfants[] //on mets un vecteur 
}
-> préfixé avec nd (on utilisait tkn pour les token)

Constructeurs : 

Node node(int type)
Node node_v(int type, int valeur)
node_i(int type, string ident)
node_1(int type, Node e1)
node_2(int type, Node e1 e2)

ajouter_enfant(Node P,Node e)

Types de noeuds : Token et Noeud (noeud +,-). Ne pas réutiliser la même énumération !!
Exemple : on a le token -, mais est-ce qu'on a le noeud - ? Non ! On a le noeud binaire 3 -1 et unaire (-5)

Maintenant qu'on a les arbres, on peut mettre en place le compilateur
Pseudo compilateur : 
main (){

    init() //initialiser l'analyseur lexical
    while(courant type!= TOK_EOS){
        gencode(); // prend du code en entrée et donne en sortie du code assembleur 
    }
}

Gencode doit commencer par avoir un arbre sur lequel il va commencer par produire du code
gencode(){
    Node A = AnaSem() //déclare un arbre A (complet) en demandant à l'analyseur sémantique
    .......
}

Node AnaSem(){
    //Ne prend rien en paramètre mais renvoie un arbre 
    Node A =  AnaSynt();//  Donne le prochain arbre qu'il trouve dans le code
    return A;
}

Node AnaSynt(){
    //C'est lui qui construit l'arbre, et à la fin, le renvoie
    // il le fabrique en fonction des tokens qu'il reçoit de l'ana lexical
    ......
   //prendre le texte sous forme de token et créer les arbres
}

Règles : 
F -> Instruction (I)
I -> Expression (E)
E ->  E + E / E -E / 

            A   


