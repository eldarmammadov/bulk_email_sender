# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('./Subjects/Subjects.csv', './Subjects'),('./Text_Email/EmailTemplate1.txt', './Text_Email'),('./Text_Email/EmailTemplate2.txt', './Text_Email'),('./Text_Email/EmailTemplate3.txt', './Text_Email'),('./Text_Email/EmailTemplate4.txt', './Text_Email'),('./Prospective_Emails/List_A.csv', './Prospective_Emails'),('./Prospective_Emails/List_B.csv', './Prospective_Emails')],
    hiddenimports=[],
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
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
