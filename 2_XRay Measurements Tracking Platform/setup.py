from distutils.core import setup
import py2exe
import sys
if len(sys.argv)==1:
    sys.argv.append("py2exe")
setup(options={"py2exe":{"includes":["tkinter","pandas","matplotlib","numpy.random"]}},
                         console=["xraytracker.py"])