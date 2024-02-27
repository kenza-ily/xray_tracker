#############################################################################
#           Sets the Cx_Freeze made App parameters
#############################################################################



#import cx_freeze
import sys
import matplotlib

base=None

if sys.platform=='win32':
    base='Win32GUI'
    
executables=[cx_Freeze.Executable("df_saver.py"),base=base,icon='HSS-monogram-logo_1400.ico']

cx_Freeze.setup(
        name="XRays Measurements Tracking App",
        options={"build_exe":{"packages":["tkinter","matplotlib","webbrowser","pathlib","datetime","pandas","pandastable","subprocess"],"include_files":['HSS-monogram-logo_1400.ico']}},
        version="0.01",
        description = " App screening the Studies directory in order to track the Status of each X-Ray and display a list of X-Rays to check or to verify",
        executables=executables
        )