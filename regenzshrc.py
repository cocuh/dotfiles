#!/bin/env python
import os
import sys
try:
    import io
except:
    import StringIO as io


class ZshRc(object):
    directory_path = os.path.expanduser('~/.zshrc.d')
    config_path = os.path.expanduser('~/.zshrc.d/zshrc.conf')
    zshrc_path = os.path.expanduser('~/.zshrc')

    @staticmethod
    def is_module_name(name):
        name = name.strip()
        if name.startswith('#'):
            return False
        elif len(name) == 0:
            return False
        else:
            return True

    def __init__(self):
        module_names = [
            name.strip()
            for name in open(self.config_path).readlines()
            if self.is_module_name(name)
        ]
        self.module_names = module_names

    def generate_module_data(self, name):
        path = os.path.join(self.directory_path, name)
        _data = open(path).read().strip()
        data = '\n'.join([
            '##################################',
            '# {}'.format(name),
            '##################################',
            '() {',
            '{}'.format(_data),
            '}',
        ])
        return data

    def generate(self):
        data = '\n\n\n\n'.join(
            self.generate_module_data(name)
            for name in self.module_names
        )
        return data

    def update(self):
        with open(self.zshrc_path, 'w') as fp:
            fp.write(self.generate())

def main():
    zshrc = ZshRc()
    zshrc.update()

if __name__ == '__main__':
    main()