# Secure Deletion
## _it automatically set the given file bytes to 0 and delete it, to prevent the file recovery. i guess_

## Usage
Example-0:
```sh
PS C:/> rmv -p C:/Users/0xfce/desktop/some_random_file.exe 
```
Example-1:
```sh
PS C:/> rmv -p g:/bunch_of_useless_shit_folder -s txt "it will delete every .txt file in the target folder"
```
Example-2:
```sh
PS C:/Users/0xfce> cd desktop/bunch_of_useless_shit_folder/
PS C:/Users/0xfce/bunch_of_useless_shit_folder> rmv -p here -s pdf "it will delete every pdf file in the current working directory/folder"
```
Example-3:
```sh
PS C:/Users/0xfce> cd desktop/bunch_of_useless_shit_folder/
PS C:/Users/0xfce/bunch_of_useless_shit_folder> rmv -p here "it will delete everything in the current working directory/folder"
```
Example-4:
```sh
PS C:/> rmv -p g:/bunch_of_useless_shit_folder  "it will delete everything in the target directory/folder"
```
## Requirements:
- Python 3
