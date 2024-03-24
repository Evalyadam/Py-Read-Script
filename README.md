# Description

This is Py Read Script, **an alternative to DLL's.**
Its readable, with Python code in a .pyreadscript file. Error handling is like normal python, and shows the line, error message, and error code.

# How to Use

You will put the pyreadscript.py file in the same directory as your project and import it, by adding in the file: `from pyreadscript import pyreadscript`
Now, to call the function, you use `pyreadscript(filename)`.

For exemple:
in script.pyreadscript, there is a script/function you wanna use, assuming its in the same directory, you call `pyreadscript('script.pyreadscript')`.
