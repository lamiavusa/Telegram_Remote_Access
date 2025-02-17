import os

class WriteConfig:

    def __init__(self, config: dict) -> None:
        self.config = config
        self.build_dir = os.path.join(os.getcwd(), 'build')
        self.config_file = os.path.join(self.build_dir, 'src', 'config.py')

    def write_config(self) -> None:

        with open(self.config_file, 'w') as f:
            f.write(f'__CONFIG__ = {self.config}')
