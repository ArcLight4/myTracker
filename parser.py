import glob
import os.path
import re

path = 'D:/Documents/Winamax Poker/accounts/ArcLight__4/history'

def listdirectory(path):
    files = glob.glob(path+'/*')
    variante, position, nbjoueur, vitesse, mode, prizepool, buyin, gain = [], [], [], [], [], [], [], []

    for i in files:

        if os.path.splitext(i)[1] == '.txt':

            if i.find('_summary')>-1 :
                a = open(i, 'r', encoding='utf-8')
                raw = a.read()


                if i[len(path)+1:].find('holdem_no')>-1 :
                    variante.append('NLHE')

                elif i[len(path)+1:].find('omaha_pot')>-1 :
                    variante.append('PLO')

                else :
                    variante.append('Other')

                position.append(int(re.search('You finished in (\d+)', raw).group(1)))

                nbjoueur.append(int(re.search('Registered players : (\d+)', raw).group(1)))

                vitesse.append(re.search('Speed : (\S+)', raw).group(1))

                mode.append(re.search('Mode : (\S+)', raw).group(1))

                prizepool.append(re.search('Prizepool : (\d+\.?(\d+)?)€', raw).group(1))
                
                buyinraw = re.search('Buy-In : (\d+\.?\d*)€ \+ (\d+\.?\d*)€', raw)
                buyin.append((buyinraw.group(1), buyinraw.group(2)))
                
                if re.search('You won (\d+\.?\d*)€', raw):
                    gain.append(float(re.search('You won (\d+\.?\d*)€', raw).group(1)))
                else:
                    gain.append(0)

                a.close()
        
    return [variante, position, nbjoueur, vitesse, mode, prizepool, gain, buyin]


result = listdirectory(path)