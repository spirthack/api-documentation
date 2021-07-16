from pathlib import Path
from typing import List


'''
@note: es3n1n: this script will iterate through every file in developers/ dir
and replace '\t' with '    '
'''

root_path = Path('.')

ignore = [
    '.git',
]

txt_hardtab = '\t'
markdown_hardtab = ' ' * 4


def _iterdir(dir: Path, parents: List[Path] = list()) -> None:
    global result

    for item in dir.iterdir():
        if item.name in ignore:
            continue

        if item.is_dir():
            _iterdir(item, parents=[*parents, item])
            continue

        with open(item, 'r') as f:
            content = f.read().replace(txt_hardtab, markdown_hardtab)
        with open(item, 'w') as f:
            f.write(content)


if __name__ == '__main__':
    _iterdir(root_path)
