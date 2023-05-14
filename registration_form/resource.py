from pathlib import Path
import os.path
import tests

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
path_file = os.path.join(PROJECT_ROOT_PATH, 'resources')

def path(file_name):
    return str(
        Path(tests.__file__).parent.joinpath(f'resources/{file_name}').absolute()
    )
