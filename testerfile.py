import csv
import re

class Player:
    name = ''
    club =  ''
    dob = ''
    def __init__(self, name, pos, club, dob, link):
        self.name = name
        self.pos = pos
        self.club = club
        self.dob = dob
        self.link = link

    def get_name(self):
        return self.name

    def get_pos(self):
        return self.pos

    def get_club(self):
        return self.club

    def get_dob(self):
        return self.dob

    def get_link(self):
        return self.link




def getClubName(html_line):
    clubName = html_line[14:-11]
    i = 1
    while clubName[i] != '/':
        i += 1
    clubName = clubName[i+1:]
    clubName = clubName.replace('-', ' ')

    return clubName


def parseNprint():
    f = open("playerStats.txt", 'r')
    strlen = len("overview__info")
    players = open("links.txt")
    pos = {'Goalkeeper', 'Defender', 'Midfielder', 'Forward'}
    unaccounted = []

    x = 0
    noClub = 0
    player_link = ''
    name = ''
    club = ''
    age = ''
    dob = ''
    position = ''
    appearances = 0
    arr = []
    playernum = 1;
    for line in f:  ##opens playerStats and go thru each line individually
        newstr = line.replace('\n', '')  ##removes newline just to make sure everything is read equally
        x += 1
        i = 0

        if newstr == '******end, new player******':  ##immediately checks for new playerline
            searching = ''
            for x in range(0, len(unaccounted)):
                searching = searching + unaccounted[x]

            age = re.search("\d\d[\/]\d\d[\/]\d\d\d\d", searching)

            print(playernum, ":\nName:", name)
            print(player_link)
            print('Age:', age.group())
            if club == '':
                print("NO VALID CLUB\n")
                playernum += 1
                noClub += 1
                continue

            print('Position:', position)
            print('Club:', club)

            '''
            print('*****')
            print(unaccounted)


            print('******')
              '''
            ##print('new player has been found, reset\n')
            print('\n')
            player_obj = Player(name, position, club, age.group(), player_link)
            arr.append(player_obj)
            playernum += 1

            name = ''
            club = ''
            x = 0
            age = ''
            unaccounted.clear()  ##prints all the found data, then clears vars along with list

        if newstr.__contains__('www.premierleague.com/players/'):  ## shortens down link and gets name from the link
            player_link = newstr
            newstr = newstr[35:-9]
            if newstr[0].isdigit():
                newstr = newstr[2:]

            elif newstr[0] == '/':
                newstr = newstr[1:]

            newstr = newstr.replace('-', ' ')
            name = newstr
            ##print(newstr) ## prints name, assigned to name var

        if newstr.__contains__('overview__info'):  ##this line hold most of the intresting data

            newstr = next(f)  ##gets the juicy html
            newstr = newstr.replace(" ", "")
            newstr = newstr.replace("\n", "")
            if newstr == '</div>' or newstr == '</section>':
                continue  ##

            for w in pos:
                if newstr.__contains__(w):  ##checks if position is in list, which should be then assignes it when found
                    position = w
                    ##print('Postition', newstr)
                    continue

            if newstr.__contains__('club'):
                club = getClubName(newstr)

            if (x == 1344):
                newstr = newstr.replace("\n", "")
                age = newstr
                ##print("Age:", newstr)
            if (x == 1353):
                newstr = newstr.replace(" ", "")
                newstr = newstr.replace("\n", "")
                club = newstr
                ##print("club:", newstr)
            else:
                unaccounted.append(newstr)

    print(len(arr))
    print(noClub)

    with open('players.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Position', 'Club', 'DOB', 'link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for x in arr:
            print(x.get_name())
            print(x.get_pos())
            print(x.get_club())
            print(x.get_dob())
            print(x.get_link())

            data = {
                'Name': x.get_name(),
                'Position': x.get_pos(),
                'Club': x.get_club(),
                'DOB': x.get_dob(),
                'link': x.get_link()
            }
            writer.writerow(data)

            print('******\n')

