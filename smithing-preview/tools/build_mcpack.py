#!/usr/bin/env python3
"""Zip the pack/ folder into a .mcpack (files at the archive root, no wrapper folder).

Usage: python3 tools/build_mcpack.py [output.mcpack]
Runs tools/validate_pack.py first and refuses to build if it reports errors.
"""
import os
import subprocess
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.join(os.path.dirname(HERE), 'pack')
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(HERE), 'dist', 'Smithing-Preview.mcpack')

if subprocess.call([sys.executable, os.path.join(HERE, 'validate_pack.py'), PACK]) != 0:
    sys.exit('validation failed, pack not built')

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(PACK):
        for name in sorted(files):
            full = os.path.join(root, name)
            z.write(full, os.path.relpath(full, PACK).replace(os.sep, '/'))
print('built', OUT)
