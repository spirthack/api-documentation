from pathlib import Path
from typing import List


'''
@note: es3n1n: this script will iterate through every file in developers/ dir
and generate for this directory summary schema
'''

root_path = Path('.')

ignore = [
    '.github',
    '.git',
    'LICENSE.md',
    'README.md',
    'SUMMARY.md',
    'scripts',
]

remap = {
    '_t': '',
    '_': ' ',
    'api': 'API',
    'esp': 'ESP',
    'C Base': 'C_Base',  # @note: es3n1n: 300iq move
}

markdown_list = '- '
markdown_url = lambda name, path: f'[{name}]({path})'
markdown_nextline = '\n'
markdown_hardtab = ' ' * 3

summary_path = root_path / 'SUMMARY.md'
summary_header = f'''# Table of contents

- [Useful information](README.md){markdown_nextline}'''


result = summary_header


def _iterdir(dir: Path, parents: List[Path] = list()) -> None:
    global result

    for item in sorted(dir.iterdir(), key=lambda x: x.is_dir(), reverse=True):
        if item.name in ignore:
            continue

        name = item.name.split('.')[0]
        name = name.capitalize() if name[0] != name[0].upper() else name

        # @note: es3n1n: remapping _ to ' ', etc
        for k in remap.keys():
            name = name.replace(k, remap[k])

        pad = markdown_hardtab * (len(parents))
        pad = markdown_hardtab if not item.is_dir() and pad == '' else pad
        
        relative_path = str(item).replace('\\', '/')
        if item.is_dir():
            relative_path += '/README.md'
        
        result += f'{pad}{markdown_list}{markdown_url(name, relative_path)}{markdown_nextline}'

        if item.is_dir():
            _iterdir(item, parents=[*parents, dir])


if __name__ == '__main__':
    _iterdir(root_path)
    
    with open(summary_path, 'w') as f:
        f.write(result)
