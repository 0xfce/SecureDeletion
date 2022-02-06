from argparse import ArgumentParser as ArgParser
from os import path, getcwd, listdir, remove, walk, chdir

parser = ArgParser()

parser.add_argument('-s', '--specify', help='Deletes only a specific files extension', required=False)
parser.add_argument('-p', '--path', help='Path to the file/directory/folder', required=True)

args = parser.parse_args()

def format(input: str) -> str:
    return input.replace('\\', '/').replace('//', '/')

def rmv(dir: str):
    dir = format(dir)
    first_path = getcwd()
    try:
        if path.isdir(dir):
            chdir(dir)
            if not args.path == 'here' or not args.path == 'this' and not first_path == dir:
                for files in listdir(dir):
                    with open(files, mode='wb') as f:
                        if args.specify:
                            if f.name.endswith(f'.{args.specify}'):
                                f.write(bytes(0x0))
                                f.close()
                                print(f'{f.name} has been deleted.')
                                remove(f.name)                          
                        else:
                            f.write(bytes(0x0))
                            f.close()
                            print(f'{f.name} has been deleted.')
                            remove(f.name)
                chdir(args.path)
        else:
            with open(dir, mode='wb') as f:
                f.write(bytes(0x0))
                f.close()
                print(f'{f.name} has been deleted.')
                remove(f.name)            
    except NotADirectoryError:
        print('directory not found.')
    except FileNotFoundError:
        print('file not found.')
    except PermissionError:
        pass

def execute(_path:str):
    if path.isdir(_path):
        sub_dirs = [dir for dir in walk(_path)]
        if len(listdir(_path)) > 0:
            for file in listdir(_path):
                rmv(f'{_path}/{file}')                        
        if len(sub_dirs) > 1:
            for x in range(1, len(sub_dirs)):
                chdir(format(sub_dirs[x][0]))
                for j in range(0, len(sub_dirs[x])):
                    if not len(sub_dirs[x][j]) == 0:
                        for k in range(0, len(sub_dirs[x][j])):
                            if not path.isdir(sub_dirs[x][j][k]):
                                for file in listdir(format(sub_dirs[x][0])):                                      
                                    rmv('%s/%s' % (format(sub_dirs[x][0]), file,))
                                    chdir(format(_path))                            
    else:
        rmv(_path)

if __name__ == '__main__':
    execute(getcwd() if args.path == 'this' or args.path == 'here' else args.path)

