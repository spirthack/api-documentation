from pathlib import Path
from typing import List


'''
@note: es3n1n: this script will migrate from api classes to tables
g_GlobalVars: -> GlobalVars.
cheat -> Cheat
'''

root_path = Path('.')

ignore = [
    '.git',
    'LICENSE.md',
    'README.md',
    'SUMMARY.md',
    'scripts',
]

remap = {
    'g_GlobalVars:': 'GlobalVars.',
    'g_ClientState:': 'ClientState.',
    'cheat.': 'Cheat.',
    'utils': 'Utils.',
    'menu.': 'Menu.',
    'http.': 'Http.',
    'ragebot.': 'RageBot.',
    'antiaim.': 'AntiAim.',
    'exploits.': 'Exploits.',
    'fakelag.': 'FakeLag.',
    'esp.': 'ESP.',
    'g_EngineTrace:': 'EngineTrace.',
    'g_EntityList:': 'EntityList.',
    'g_EngineClient:': 'EngineClient.',
    'g_DebugOverlay:': 'DebugOverlay.',
    'g_MaterialSystem:': 'MatSystem.',  # @note: es3n1n: unsure
    'g_MatSystem:': 'MatSystem.',
    'g_RenderBeams:': 'RenderBeams.',
    'g_Render:': 'Render.',
    'g_Panorama:': 'Panorama.',
    'g_CVar:': 'CVar.',
    'Utils..': 'Utils.',  # @note: es3n1n: ugh just cz it was broken
    'g_Config:': 'Menu.',
}


def _iterdir(dir: Path) -> None:
    global result

    for item in dir.iterdir():
        if item.name in ignore:
            continue

        if item.is_dir():
            _iterdir(item)
            continue

        with open(str(item), 'r') as f:
            content = f.read()

        for k in remap.keys():
            content = content.replace(k, remap[k])

        with open(str(item), 'w') as f:
            f.write(content)


if __name__ == '__main__':
    _iterdir(root_path)
