from locust import HttpUser, task


<<<<<<< HEAD
valid_email = "admin@irontemple.com"


=======
>>>>>>> BUG_Booking_places_in_past_competitions
class ProjectPerfTest(HttpUser):

    @task(6)
    def index(self):
        self.client.get("/")

    @task(6)
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
