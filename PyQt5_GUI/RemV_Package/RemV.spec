# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['RemV.py'],
             pathex=[r'C:\Users\Armand\PycharmProjects\RemV\PyQt5_GUI\RemV_Package\pyFile'],
             binaries=[],
             datas=[(r'lib/res/image/*.png', "lib/res/image"), (r'lib/res/word_Repository/*.xlsx', "lib/res/word_Repository")
                    , (r'lib/*.txt',"lib"),(r'lib/res/image/*.jpg', "lib/res/image")],
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
          [],
          exclude_binaries=True,
          name='RemV',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False
          )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='RemV')