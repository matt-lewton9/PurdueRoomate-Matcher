import csv
excpt = ['hopefully', 'not', 'too', 'now', 'looking', '', 'in', 'or', 'and', 'the', 'to', 'either', 'maybe', 'at', 'but', 'planning', 'in', 'at', 'apply', 'applying', 'just', 'i', 'is', 'are', 'can', 'listen', 'however', 'a', 'with', 'for', 'as', 'by', 'on', 'out', 'so']


def load(file):
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #Create Subject Student 
            Stud.append([row['Name'], row['Learning Community?'].lower(), row['Major?'].lower(), row['Rushing (frats)'].lower(), row['I/E'].lower(), row['Light / Heavy sleeper '].lower(), row['Morning / Night person?'].lower(), row['Clean / Messy?'].lower(), row['Down to Party?'].lower(), row['Can you cook?'].lower(), row['Gym buddies? '].lower(), row['Weekend spent? '].lower(), row['Fav Music'].lower()])
      
#compare str
def strcmp(subj, obj):
    subjtmp = subj.replace(',', '').replace('(', '').replace(')', '').replace('/', ' ').split(" ")
    objtmp = obj.replace(',', '').replace('(', '').replace(')', '').replace('/', ' ').split(" ")
    for i in range(len(subjtmp)):
        if subjtmp[i] in objtmp and subjtmp[i] not in excpt:
            return 1
    return 0

#compare common positives
def poscmp(subj, obj):
    pos = ['down', 'yes', 'ye', 'yeah', 'sure', 'probably', 'planning', 'practice', 'time', 'love', 'make', 'please', '']
    subjtmp = subj.replace(',', '').replace('(', '').replace(')', '').replace('/', ' ').split(" ")
    objtmp = obj.replace(',', '').replace('(', '').replace(')', '').replace('/', ' ').split(" ")
    for i in range(len(subjtmp)):
        for j in range(len(objtmp)):
            if subjtmp[i] in pos and objtmp[j] in pos and subjtmp[i]:
                return 1
    return 0

#compare a/b
def abcmp(subj, obj, a, b):
    if a in subj and a in obj:
        return 1
    elif b in subj and b in obj:
        return 1
    elif a in subj and b in obj:
        return -1
    elif b in subj and a in obj:
        return -1
    return 0

#compare major
def majcmp(subj, obj):
    #abbreviations
    maj = [['cs', 'computer', 'science'], ['tech', 'technology', 'polytech', 'polytechnic'], ['fye', 'engineering', 'ae', 'me', 'aero/astro', 'aero', 'astro', 'mechanical', 'meche', 'industrial', 'Chem', 'chemical' 'nuclear',]]

    #prep strings
    subjtmp = subj.replace(',', '').replace('(', '').replace(')', '').replace('/', ' ').split(" ")
    objtmp = obj.replace(',', '').replace('(', '').replace(')', '').replace('/', ' ').split(" ")

    #compare strings
    for i in range(len(subjtmp)):
        if subjtmp[i] in objtmp and subjtmp[i] not in excpt:
            return 1
        for j in range(len(maj)):
            if subjtmp[i] in maj[j]:
                for k in range(len(maj[j])):
                    if maj[j][k] in objtmp:
                        return 1
    return 0    

#compare weekends
def wkndcmp(subj, obj):
    subjtmp = subj.replace(',', '').replace('(', '').replace(')', '').replace('/', ' ').split(" ")
    objtmp = obj.replace(',', '').replace('(', '').replace(')', '').replace('/', ' ').split(" ")
    sim = 0
    
    #create similar word lists
    act = [['bike' 'biking', 'hiking', 'outdoors', 'outdoorsy', 'fishing'], ['video', 'games', 'game', 'gaming', 'lol', 'league', 'minecraft', 'videogames', 'csgo'], ['study', 'studying', 'school', 'reading'], ['friend, friends', 'hanging', 'chilling', 'chillin', 'hang', 'parties', 'party', 'social', 'events'], ['coding', '3d', 'project', 'projects', 'engineering', 'programming'], ['movie', 'movies', 'tv', 'shows', 'binging', 'netflix', 'youtube', 'anime'], ['sports', 'sport', 'intramural', 'intramurals', 'football', 'baseball', 'basketball', 'soccer', 'swim', 'hockey', 'skating', 'riding', 'out', 'gym', 'skateboarding', 'climbing', 'tennis']]

    #compare all similar words
    for i in range(len(subjtmp)):
        if subjtmp[i] in objtmp and subjtmp[i] not in excpt:
            sim+=1
    for j in range(len(act)):
        for k in range(len(act[j])):
            if act[j][k] in subjtmp and act[j][k] in objtmp:
                sim+=1
    #print(subjtmp, objtmp, sim)
    return round(sim)

def write(Scores):
    with open('roomatedata.csv', 'w', newline = '') as datafile:
        datawriter = csv.writer(datafile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        #Get Names Header
        names = [0]
        for i in range(len(Scores)):
            names.append(Scores[i][0])
        datawriter.writerow(names)

        #Fill in data
        for i in range(len(Scores)):
            datawriter.writerow(Scores[i])

#main
Stud = []
Scores = []

load('raw/purdueE.csv')

#Compare Students
for i in range(len(Stud)):

    #Create new student for score recording
    CurrStud = [Stud[i][0]]

    #initate new obbject student
    for j in range(len(Stud)):
        Score = 0

        #compare LC
        Score += 5*strcmp(Stud[i][1], Stud[j][1])

        #!compare Major
        Score += majcmp(Stud[i][2], Stud[j][2])

        #compare rushing
        Score += abcmp(Stud[i][3], Stud[j][3], 'ye', 'no')

        #compare i/e
        Score += abcmp(Stud[i][4], Stud[j][4], 'in', 'ex')

        #compare sleep
        Score += abcmp(Stud[i][5], Stud[j][5], 'li', 'he')

        #compare morning/night
        Score += abcmp(Stud[i][6], Stud[j][6], 'mo', 'ni')

        #compare cleanliness
        Score += abcmp(Stud[i][7], Stud[j][7], 'cl', 'me')

        #compare party
        Score += poscmp(Stud[i][8], Stud[j][8])

        #!compare cooking
        Score += poscmp(Stud[i][9], Stud[j][9])

        #!compare gym
        Score += poscmp(Stud[i][10], Stud[j][10])

        #!compare weekends
        Score += wkndcmp(Stud[i][11], Stud[j][11])

        #compare music
        Score += 2*strcmp(Stud[i][12], Stud[j][12])

        #record score for subj-obj pair
        CurrStud.append(Score)

    Scores.append(CurrStud)

#finish
write(Scores)
print('Done')
