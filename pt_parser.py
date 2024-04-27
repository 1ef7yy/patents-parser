from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


class PatentsParser:
    def __init__(self, patent_name, pages):
        self.link = f"https://yandex.ru/patents?text={patent_name}&spp=200"

        self.driver = webdriver.Chrome()
        self.pages = pages

        self.patents = []

    def get_page(self, page_num, try_num):
        self.driver.get(self.link+f"&sp={page_num}")
        if try_num > 5:
            self.get_page(page_num+1, 0)
        try:
            element_present = EC.presence_of_element_located((By.CSS_SELECTOR, "a.snippet-title"))
            WebDriverWait(self.driver, 15).until(element_present)
        except Exception:
            self.get_page(page_num, try_num+1)

    def get_patents(self):
        return self.driver.find_elements(By.CLASS_NAME, "snippet-block")



    def get_data(self, patent):
        title = patent.find_element(By.CSS_SELECTOR, "a.snippet-title").text
        link = patent.find_element(By.CSS_SELECTOR, "a.snippet-title").get_attribute("href")
        id = patent.find_element(By.CSS_SELECTOR, "span.subtitle-item.subtitle-item__desktop.subtitle-item__url").text.replace(" ", '')
        author = patent.find_elements(By.CSS_SELECTOR, "span.subtitle-item.subtitle-item__desktop.subtitle-item__minor")[-1].text.replace(" • ", '') if len(patent.find_elements(By.CSS_SELECTOR, "span.subtitle-item.subtitle-item__desktop.subtitle-item__minor")) > 1 else None
        dates = patent.find_elements(By.CSS_SELECTOR, "span.date-item__desktop")
        commit_date = dates[0].text
        publication_date = dates[1].text if len(dates) > 1 else None
        

        return {
            "Название": title,
            "Ссылка": link,
            "Id": id,
            "Автор": author,
            "Дата подачи": commit_date,
            "Дата публикации": publication_date,
        }
    

    def parse(self):
        self.driver.get(self.link)
        time.sleep(5)

        for page in range(1, self.pages+1):
            patents = self.get_patents()
            for patent in patents:
                self.patents.append(self.get_data(patent))

            self.get_page(page+1, 0)

        return self.patents
