import csv

def write_to_csv(file_name, data):
    with open(file_name, "w", encoding="utf-8", newline='') as f:
        writer = csv.DictWriter(
            f, fieldnames=list(data[0].keys()))
        
        writer.writeheader()

        for patent in data:
            writer.writerow(patent)
