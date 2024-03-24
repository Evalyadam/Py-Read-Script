def pyreadscript(filename):
    if filename.endswith('.pyreadscript'):
        with open(filename, 'r') as file:
            returnedscript = file.read()
            exec(returnedscript)
    else:
        print("Error: Must be a .pyreadscript file. - ID=1")
