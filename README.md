# Description

This is Py Read Script, **an alternative to DLL's.**
Its readable, with Python code in a .pyreadscript file. Error handling is like normal python, and shows the line, error message, and error code.

# How to Use

## pyreadscript()

You will put the pyreadscript.py file in the same directory as your project and import it, by adding in the file: `import pyreadscript as prs`
Now, to call a function, you use `prs.pyreadscript(filename)`.

## printfilecontents()

There is another function called `printfilecontents(filename)`, this one prints the file contents of a `.pyreadscript` file.
and __could__ be moved to another extension. (eg. `.pyscriptcontents`.)

to call it you use `prs.printfilecontents(filename)`, replace `filename` with your actual script name.
