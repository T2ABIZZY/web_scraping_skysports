
import requests
import csv
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://www.skysports.com/premier-league-results/2022-23")
WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[id^=sp_message_iframe_758392]")))
try:
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".message-component.message-button.no-children.focusable.sp_message-accept-button.sp_choice_type_11"))).click()
except:
    print("Could not click")
    pass

driver.find_element(By.CLASS_NAME,"plus-more").click()
page_source = driver.page_source
driver.quit()



soup= BeautifulSoup(page_source,'lxml')

matches = soup.find_all('div', class_='fixres__item')

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
        date_part = time.split(',')[1].strip()
        date_only = date_part.split(' ')[1:4]
        date_string = ' '.join(date_only)
        date_string=date_string[:len(date_string)-1]
        dates.append(date_string)
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


#
with open("Premier_League.csv","w",newline='') as file:
    wr= csv.writer(file)
    wr.writerow(["date","clock","stadium","attendance","Home Team","Goals Home","Away Goals","Away Team","home_possessions","away_possessions","home_shots","away_shots","home_on","away_on","home_off",
                 "away_off","home_blocked","away_blocked","home_pass","away_pass",
                  "home_chances","away_chances","home_corners","away_corners","home_offside","away_offside",
                 "home_tackles","away_tackles","home_duels","away_duels","home_saves","away_saves","home_fouls",
                 "away_fouls","home_yellow","away_yellow","home_red","away_red","links",])

    for i in range(len(home_team)):
        wr.writerow([dates[i],clock[i],stadiums[i],attendances[i],home_team[i],goals_home[i],away_team[i],goals_away[i],home_possessions[i],away_possessions[i],home_shots[i],away_shots[i],home_on[i],
                     away_on[i],home_off[i],away_off[i],home_blocked[i],away_blocked[i],home_pass[i],away_pass[i],
                home_chances[i],away_chances[i],home_corners[i],away_corners[i],home_offside[i],away_offside[i],home_tackles[i],
                     away_tackles[i],home_duels[i],away_duels[i],home_saves[i],away_saves[i],home_fouls[i],away_fouls[i],home_yellow[i],away_yellow[i],home_red[i],away_red[i],links[i]])
