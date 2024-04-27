# -*- coding: utf-8 -*-

import pt_parser as parser
import excel


if __name__ == "__main__":
    patent_parser = parser.PatentsParser("оружие", 30)
    patents = patent_parser.parse()

    excel.write_to_csv(file_name="patents.csv", data=patents)
    