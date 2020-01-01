
import unittest
import os, signal
import time
import subprocess
from selenium import webdriver

class DevHealthTest(unittest.TestCase):

    # os.system(f"docker-compose -f {cls.docker_file_directory} down -v")
    @classmethod
    def setUpClass(cls) -> None:
        cls.doc_comp_file = 'docker_compose_files/docker-compose.demo.yml'
        cls.app_name = 'demo_app'
        os.system(f"docker-compose -f {cls.doc_comp_file} build")
        cls.container = subprocess.Popen(f"docker-compose -f {cls.doc_comp_file} up", shell=True)
        time.sleep(5)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.container.kill()
        os.system(f"docker kill {cls.app_name}")

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(4)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_server_live(self):
        self.browser.get('http://localhost')
        time.sleep(1)
        self.assertIn('APAX HRS', self.browser.title, self.browser.title)
        self.browser.implicitly_wait(1)

if __name__ == '__main__': #
    unittest.main(warnings='ignore') #

