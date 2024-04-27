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
        title = patent.find_element(By.CSS_SELECTOR, "a.snippet-title").text
        link = patent.find_element(By.CSS_SELECTOR, "a.snippet-title").get_attribute("href")
        id = patent.find_element(By.CSS_SELECTOR, "span.subtitle-item.subtitle-item__desktop.subtitle-item__url").text.replace(" ", '')
        author = patent.find_elements(By.CSS_SELECTOR, "span.subtitle-item.subtitle-item__desktop.subtitle-item__minor")[-1].text.replace(" • ", '')
        dates = patent.find_elements(By.CSS_SELECTOR, "span.date-item__desktop")
        commit_date = dates[0].text
        publication_date = dates[1].text
        start_date = dates[2].text if len(dates) >= 3 else None
        

        return {
            "title": title,
            "link": link,
            "id": id,
            "author": author,
            "commit": commit_date,
            "publication": publication_date,
            "start": start_date
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


    
        

