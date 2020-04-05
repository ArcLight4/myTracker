import glob
import os.path
import re
import datetime

path = 'D:/Documents/Winamax Poker/accounts/ArcLight__4/history'


def listdirectory(path):
    files = glob.glob(path + '/*')
    games = []

    for i in files:

        if os.path.splitext(i)[1] == '.txt':

            if i.find('_summary') > -1:
                a = open(i, 'r', encoding='utf-8')
                raw = a.read()

                if i[len(path) + 1:].find('holdem_no') > -1:
                    variante = 'NLHE'
                elif i[len(path) + 1:].find('omaha_pot') > -1:
                    variante = 'PLO'
                else:
                    variante = 'Other'

                position = int(re.search('You finished in (\d+)', raw).group(1))

                nbjoueur = int(re.search('Registered players : (\d+)', raw).group(1))

                vitesse = re.search('Speed : (\S+)', raw).group(1)

                mode = re.search('Mode : (\S+)', raw).group(1)

                prizepool = float(re.search('Prizepool : (\d+\.?\d*)€', raw).group(1))

                buyinraw = re.search('Buy-In : (\d+\.?\d*)€ \+ (\d+\.?\d*)€', raw)
                buyin = (float(buyinraw.group(1)), float(buyinraw.group(2)))

                dateraw = re.search(
                    'Tournament started ([\d]{4})\/([\d]{2})\/([\d]{2}) ([\d]{2})\:([\d]{2})\:([\d]{2}) (\S+)', raw)
                date = datetime.datetime(int(dateraw.group(1)), int(dateraw.group(2)), int(dateraw.group(3)),
                                         int(dateraw.group(4)), int(dateraw.group(5)), int(dateraw.group(6)))

                if re.search('You won (\d+\.?\d*)€', raw):
                    gain = (float(re.search('You won (\d+\.?\d*)€', raw).group(1)))
                else:
                    gain = (0)

                a.close()
                games.append((variante, position, nbjoueur, vitesse, mode, prizepool, date, gain, buyin))

    return games


result = listdirectory(path)
