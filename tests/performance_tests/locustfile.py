from locust import HttpUser, task



valid_email = "admin@irontemple.com"
places_bought = 1
club = "Simply Lift"
competition = "Spring Festival"



class ProjectPerfTest(HttpUser):

    @task(6)
    def index(self):
        self.client.get("/")

    @task(6)
    def showSummary(self):
        response = self.client.post('/showSummary', data={'email': [valid_email]})

    @task(6)
    def logout(self):
        self.client.get("/logout")

    @task(6)
    def purchasePlace(self):
        response = self.client.post('/purchasePlaces', data=dict(club=club, competition=competition, places=places_bought))

    def clubsTable(self):
        response = self.client.get("/clubs")



