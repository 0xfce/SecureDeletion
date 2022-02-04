from sys import argv as arg
from os import path, getcwd, listdir, remove, walk, chdir

def rmv(dir: str):
    with open(dir, mode='wb') as f:
        f.write(bytes(0x0))
        f.close()
        remove(dir)

def format(input: str) -> str:
    return str(input).replace('\\', '/').replace('//', '/')

if __name__ == '__main__':
    if path.isdir(arg[1]):
        sub_dirs = [dir for dir in walk(arg[1])]
        cwd = '%s/%s' % (format(getcwd()), arg[1],)
        if len(listdir(cwd)) > 0:
            for file in listdir(cwd):
                try:
                    print(f'{cwd}/{file} has been deleted')
                    rmv(f'{cwd}/{file}')                    
                except PermissionError:
                    pass
        if len(sub_dirs) > 1:
            for x in range(1, len(sub_dirs)):
                cwd = cwd.replace(f'{arg[1]}', '')
                chdir('%s/%s' % (format(cwd), format(sub_dirs[x][0]),))
                for j in range(0, len(sub_dirs[x])):
                    if not len(sub_dirs[x][j]) == 0:
                        for k in range(0, len(sub_dirs[x][j])):
                            try:
                                if not path.isdir(sub_dirs[x][j][k]):
                                    for file in listdir('%s/%s' % (format(cwd), format(sub_dirs[x][0]),)):                                      
                                        print('%s/%s/%s has been deleted.' % (format(cwd), format(sub_dirs[x][0]), file,))
                                        rmv('%s/%s/%s' % (format(cwd), format(sub_dirs[x][0]), file,))
                                        chdir(format(cwd))                            
                            except PermissionError:
                                pass
    else:
        print(f'{arg[1]} has been deleted.')
        rmv(arg[1])

