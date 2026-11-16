# 📋 Contraintes du projet (Compilateur)

### 🚫 Fonctionnalités du langage interdites
* **Pas de `switch`**
* **Pas de structures** (`struct`, `class`)
* **Pas de types complexes** : le langage ne gère **que les entiers** (`int`) et les **fonctions**.
* **Pas d'opérateurs d'incrémentation/décrémentation** (`++`, `--`) — *sauf mention contraire ou extension autorisée*.

### ⚙️ Exigences de compilation et sortie
* **Production de binaire** : Le compilateur doit produire un programme binaire en sortie, strictement équivalent au programme source fourni.

### ⚠️ Gestion des erreurs (Strict)
* **Interdiction de compiler en cas d'erreur** : Si le programme d'entrée est incorrect, le processus de génération du binaire doit être immédiatement stoppé.
* **Détection active** : Le compilateur doit détecter toutes les erreurs syntaxiques et sémantiques.
* **Rapport d'erreur** : En cas d'échec, le compilateur doit afficher un message d'erreur clair accompagné d'une indication pour résoudre le problème.
