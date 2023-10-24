# win_dir_iconify

![this project icon](icon.png)

Process directory tree, if encounter icon.png/.jpg create/remove desktop.ini/icon.ico for that directory and set icon for that folder with other atributes


```
Usage: python main.py <path> <step>

-----------------------------------
'path' - path to directory,
'step' : ini, ico, ini_c, ico_c
 
-----------------------------------
steps:
    ini - creates desktop.ini files
    ico - creates icon.ico files
    ini_c - clears .ini files (delete)
    ico_c - clears .ico files (delete)

-----------------------------------
recomended steps: ini -> ico [-> ico_c -> ico](to be sure that explorer refresh icons)
```