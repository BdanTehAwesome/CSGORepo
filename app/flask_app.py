# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template
import urllib.request, json,pprint,operator

app = Flask(__name__)

#Profiles not set to Public
#76561198119519194 Tommy
#76561197992177096 Dennis
#76561198100508555 callum
#76561198301226240 sean 2?
#76561198064816164 connie##

def SortListOnKD(fullList):
    #code here to show profiles in ascending order on KD
    return fullList
#add in a steam ID for it to appear on the page#
listOfIDs=["76561198119457693"]
def getStats(fullList):
    listOfData=[]
    for i in listOfIDs:
            url = "http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?key=FD3CD0C6CE4594E95B645BFD740A0131&appid=730&steamid="+i
            url2 = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=FD3CD0C6CE4594E95B645BFD740A0131&appid=730&steamids="+i
            response = urllib.request.urlopen(url)
            response2 = urllib.request.urlopen(url2)
            data = json.loads(response.read())
            data2 = json.loads(response2.read())
            #pprint.pprint(data)## print the json object all pretty
            listOfData.append(data2['response']['players'][0]['avatarmedium'])
            listOfData.append(data2['response']['players'][0]['personaname'])
            #listOfData.append(data2['response']['players'][0]['realname'])#throwing errors if its not set on a players profile ie sean :P
            listOfData.append("Real name coming soon")
            listOfData.append(data['playerstats']['stats'][0]['value'])
            listOfData.append(data['playerstats']['stats'][1]['value'])
            listOfData.append(round(float(data['playerstats']['stats'][0]['value']) / float(data['playerstats']['stats'][1]['value']),2)) # kd
            listOfData.append(data['playerstats']['stats'][96]['value'])
            listOfData.append(data['playerstats']['stats'][3]['value'])
            listOfData.append(data['playerstats']['stats'][4]['value'])
            listOfData.append(round(float(data['playerstats']['stats'][25]['value'])/float(listOfData[3]),2))
            fullList.append(listOfData)
            listOfData=[]
    return fullList

@app.route('/')
def displayStats():
    fullList=[]
    getStats(fullList)
    SortListOnKD(fullList)
    return render_template('test.html',result = fullList)
if __name__ == '__main__':
   app.run(debug = True)
