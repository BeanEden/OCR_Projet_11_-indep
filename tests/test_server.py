import pytest
from server import app


valid_email = "admin@irontemple.com"
unvalid_email = "unvalidmail"
unregistered_mail = "unregistered_mail@irontemple.com"

from server import date_str_split, datetime_check


valid_email = "admin@irontemple.com"

from tests.utilities.db_manage import get_club


club = "Simply Lift"
competition = "Spring Festival"



club = "Iron Temple"
competition = "Spring Festival"


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
def test_get_index_page(client):
    rv = client.get('/')
    assert rv.status_code == 200


def test_showSummary_valid_mail(client):
    rv = client.post('/showSummary', data={'email': [valid_email]})
    data = rv.data.decode()
    assert rv.status_code == 200
    assert data.find('<p>Sorry, that email wasn&#39;t found.</p>') == -1


def test_showSummary_unvalid_email(client):
    rv = client.post('/showSummary', data={'email': [unvalid_email]})
    data = rv.data.decode()
    assert rv.status_code == 200
    assert data.find('<p>Sorry, that email wasn&#39;t found.</p>') != -1


def test_showSummary_unregistered_mail(client):
    rv = client.post('/showSummary', data={'email': [unregistered_mail]})
    data = rv.data.decode()
    assert rv.status_code == 200
    assert data.find('<p>Sorry, that email wasn&#39;t found.</p>') != -1
=======
def test_date_str_split():
    date_clean = "2020-03-27 10:00:00"
    date_datetime_str = "2020-03-27 10:00:00.134247"
    expected_value = "202003271000"

    assert date_str_split(date_clean) == expected_value
    assert date_str_split(date_datetime_str) == expected_value


def test_datetime_check():
    competition_open = {'date': "2024-03-27 10:00:00"}
    competition_closed_year = {'date': "2020-03-27 10:00:00"}
    competition_closed_month = {'date': "2022-03-27 10:00:00"}

    assert datetime_check(competition_open)['status'] == 'open'
    assert datetime_check(competition_closed_year)['status'] == 'closed'
    assert datetime_check(competition_closed_month)['status'] == 'closed'


def test_showSummary(client):
    rv = client.post('/showSummary', data={'email': [valid_email]})
    data = rv.data.decode()
    assert rv.status_code == 200
    assert data.find('<a href="/book/Spring%20Festival/Iron%20Temple">Book Places</a>') != -1
>>>>>>> BUG_Booking_places_in_past_competitions
=======
def test_purchasePlace_booking_should_work(client):
    places_bought = 2
    club_base = get_club(club)
    rv = client.post('/purchasePlaces', data=dict(club=club, competition=competition, places=places_bought))
    data = rv.data.decode()
    points = club_base['points']
    message = 'Points available: ' + str(points-places_bought)
    assert rv.status_code == 200
    assert data.find('<li>Great-booking complete!</li>') != -1
    assert data.find(message) != -1
>>>>>>> BUG_Point_updates_are_not_reflected
=======
def test_purchasePlace_booking_should_work(client):
    places_bought = 1
    rv = client.post('/purchasePlaces', data=dict(club=club, competition=competition, places=places_bought))
    data = rv.data.decode()
    assert rv.status_code == 200
    assert data.find('<li>Great-booking complete!</li>') != -1


def test_purchasePlace_booking_impossible(client):
    places_bought = 50
    rv = client.post('/purchasePlaces', data=dict(club=club, competition=competition, places=places_bought))
    data = rv.data.decode()
    assert rv.status_code == 200
    assert data.find('<p>You don&#39;t have enough points to make this reservation</p>') != -1
>>>>>>> BUG_Clubs_should_not_be_able_to_use_more_than_their_points_allowed
