import os
import shutil

class MakeEnv:

    def __init__(self) -> None:
        self.build_dir = os.path.join(os.getcwd(), 'build')

    def make_env(self) -> None:

        if os.path.exists(self.build_dir):
            shutil.rmtree(self.build_dir)
        os.mkdir(self.build_dir)

    def get_src(self) -> None:
        src_dir = os.path.join(os.getcwd(), 'src')
        shutil.copytree(src_dir, os.path.join(self.build_dir, 'src'))