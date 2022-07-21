import os
import json
<<<<<<< HEAD

=======
# from tests.test_server import club, competition, places_bought
>>>>>>> BUG_Clubs_shouldn't_be_able_to_book_more_than_12_places_per_competition

path = os.getcwd()
path = path.replace("utilities", "")


club = "Simply Lift"
<<<<<<< HEAD
=======
competition = "Spring Festival"
places_bought = 2
>>>>>>> BUG_Clubs_shouldn't_be_able_to_book_more_than_12_places_per_competition


def loadClubs():
    with open(path+'/database/clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


<<<<<<< HEAD
clubs = loadClubs()


def get_club(club):
    club = [c for c in clubs if c['name'] == club][0]
    return club
=======
def loadCompetitions():
    with open(path+'/database/competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


clubs = loadClubs()
competitions = loadCompetitions()


def reset_database(club, competition):
    club = [c for c in clubs if c['name'] == club][0]
    competition = [c for c in competitions if c['name'] == competition][0]

    club['points'] = 15
    competition['numberOfPlaces'] = 50
    for i in competition['clubsParticipating']:
        if club['name'] == i['club']:
            i['placesBooked'] = 1

    with open(path + '/database/competitions.json', "w") as cr:
        data = {'competitions': competitions}
        json.dump(data, cr)

    with open(path + '/database/clubs.json', "w") as cr:
        data = {'clubs': clubs}
        json.dump(data, cr)
>>>>>>> BUG_Clubs_shouldn't_be_able_to_book_more_than_12_places_per_competition
