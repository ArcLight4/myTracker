#### WINAMAX TRACKER V.2 ####

import time
import glob,os.path,re,matplotlib.pyplot as plt,numpy as np

start_time = time.time() #a supprimer

user_name = "William"
player_name = "WB-44"
local_disk = "C"

def listdirectory(path):
    l,variante,position,nbjoueur,vitesse,mode,prizepool,gain,buyin,date,gain_b=glob.glob(path+'\\*'),[],[],[],[],[],[],[],[],[],False
    for i in l:
        if os.path.isdir(i): listdirectory(i)
        else:
            if os.path.splitext(i)[1] == '.txt':
                if i.find("_summary")>-1 :
                    a = open(i, "r", encoding='utf-8')
                    b = a.readlines()
                    if i[len(path)+1:].find("holdem_no")>-1 : variante.append("NLHE")
                    elif i[len(path)+1:].find("omaha_pot")>-1 : variante.append("PLO")
                    else : variante.append("Other")
                    
                    for k in b :
                        if k.find("You finished in")>-1 :
                            position.append(int(re.sub("[^0-9]", "", k)))
                        elif k.find("Registered players")>-1 :
                            nbjoueur.append(int(re.sub("[^0-9]", "", k)))
                        elif k.find("Speed")>-1 :
                            vitesse.append(str(k)[8:-2])                            
                        elif k.find("Mode")>-1 :
                            mode.append(str(k)[7:-2]) 
                        elif k.find("Prizepool")>-1 :
                            prizepool.append(float(k[12:].replace('€\n','')))
                        elif k.find("You won")>-1 :
                            gain_b = True
                            gainraw = re.search("You won (\d+\.?\d*)€", k)
                            gain.append(float(gainraw.group(1)))
                        elif k.find("Tournament started")>-1 :
                            date.append(str(k[19:29]))
                        elif k.find("Buy-In")>-1 :
                            buyinraw = re.search("Buy-In : (\d+\.?\d*)€ \+ (\d+\.?\d*)€", k)
                            buyin.append((buyinraw.group(1), buyinraw.group(2)))
                        
                    a.close()
                    if not gain_b  : gain.append(0)
                    else : gain_b = False
        
    return variante,position,nbjoueur,vitesse,mode,prizepool,gain,date,buyin
    
result=listdirectory(local_disk + ":\\Users\\" + user_name + "\\Documents\\Winamax Poker\\accounts\\" + player_name + "\\history")


print("%s sec" % (time.time() - start_time)) #a supprimer