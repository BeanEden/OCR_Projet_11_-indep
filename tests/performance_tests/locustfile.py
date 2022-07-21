from locust import HttpUser, task

<<<<<<< HEAD
# <<<<<<< HEAD

valid_email = "admin@irontemple.com"
# =======
club = "Iron Temple"
competition = "Spring Festival"
places_bought = 1
# >>>>>>> BUG_Clubs_should_not_be_able_to_use_more_than_their_points_allowed
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
# <<<<<<< HEAD
    def showSummary(self):
        response = self.client.post('/showSummary', data={'email': [valid_email]})

    @task(6)
    def logout(self):
        self.client.get("/logout")
# =======
    def purchasePlace(self):
        response = self.client.post('/purchasePlaces', data=dict(club=club, competition=competition, places=places_bought))
# >>>>>>> BUG_Clubs_should_not_be_able_to_use_more_than_their_points_allowed
=======
    def purchasePlace(self):
        response = self.client.post('/purchasePlaces', data=dict(club=club, competition=competition, places=places_bought))
>>>>>>> BUG_Point_updates_are_not_reflected
