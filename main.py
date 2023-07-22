from bs4 import BeautifulSoup
import requests
import csv
import re

html_text=requests.get('https://www.skysports.com/liverpool-results/2022-23').text
soup= BeautifulSoup(html_text,'lxml')
matches = soup.find_all('div', class_='fixres__item')
date = soup.find_all('h4','fixres__header2')
competition = soup.find_all('h5','fixres__header3')
sky="https://www.skysports.com"
home_team=[]
away_team=[]
goals_home=[]
goals_away=[]
dates=[]
competitions=[]
links=[]
stadiums=[]
attendance=[]
time=[]
day=[]
home_possession=[]
away_possession=[]
home_shots=[]
away_shots=[]
home_on=[]
away_on=[]
home_off=[]
away_on=[]
home_blocked=[]
away_blocked=[]
home_pass=[]
away_pass=[]
home_chances=[]
away_chances=[]
home_corners=[]
away_corners=[]
home_offside=[]
away_offside=[]
home_tackles=[]
away_tackles=[]
home_duels=[]
away_duels=[]
home_saves=[]
away_saves=[]
home_fouls=[]
away_fouls=[]
home_yellow=[]
home_red=[]


for match in matches:
    matches_results=match.find('span','matches__item-col matches__status')
    home_team.append(match.find('span','matches__item-col matches__participant matches__participant--side1').span.span.text)
    away_team.append(match.find('span','matches__item-col matches__participant matches__participant--side2').span.span.text)
    goals_home.append(matches_results.find_all('span','matches__teamscores-side')[0].text.strip())
    goals_away.append(matches_results.find_all('span','matches__teamscores-side')[1].text.strip())
    links.append(match.find('a').attrs['href'])
for x in date:
    dates.append(x.text)
for y in competition:
    competitions.append(y.text)

for index,link in enumerate(links):
    if index != 7 :
        html_text = requests.get(link).text
        soup = BeautifulSoup(html_text, 'lxml')
        temp = soup.find('a',{"class":"sdc-site-localnav__item-link","aria-current":"true","data-role":"nav-item-links"}).attrs['href'].replace("report","stats")

        html_text = requests.get(sky+temp).text
        soup = BeautifulSoup(html_text, 'lxml')

        header=soup.find("div",{"class":"sdc-site-match-header__detail"})
        time = header.find("time",{"class":"sdc-site-match-header__detail-time"}).text
        stadium = header.find("span",{"class":"sdc-site-match-header__detail-venue sdc-site-match-header__detail-venue--with-seperator"}).text
        attendance = header.find("span",{"class":"sdc-site-match-header__detail-attendance"}).text
        print(attendance)
        stadiums.append(stadium)
        day.append(time[0:6])


with open("liverpool.csv","w",newline='') as file:
    wr= csv.writer(file)
    wr.writerow(["Date","Competition","Home Team","Goals Home","Away Goals","Away Team","links"])

    for i in range(len(home_team)):
        wr.writerow([dates[i],competitions[i],home_team[i],goals_home[i],away_team[i],goals_away[i],links[i]])
