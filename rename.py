import shutil
from pathlib import Path 
class Rename():
    def _add_prefix_to_path(self, path, prefix):
        '''Add the specified prefix to a file or a directory but dose NOT check path validity
        '''
        shutil.move(path, Path(path.parent, f'{prefix}{path.name}'))

    def add_prefix(self, path, type, specifier):
        if path.exists():
            if type == 'string' or 'str':
                self._add_prefix_to_path(path, specifier)


path = Path(Path.cwd(), 'a_a_b')
rn = Rename()
rn.add_prefix(path, 'string', 'a_')