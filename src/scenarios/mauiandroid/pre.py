'''
pre-command
'''
import sys
import os
from zipfile import ZipFile
from performance.logger import setup_loggers
from shutil import copyfile
from shared.precommands import PreCommands
from shared.const import PUBDIR
from argparse import ArgumentParser

setup_loggers(True)

parser = ArgumentParser()
parser.add_argument('--unzip', help='Unzip APK and report extracted tree', action='store_true', default=False)
args = parser.parse_args()

apkname = 'MauiAndroidDefault.apk'
apknamezip = '%s.zip' % (apkname)
if not os.path.exists(apkname):
    print('Cannot find %s' % (apkname))
    exit(-1)
if args.unzip:
    if not os.path.exists(apknamezip):
        copyfile(apkname, apknamezip)

    with ZipFile(apknamezip) as zip:
        zip.extractall(os.path.join('.', PUBDIR))

    assets_dir = os.path.join(PUBDIR, 'assets')
    assets_zip = os.path.join(assets_dir, 'assets.zip')
    with ZipFile(assets_zip) as zip:
        zip.extractall(assets_dir)

    os.remove(assets_zip)
else:
    os.mkdir(PUBDIR)
    copyfile(apkname, os.path.join(PUBDIR, apkname))



