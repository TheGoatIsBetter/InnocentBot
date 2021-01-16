import sys
import os
import shutil
import tempfile
import configparser


config = configparser.ConfigParser()
config.read('config.ini')
config.sections()


debug = config.get('Settings', 'Debug')

if(debug == 'True'):
    update = False
else:
    update  = True

#update Host
if update == True:
    # Create temporary dir
    t = tempfile.mkdtemp()
    print(t)
    # Clone into temporary dir
    os.system(f'git -C {t} clone https://github.com/TheGoatIsBetter/InnocentBot.git')
    
    # Pathsetting magic
    path = os.path.realpath(__file__)
    path = path[:-16]
    dst = path + '/Host'
    print(dst)
    src = f'{t}/InnocentBot/InnocentBotHost/Host'
    print(src)

    # take out the destination dir if it exists
    if os.path.exists(dst):
        shutil.rmtree(dst)
    
    # move the temp dir to the destination dir
    shutil.copytree(f'{src}', f'{dst}')

    # Remove temporary dir
    shutil.rmtree(t)

os.chdir('Host')
os.system('python3.8 InnocentBotHost.py')
sys.exit(0)