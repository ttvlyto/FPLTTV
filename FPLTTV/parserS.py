from bs4 import BeautifulSoup

import asyncio


def parseStats(stats, len):## passes thru dict with link and keyPair html
    f = open("links.txt", "r")
    p = open("playerStats.txt", "w")

    name = '' 
    club = ''

    dob = ''
    appearances = 0
    arr = []
    lineNumber = 0

    for line in f:
        lineNumber += 1
        if lineNumber == len:
            return


        p.write(line + '\n')
        #######
        newstr = line
        newstr = newstr[35:-10]
        if newstr[0].isdigit():
            newstr = newstr[2:]
    
        elif newstr[0] == '/':
            newstr = newstr[1:]
    
        newstr = newstr.replace('-', ' ')

        p.write(newstr + '\n')
    
        ######
        newstr = (stats[line])
        p.write(newstr + '\n')
        soup = BeautifulSoup(newstr, "html.parser")
        data = soup.find_all("div", {"class": "player-overview__info"})
        moreData = soup.find_all("div", {"data-script": "pl_player"})
        evenMoreData = soup.find("div", {"data-widget": "player-overview-stats"})
        index = 0
        for x in data:
            print(index, ". HTML")
            p.write(x.prettify())
            print(x.get_text())
            index += 1


        p.write("******end, new player******\n")


def testParser():
    p = open("playerStats.txt", "r") ## opens player stats to start reading
    newfile = open('newPlayer.txt', 'w') ## opens new txt for writing
    list_of_links = []

    f = open('links.txt', 'r') ## opens links and puts it in a list
    for line in f:
        list_of_links.append(line)
        

    whole_html = ''
    index = 0 
    

    for line in p: ## opens html txt adds is and detects for new
        line_of_html = line
        whole_html = whole_html + line

       
        if line_of_html.__contains__('******end, new player******'): ##checks for end of line

            player_link = list_of_links[index] ## writes player link
           

            print(whole_html)
            print(player_link)
            newfile.write(player_link)
            index += 1
            print('*****\n')
            soup = BeautifulSoup(whole_html, "html.parser")
            data = soup.find_all("div", {"class": "player-overview__info"})
            print(data)
            print("here is data\n")
            whole_html = ''
            
            for x in data:
        
                newfile.write(x.prettify() + '\n') ##my shittiy coding habits have come back to fight me....
            
            newfile.write("******end, new player******\n")
            

            
            


        
        

    


    