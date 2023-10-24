import os

def fix_path(path):
    if os.name == "nt":
        return path.replace("\\", "/")
    elif os.name == "posix":
        return win2wsl(path)
    # no fix for mac xD
    return path

def win2wsl(path):
    disk = path[0].lower()
    u_path = path[2:].replace("\\", "/")
    wsl_path = "/mnt/" + disk + u_path
    return wsl_path