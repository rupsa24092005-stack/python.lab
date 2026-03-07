import requests
url = "https://arbeitnow.com/api/job-board-api"

response = requests.get(url)
data = response.json()

jobs = data["data"]

print("Latest JOb Listings \n")

for i in jobs[:5] :
    job_dict = {
        "title": i["title"],
        "job_type": i["job_types"],
        "company": i["company_name"],
        "location": i["location"],
        "remote": i["remote"],
        "tags": i["tags"],
        "url": i["url"],
    } 

    print("Job Title : ",job_dict["title"])
    print("Job type : ",job_dict["job_type"])
    print("company : ",job_dict["company"])
    print("location : ",job_dict["location"])
    print("remote : ",job_dict["remote"])
    print("Tags : ",job_dict["tags"])
    print("URL : ",job_dict["url"])
    print()
    print()