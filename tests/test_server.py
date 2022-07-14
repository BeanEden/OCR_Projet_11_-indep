import pytest
from server import app


<<<<<<< HEAD
valid_email = "admin@irontemple.com"
unvalid_email = "unvalidmail"
unregistered_mail = "unregistered_mail@irontemple.com"
=======
club = "Iron Temple"
competition = "Spring Festival"
>>>>>>> BUG_Clubs_should_not_be_able_to_use_more_than_their_points_allowed


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


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
