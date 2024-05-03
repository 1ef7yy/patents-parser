import csv

def write_to_csv(file_name, data):
    with open(file_name, "a", encoding="utf-8", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(data[0].keys()))
        for patent in data:
            writer.writerow(patent)


def initialize(file_name):
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("Название,Ссылка,Id,Автор,Дата подачи,Дата публикации")
        f.write("\n")