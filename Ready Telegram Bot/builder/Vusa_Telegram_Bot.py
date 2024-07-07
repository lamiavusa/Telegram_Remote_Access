from util.makeenv import MakeEnv
from util.obfuscate import DoObfuscate
from util.build import Build
from util.config import Config
from util.writeconfig import WriteConfig
from rich.console import Console
import pyfiglet

def main():
    console = Console()

    console.clear()
    console.print(pyfiglet.figlet_format("VUSA", font="graffiti"),
                  justify="center", highlight=False, style="magenta", overflow="ignore")
    console.print(f"-_-",
                  justify="center", highlight=False, style="bold magenta", overflow="ignore")
    
    config = Config()
    config_data = config.get_config()

    make_env = MakeEnv()
    make_env.make_env()
    make_env.get_src()

    write_config = WriteConfig(config_data)
    write_config.write_config()

    do_obfuscate = DoObfuscate()
    do_obfuscate.run()

    build = Build()
    build.get_pyinstaller()
    build.get_upx()
    build.build()

if __name__ == "__main__":
    main()
