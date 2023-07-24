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
attendances=[]
clock=[]
day=[]
home_possessions=[]
away_possessions=[]
home_shots=[]
away_shots=[]
home_on=[]
away_on=[]
home_off=[]
away_off=[]
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
away_yellow=[]
home_red=[]
away_red=[]
pattern = r'\d{1,3}(?:,\d{3})*'


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
        print(index)
        html_text = requests.get(link).text
        soup = BeautifulSoup(html_text, 'lxml')
        temp = soup.find('a',{"class":"sdc-site-localnav__item-link","aria-current":"true","data-role":"nav-item-links"}).attrs['href'].replace("report","stats")
        header=soup.find("div",{"class":"sdc-site-match-header__detail"})
        time = header.find("time",{"class":"sdc-site-match-header__detail-time"}).text
        try:
            stadium = header.find("span",{"class":"sdc-site-match-header__detail-venue sdc-site-match-header__detail-venue--with-seperator"}).text
            attendance = header.find("span",{"class":"sdc-site-match-header__detail-attendance"}).text
        except AttributeError:
            stadiums.append("Nan")
            attendances.append("Nan")
        else:
            attendance = re.search(pattern, attendance)
            attendance = attendance.group()
            attendances.append(attendance)
            stadiums.append(stadium)
        clock.append(time[0:6])
        html_text = requests.get(sky+temp).text
        soup = BeautifulSoup(html_text, 'lxml')
        body=soup.find("div",{"class":"sdc-site-concertina-block__body","id":"match-stats"})
        stats=body.find_all("div",{"class":"sdc-site-match-stats__stats"})
        home_possessions.append(stats[0].find("div",{"class":"sdc-site-match-stats__stats-home"}).span.span.text)
        away_possessions.append(stats[0].find("div",{"class":"sdc-site-match-stats__stats-away"}).span.span.text)
        home_shots.append(stats[1].find("div",{"class":"sdc-site-match-stats__stats-home"}).span.span.text)
        away_shots.append(stats[1].find("div",{"class":"sdc-site-match-stats__stats-away"}).span.span.text)
        home_on.append(stats[2].find("div",{"class":"sdc-site-match-stats__stats-home"}).span.span.text)
        away_on.append(stats[2].find("div",{"class":"sdc-site-match-stats__stats-away"}).span.span.text)
        home_off.append(stats[3].find("div",{"class":"sdc-site-match-stats__stats-home"}).span.span.text)
        away_off.append(stats[3].find("div",{"class":"sdc-site-match-stats__stats-away"}).span.span.text)
        home_blocked.append(stats[4].find("div",{"class":"sdc-site-match-stats__stats-home"}).span.span.text)
        away_blocked.append(stats[4].find("div",{"class":"sdc-site-match-stats__stats-away"}).span.span.text)
        home_pass.append(stats[5].find("div",{"class":"sdc-site-match-stats__stats-home"}).span.span.text)
        away_pass.append(stats[5].find("div",{"class":"sdc-site-match-stats__stats-away"}).span.span.text)
        home_chances.append(stats[6].find("div",{"class":"sdc-site-match-stats__stats-home"}).span.span.text)
        away_chances.append(stats[6].find("div",{"class":"sdc-site-match-stats__stats-away"}).span.span.text)
        home_corners.append(stats[7].find("div",{"class":"sdc-site-match-stats__stats-home"}).span.span.text)
        away_corners.append(stats[7].find("div",{"class":"sdc-site-match-stats__stats-away"}).span.span.text)
        home_offside.append(stats[8].find("div",{"class":"sdc-site-match-stats__stats-home"}).span.span.text)
        away_offside.append(stats[8].find("div",{"class":"sdc-site-match-stats__stats-away"}).span.span.text)
        home_tackles.append(stats[9].find("div",{"class":"sdc-site-match-stats__stats-home"}).span.span.text)
        away_tackles.append(stats[9].find("div",{"class":"sdc-site-match-stats__stats-away"}).span.span.text)
        home_duels.append(stats[10].find("div",{"class":"sdc-site-match-stats__stats-home"}).span.span.text)
        away_duels.append(stats[10].find("div",{"class":"sdc-site-match-stats__stats-away"}).span.span.text)
        home_saves.append(stats[11].find("div",{"class":"sdc-site-match-stats__stats-home"}).span.span.text)
        away_saves.append(stats[11].find("div",{"class":"sdc-site-match-stats__stats-away"}).span.span.text)
        home_fouls.append(stats[12].find("div",{"class":"sdc-site-match-stats__stats-home"}).span.span.text)
        away_fouls.append(stats[12].find("div",{"class":"sdc-site-match-stats__stats-away"}).span.span.text)
        home_yellow.append(stats[14].find("div",{"class":"sdc-site-match-stats__stats-home"}).span.span.text)
        away_yellow.append(stats[14].find("div",{"class":"sdc-site-match-stats__stats-away"}).span.span.text)
        home_red.append(stats[15].find("div",{"class":"sdc-site-match-stats__stats-home"}).span.span.text)
        away_red.append(stats[15].find("div",{"class":"sdc-site-match-stats__stats-away"}).span.span.text)

print(len(date))
print(len(time))
print(len(stadiums))
print(len(attendances))
#
with open("liverpool.csv","w",newline='') as file:
    wr= csv.writer(file)
    wr.writerow(["Date","Competition","clock","stadium","attendance","Home Team","Goals Home","Away Goals","Away Team","home_possessions","away_possessions","home_shots","away_shots","home_on","away_on","home_off",
                 "away_off","home_blocked","away_blocked","home_pass","away_pass",
                  "home_chances","away_chances","home_corners","away_corners","home_offside","away_offside",
                 "home_tackles","away_tackles","home_duels","away_duels","home_saves","away_saves","home_fouls",
                 "away_fouls","home_yellow","away_yellow","home_red","away_red","links",])

    for i in range(len(home_team)):
        wr.writerow([dates[i],competitions[i],clock[i],stadiums[i],attendances[i],home_team[i],goals_home[i],away_team[i],goals_away[i],home_possessions[i],away_possessions[i],home_shots[i],away_shots[i],home_on[i],
                     away_on[i],home_off[i],away_off[i],home_blocked[i],away_blocked[i],home_pass[i],away_pass[i],
                home_chances[i],away_chances[i],home_corners[i],away_corners[i],home_offside[i],away_offside[i],home_tackles[i],
                     away_tackles[i],home_duels[i],away_duels[i],home_saves[i],away_saves[i],home_fouls[i],away_fouls[i],home_yellow[i],away_yellow[i],home_red[i],away_red[i],links[i]])
