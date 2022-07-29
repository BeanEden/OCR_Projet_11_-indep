from locust import HttpUser, task

<<<<<<< HEAD

<<<<<<< HEAD
valid_email = "admin@irontemple.com"


=======
>>>>>>> BUG_Booking_places_in_past_competitions
=======
club = "Simply Lift"
competition = "Spring Festival"
places_bought = 2



>>>>>>> BUG_Point_updates_are_not_reflected
class ProjectPerfTest(HttpUser):

    @task(6)
    def index(self):
        self.client.get("/")

    @task(6)
<<<<<<< HEAD
<<<<<<< HEAD
    def showSummary(self):
        response = self.client.post('/showSummary', data={'email': [valid_email]})

    @task(6)
    def logout(self):
        self.client.get("/logout")
=======
    def clubsTable(self):
        response = self.client.get("/clubs")


>>>>>>> BUG_Booking_places_in_past_competitions
=======
    def purchasePlace(self):
        response = self.client.post('/purchasePlaces', data=dict(club=club, competition=competition, places=places_bought))
>>>>>>> BUG_Point_updates_are_not_reflected
