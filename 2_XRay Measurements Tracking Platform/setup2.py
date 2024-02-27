import sys,os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'D:\ProgramFiles\Anaconda3\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'D:\ProgramFiles\Anaconda3\tcl\tk8.6'

__version__="1.1.0"

include_files=['icoco.ico']
packages=["os","tkinter","json","base64","pyodbc","time","pathlib","webbrowser","openpyxl","pandas","pandastable","numpy"]
setup(name="XRay Tracker",description="XRays Measurements Tracking App",version=__version__,
      options={"build_exe":{'packages':packages,"include_files":include_files,"include_msvcr":True}},executables=[Executable("xraytracker.py",base="Win32GUI")])