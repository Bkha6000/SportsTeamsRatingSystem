import pprint
eplPowerScore={}
"""
Calculate EPL strength of schedule """
f = open("Matches.txt","r")
m = open("Table.txt","r")

table = {}
Lines = m.readlines()
gamesPlayed=6
for line in Lines:
    terms = line.split()
    table[terms[0]]=int(terms[1])
print(table)
team_schedule={}
match_list= f.readlines()
for match in match_list:
    terms = match.split()
    team_schedule[terms[0]]=0
    for k in range(1,len(terms)):
        team_schedule[terms[0]]=team_schedule[terms[0]]+int(table[terms[k]])
eplPowerScore={}
"""
Calculate Nfl strength of schedule """
for key in team_schedule:
    eplPowerScore[key] = team_schedule[key]+table[key]
m1 = open("Standings.txt","r")
teams = m1.readlines()
nflTable={}
teamNetYdsPerPA={}
for line in teams:
    terms = line.split()
    nflTable[terms[0]]=int(terms[1])
    teamNetYdsPerPA[terms[0]]=float(terms[2])
#print(nflTable)
m1 = open("Games.txt","r")
teams = m1.readlines()
nflSchedule={}
nflScheduleNetYDS={}
for line in teams:
    terms = line.split()
    nflSchedule[terms[0]]=0
    nflScheduleNetYDS[terms[0]]=0
    for k in range(1,len(terms)):
        nflScheduleNetYDS[terms[0]]= nflScheduleNetYDS[terms[0]]+int(teamNetYdsPerPA[terms[k]])
        nflSchedule[terms[0]]=nflSchedule[terms[0]]+int(nflTable[terms[k]])
for key in nflSchedule:
    nflSchedule[key] = nflSchedule[key]/gamesPlayed
    nflScheduleNetYDS[key] = nflScheduleNetYDS[key]/gamesPlayed
#print(nflSchedule)

nflPowerScore={}
nflPowerScoreNetYDS={}
for key in nflSchedule:
    nflPowerScore[key] = nflSchedule[key]+nflTable[key]
    nflPowerScoreNetYDS[key] = nflScheduleNetYDS[key]+teamNetYdsPerPA[key]
pp=pprint.PrettyPrinter()
pp.pprint(nflPowerScore)
print(team_schedule)
