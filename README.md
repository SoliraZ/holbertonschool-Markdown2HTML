# Markdown2HTML

Petit utilitaire en Python qui prend un fichier Markdown en entrée et produit un fichier HTML en sortie (sans dépendance externe).

## Usage

```bash
./markdown2html.py README.md README.html
```

- 1er argument : fichier Markdown source.
- 2e argument : fichier HTML de sortie.

## Comportement attendu

- Si le nombre d’arguments est insuffisant : message d’usage sur stderr et code de retour 1.
- Si le fichier source n’existe pas : `Missing <filename>` sur stderr et code de retour 1.
- Sinon : ne rien afficher et retourner 0.

Exemple :

```bash
$ ./markdown2html.py
Usage: ./markdown2html.py README.md README.html
$ echo $?
1

$ ./markdown2html.py README.md README.html
Missing README.md
$ echo $?
1

$ echo "Test" > README.md
$ ./markdown2html.py README.md README.html
$ echo $?
0
```

## Contraintes

- Interprété avec Python 3.7+ sur Ubuntu 18.04 LTS.
- Respect du style PEP 8.
- Fichiers exécutables (`chmod +x markdown2html.py`).
- Code non exécuté à l’import (garde `if __name__ == "__main__":`).
- Ne pas utiliser la librairie `markdown` de Python.

