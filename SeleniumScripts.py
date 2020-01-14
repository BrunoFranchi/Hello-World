import json
from selenium import webdriver

class SeleniumClass:
    def __init__(self):
        with open('My_file.json') as file_data:
            self.read_content = json.load(file_data)
        self.list_dict = []
        self.count = 0

    def web_search(self):
        for p in self.read_content['google-me']:
            self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
            self.driver.implicitly_wait(10)
            self.driver.get('https://google.com')
            self.driver.implicitly_wait(5)
            self.search = self.driver.find_element_by_name('q')
            self.search.send_keys(p)
            self.driver.implicitly_wait(2)
            self.driver.find_element_by_name('btnK').click()
            self.driver.implicitly_wait(2)
            self.t1 = self.driver.find_element_by_xpath(self.read_content[p][0]).text
            self.driver.implicitly_wait(2)
            self.t2 = self.driver.find_element_by_xpath(self.read_content[p][1]).text
            self.driver.implicitly_wait(2)
            self.t3 = self.driver.find_element_by_xpath(self.read_content[p][2]).text
            self.dicionario1 = {self.read_content['google-me'][self.count]: [self.t1, self.t2, self.t3]}
            self.count += 1

            print(
                f'\n Resultado: {self.t1}'
                f'\n Resultado: {self.t2}'
                f'\n Resultado: {self.t3}')
            self.driver.back()
            self.driver.implicitly_wait(3)
            self.driver.close()
            self.list_dict.append(self.dicionario1)

    def output_json(self):
        file = open("output.json", "w+", encoding='utf-8')
        file.write(json.dumps(self.list_dict, ensure_ascii=False, indent=4, sort_keys=True))

