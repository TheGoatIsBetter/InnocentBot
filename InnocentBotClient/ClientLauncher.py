while(True):
    try:
        import sys
        import os
        import configparser
        import wget
        break
    except:
        os.system('pip3 install configparser')
        os.system('pip3 install wget')

config = configparser.ConfigParser()
config.read('config.ini')
config.sections()


debug = config.get('Settings', 'Debug')
URL = config.get('File Server', 'URL')

if(debug == 'True'):
    update = False
else:
    update  = True

#update Host
if update == True:

    # take out the destination dir if it exists
    if os.path.exists('Client'):
        os.remove('Client')
    
    # download new client
    wget.download(URL)
   
    
    #some old code for cloning from git 

    ## Create temporary dir
    #t = tempfile.mkdtemp()
    #print(t)
    ## Clone into temporary dir
    #os.system(f'git -C {t} clone https://github.com/TheGoatIsBetter/InnocentBot.git')
    ## Copy desired file tree from temporary dir
    #path = os.path.realpath(__file__)
    #path = path[:-18]
    #dst = path + '/Client'
    #print(dst)
    #src = f'{t}/InnocentBot/InnocentBotClient/Client'
    #print(src)
#
    #if os.path.exists(dst):
    #    shutil.rmtree(dst)
    #shutil.copytree(f'{src}', f'{dst}')
#
    ## Remove temporary dir
    #shutil.rmtree(t)
#
os.chdir('Client')
os.system('python3 InnocentBotClient.py')
sys.exit()