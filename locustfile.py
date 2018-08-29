from locust import HttpLocust, TaskSet, task
import random

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def login(self):
        response = self.client.get('/logout/')
        response = self.client.get('')
        self.client.headers['Referer'] = self.client.base_url
        #response = self.client.get('/login/')
        csrftoken = response.cookies['csrftoken']
        name_cookie_id = "locust_id_"+str(random.choice(list(range(20))))#response.cookies['NamingGameUser']
        #self.client.post('/accounts/login/',
        #                 {'username': 'username', 'password': 'password'},
        #                 headers={'X-CSRFToken': csrftoken})
        self.client.post("/login/", {"your_name":"locust_name_"+str(random.choice(list(range(20)))), "name_cookie_id":name_cookie_id,"lang":"en","code":"locust_test",
            'csrfmiddlewaretoken': csrftoken})

    @task(1)
    def story(self):
        self.client.get("/story")

    @task(1)
    def index(self):
        self.client.get("/new_experiment/basic")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 500
    max_wait = 900