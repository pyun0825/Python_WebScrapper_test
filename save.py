import csv

def save_to_file(jobs):
    file = open("jobs.csv", "w")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "loaction", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return