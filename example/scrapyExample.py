
from lxml import html
import requests
class PageParser:
    page = requests.get('http://www.betexplorer.com/hockey/asia/asia-league-2017-2018/nikko-ice-bucks-oji-eagles/0A1vvE0N/')
    tree = html.fromstring(page.content)
    def parserURL(self,url):
        url='http://www.betexplorer.com/hockey/asia/asia-league-2017-2018/nikko-ice-bucks-oji-eagles/0A1vvE0N/'
        urls=url.strip("http://").split("/")
        gametype=urls[1]
        game_name=urls[3]
        game_id=urls[-1]
        return(game_id+","+game_name+","+gametype)
    def get_season(self,tree):
        rawText=tree.xpath('//h1[@class="wrap-section__header__title"]/a/text()')
        #print(rawText[0].split(' ')[-1].split('/')[0]) e.g. Asia League 2018/2019 get 2018
        season=rawText[0].split(' ')[-1].split('/')[0]
        print(season)
        return season
    def get_participants(self,tree):
        rawParticipants=tree.xpath('//li/h2[@class="list-details__item__title"]/a/text()')
        participant1=rawParticipants[0]
        participant2=rawParticipants[1]
        return (participant1,participant2)
    def get_scoreDetail(self,tree):
        rawscore=tree.xpath('//li/h2[@id="js-partial" ]/text()')[0].strip("()")
        print(rawscore)
        return rawscore
    def get_participants_score(self,tree):
        score=tree.xpath('//li/p[@id="js-score" ]/text()')[0]
        scoresplits=score.split(":")
        participant1_score=scoresplits[0]
        participant2_score=scoresplits[1]
        return (participant1_score,participant2_score)
    def getDateTime(self,tree):

       
        match_date=tree.xpath('//li/p[@id="match-date"]/@data-dt')
        print(match_date)
        temps=match_date[0].split(",")
        month=temps[1]
        day=temps[0]
        year=temps[2]
        hrs=temps[3]
        mins=temps[4]
        time=hrs+":"+mins
        return(year,month,day,time)
page = requests.get('http://www.betexplorer.com/hockey/asia/asia-league-2017-2018/nikko-ice-bucks-oji-eagles/0A1vvE0N/')
tree = html.fromstring(page.content)