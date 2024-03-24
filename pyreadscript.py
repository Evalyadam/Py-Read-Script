def pyreadscript(filename):
    if filename.endswith('.pyreadscript'):
        with open(filename, 'r') as file:
            exec(file.read())
    else:
        print('Could not read file, skipping. (FILE IS NOT .pyreadscript)')

def printfilecontents(filename):
    if filename.endswith('.pyreadscript'):
        with open(filename, 'r') as file:
            contents= file.read
            print(contents)
