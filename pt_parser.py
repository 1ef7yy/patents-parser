from selenium import webdriver
from selenium.webdriver.common.by import By

import time


class PatentsParser:
    def __init__(self, patent_name, pages):
        self.link = f"https://yandex.ru/patents?text={patent_name}&spp=50"

        self.driver = webdriver.Chrome()
        self.pages = pages

        self.patents = []

    def next_page(self):
        button = self.driver.find_element(By.CLASS_NAME, "leaf-button__next")
        button.click()


    def get_patents(self):
        return self.driver.find_elements(By.CLASS_NAME, "snippet-block")



    def get_data(self, patent):
        link = patent.find_element(By.CSS_SELECTOR, "a.snippet-title").get_attribute("href")


        return {
            "link": link
        }
    

    def parse(self):
        self.driver.get(self.link)
        time.sleep(5)

        for _ in range(self.pages):
            patents = self.get_patents()
            for patent in patents:
                self.patents.append(self.get_data(patent))

            self.next_page()

        return self.patents


    
        



my_parser = PatentsParser("оружие", 3)

print(len(my_parser.test()))
