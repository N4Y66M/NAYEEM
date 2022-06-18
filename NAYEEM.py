import os, platform, time
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '32bit':
    print("\n\x1b[1;92m Congratulations ! Your Device Support Tolls")
    print(" \033[1;31m   Connect Vpn if Run Error!\033[1;37m")
    from NAYEEM import Sub
    Sub()
