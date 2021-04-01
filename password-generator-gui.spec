# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['password-generator-gui.py'],
             pathex=['C:\\Users\\Timothy Pavlushik\\Documents\\Visual Studio Code\\Projects\\password-generator'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += [('words.txt', 'C:\\Users\\Timothy Pavlushik\\Documents\\Visual Studio Code\\Projects\\password-generator\\words.txt', 'DATA')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='password-generator-gui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
