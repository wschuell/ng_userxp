import random
import time
from locust import HttpLocust, TaskSet, task

def get_js_strvar(response,var):
    return str(response.content).split("var " + var + " = \"")[1].split('"')[0]

def get_page_type(response):
    http_str = str(response.content)
    try:
        role = http_str.split("<span id=\"role\">")[1].split('</span>')[0]
        if role == "":
            return "skipped"
        else:
            return role
    except:
        nb_played = http_str.split("<span id=\"nbr_played\">")[1].split('</span>')[0]
        print(http_str.split("<span id=\"texte_score\">")[1].split('</h2>')[0])
        return"final_results"


class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()
        self.tuto_played = False

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
    def xp_basic(self):
        self.tuto_played = True
        return self.xp(xp_type="basic")

    @task(2)
    def xp_normal(self):
        if self.tuto_played:
            for i in range(7):
                self.xp(xp_type="normal")
            return self.client.get('/infos/')

    def xp(self,xp_type):
        response = self.client.get("/new_experiment/"+xp_type)
        m = None
        try:
            url_continue = get_js_strvar(response=response,var="url_continue")
        except:
            raise ValueError(response.content)
        url_hr = get_js_strvar(response=response,var="url_results_hearer_base")
        url_sp = get_js_strvar(response=response,var="url_results_speaker_base")
        page = get_page_type(response)
        while page != "final_results":
            if m is None and page != 'skipped':
                m = str(response.content).split("meaning_name=\"")[1].split('"')[0]
            time.sleep(0.1)
            if page == 'speaker':
                self.client.get(url_sp+m+'-locust0/results_continue/')
                time.sleep(0.1)
                response = self.client.get(url_continue)
            elif page == 'hearer':
                self.client.get(url_hr+m+'/results_continue/')
                time.sleep(0.1)
                response = self.client.get(url_continue)
            elif page == 'skipped':
                response = self.client.get(url_continue)
            page = get_page_type(response)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 500
    max_wait = 900
