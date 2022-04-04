from django.test import TestCase, Client

# Create your tests here.

from bs4 import BeautifulSoup
from .models import TodayTasks
from .operating_files.obj_date import DateObj


class TestView(TestCase):

    def setUP(self):
        self.client = Client()

    # how to use test code
    def test_how_to_use(self):
        self.assertEqual(2, 2)

    def test_main(self):
        # 1.1   Success to open page - /mytasks/
        response = self.client.get('/mytasks/')
        self.assertEqual(response.status_code, 200)
        # 1.3   Title should be "mytasks"
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertIn('mytasks', soup.title.text)

    def test_main_today(self):
        # 2.1   Success to open page - /mytasks/(today_url)/
        today = DateObj()
        response = self.client.get('/mytasks/' + today.today_url + '/')
        self.assertEqual(response.status_code, 200)
        # 2.2   If there's no today task,
        self.assertEqual(TodayTasks.objects.count(), 0)
        # 2.2.1 show message - "There are no today tasks"
        soup = BeautifulSoup(response.content, 'html.parser')
        main_area = soup.find('div', id='main-area')
        self.assertIn('There are no today tasks', main_area.text)

        # 2.2   There are two tasks,
        task_001 = TodayTasks.objects.create(
            title="test",
        )
        task_002 = TodayTasks.objects.create(
            title="test",
        )
        self.assertEqual(TodayTasks.objects.count(), 2)
        # 2.2.1 When refresh page
        response = self.client.get('/mytasks/' + today.today_url + '/')
        soup = BeautifulSoup(response.content, 'html.parser')
        # 2.2.2 There are two title
        main_area = soup.find('div', id='main-area')
        self.assertIn(task_001.title, main_area.text)
        self.assertIn(task_002.title, main_area.text)
        # 2.2.3 Shouldn't be been message - "There are no today tasks"
        self.assertNotIn('There are no today tasks', main_area.text)

        # 3.1   If no global task, show message - "There's no global task"
        # 3.2   If there are global tasks, it should be shown
