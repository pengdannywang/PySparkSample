
from lxml import html
import csv
import requests
class PageParser:
    page = requests.get('http://www.betexplorer.com/hockey/asia/asia-league-2017-2018/nikko-ice-bucks-oji-eagles/0A1vvE0N/')
    tree = html.fromstring(page.content)
    def parserURL(self,url):
      
        urls=url.strip("http://").split("/")
        gametype=urls[1]
        game_name=urls[3]
        game_id=urls[-1]
        return(game_id,gametype,game_name)
    
    
    def get_season(self,tree):
        rawText=tree.xpath('//h1[@class="wrap-section__header__title"]/a/text()')
        #print(rawText[0].split(' ')[-1].split('/')[0]) e.g. Asia League 2018/2019 get 2018
        season=rawText[0].split(' ')[-1].split('/')[0]
   
        return season
    
    
    def get_participants(self,tree):
        rawParticipants=tree.xpath('//li/h2[@class="list-details__item__title"]/a/text()')
        participant1=rawParticipants[0]
        participant2=rawParticipants[1]
        return (participant1,participant2)
    
    
    def get_scoreDetail(self,tree):
        rawscore=tree.xpath('//li/h2[@id="js-partial" ]/text()')[0].strip("()")
        return rawscore
    
    
    def get_participants_score(self,tree):
        score=tree.xpath('//li/p[@id="js-score" ]/text()')[0]
        scoresplits=score.split(":")
        participant1_score=scoresplits[0]
        participant2_score=scoresplits[1]
        return (participant1_score,participant2_score)
    
    
    def getDateTime(self,tree):
        match_date=tree.xpath('//li/p[@id="match-date"]/@data-dt')

        temps=match_date[0].split(",")
        month=temps[1]
        day=temps[0]
        year=temps[2]
        hrs=temps[3]
        mins=temps[4]
        time=hrs+":"+mins
        return(day,month,year,time)
    
    
    def getRow(self,url):
        page = requests.get(url)
        tree = html.fromstring(page.content)
        game_id,sport,competition=self.parserURL(url)
        season=self.get_season(tree)
        match_day,match_month,match_year,start_time=self.getDateTime(tree)
        participant_1,participant_2=self.get_participants(tree)
        participant_1_score,participant_2_score=self.get_participants_score(tree)
        full_score=self.get_scoreDetail(tree)
        row=list()
        
        row.append(game_id)
        row.append(url)
        row.append(sport)
        row.append(competition)
        row.append(season)
        row.append(match_day)
        row.append(match_month)
        row.append(match_year)
        row.append(start_time)
        row.append(participant_1)
        row.append(participant_2)
        row.append(participant_1_score)
        row.append(participant_2_score)
        row.append(full_score)

        return (row)
    
page = 'http://www.betexplorer.com/hockey/asia/asia-league-2017-2018/nikko-ice-bucks-oji-eagles/0A1vvE0N/'
parser=PageParser()
row=parser.getRow(page)

with open('persons.csv','a', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar="'", quoting=csv.QUOTE_MINIMAL)
    print(row)
    filewriter.writerow(row)



    
    