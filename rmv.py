from sys import argv as arg
from os import path, getcwd, listdir, remove, walk, chdir

def remove(dir: str):
    with open(dir, mode='wb') as f:
        f.write(bytes(0x0))
        f.close()
        remove(dir)

if __name__ == '__main__':
    if path.isdir(arg[1]):
        sub_dirs = [dir for dir in walk(arg[1])]
        cwd = f'{getcwd()}/{arg[1]}'.replace('\\', '/')
        if len(listdir(cwd)) > 0:
            for file in listdir(cwd):
                try:
                    print(f'{cwd}/{file} has been deleted.')
                    remove(f'{cwd}/{file}')                    
                except PermissionError:
                    pass
        if len(sub_dirs) > 1:
            for x in range(1, len(sub_dirs)):
                aa = cwd.replace(f'{arg[1]}', '')
                chdir(f'{aa}/{sub_dirs[x][0]}'.replace('\\', '/').replace('//', '/'))
                for j in range(0, len(sub_dirs[x])):
                    if not len(sub_dirs[x][j]) == 0:
                        for k in range(0, len(sub_dirs[x][j])):
                            try:
                                if not path.isdir(sub_dirs[x][j][k]):
                                    for file in listdir(f'{aa}/{sub_dirs[x][0]}'.replace('//', '/').replace('\\', '/')):                                      
                                        print(f'{aa}/{sub_dirs[x][0]}/{file} has been deleted.'.replace('//', '/').replace('\\', '/'))
                                        remove(f'{aa}/{sub_dirs[x][0]}/{file}'.replace('//', '/').replace('\\', '/'))
                                        chdir(cwd)                            
                            except PermissionError:
                                pass
    else:
        print(f'{arg[1]} has been deleted.')
        remove(arg[1])


