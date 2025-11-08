# -*- mode: python ; coding: utf-8 -*-
import sys
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

block_cipher = None

# Streamlit 데이터 파일 수집
streamlit_datas = collect_data_files('streamlit')

# 추가 데이터 파일
added_files = [
    ('app.py', '.'),
    ('.streamlit', '.streamlit'),
]

# 숨겨진 import 수집
hiddenimports = [
    'streamlit',
    'streamlit.web.cli',
    'streamlit.web.bootstrap',
    'streamlit.runtime',
    'streamlit.runtime.scriptrunner',
    'streamlit.runtime.scriptrunner.magic_funcs',
    'anthropic',
    'openai',
    'altair',
    'pandas',
    'numpy',
    'PIL',
    'PIL._imaging',
    'pyarrow',
    'pydeck',
    'validators',
    'watchdog',
    'click',
    'tornado',
    'packaging',
    'packaging.version',
    'packaging.specifiers',
    'packaging.requirements',
]

a = Analysis(
    ['run_app.py'],
    pathex=[],
    binaries=[],
    datas=added_files + streamlit_datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='시와그림생성기',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
