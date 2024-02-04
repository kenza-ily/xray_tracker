# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['XRayTracker_try5.py'],
             pathex=['Y:\\10 - Projects\\02-Database managment\\XRay Measurements Tracking Plaform\\XRaysTracker'],
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
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='XRayTracker_try5',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='HSS-monogram-logo_1400.ico')
