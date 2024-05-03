# -*- coding: utf-8 -*-

import pt_parser as parser
import excel


if __name__ == "__main__":
    patent_parser = parser.PatentsParser("оружие", 30)

    file_name = "patents.csv"

    excel.initialize(file_name)

    for page in range(1, patent_parser.pages+1):
        patent_parser.get_page(page, try_num=0)
        patents = patent_parser.parse()
        excel.write_to_csv(file_name=file_name, data=patents)
        print(f"Страница №{page} записана в csv файл!")
        
    