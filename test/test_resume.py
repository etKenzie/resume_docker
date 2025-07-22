import requests

url = "http://localhost:9000/"  # Adjust port/path if needed

# Sample job description
job_description = """
SALES OFFICER

KUALIFIKASI
1.PRIA/WANITA
2UMUR MAKS 30
3.PENDIDIKAN MIN SMA
4.PENGALAMAN MIN 1 TAHUN
"""
target_skills=["Communication", "Emotional Intelligence", "Leadership", "Project Management", "Teamwork", "Strategic Planning", "Time Management", "Operations Management", "Creativity", "Sales & Lead Generation"]
target_skills_2 = ["football", "coaching", "leadership"]


data = {
    "resume_text": """DINDIN MOCH WALUDIN
CONTACT
083861084187
dindinmw20@gmail.com
JL. BBK PRIANGAN RT 07 RW 01
EDUCATION
2018
SMA SEBELAS MARET
IPS 2015
SMP PASUNDAN 1 BANDUNG 2012
SDN BABAKAN PRIANGAN 5
SKILLS
Project Management Public Relations Teamwork
Time Management Leadership
Effective Communication Critical Thinking
LANGUAGES
English (Basic)
PROFILE
Let me introduce myself, my name is Dindin, I am now 25 years old, I am the third child of 3 siblings. My hobby is playing sports, such as futsal, badminton, for my daily life. Currently I am selling second-hand clothes, most recently I worked at First Media as a sales company for 1 year.
WORK EXPERIENCE
First media Sales Marketing
Offers door to door wifi installation to customers
2023 - 2025
Promoting and selling WiFi and broadband services to potential customers. identifying sales opportunities, managing customer relationships, and meeting sales targets to drive service adoption.
J&T EXPRESS
• Warehouse
2020 - 2023
Sorting packages in the warehouse area to be given to the respective area couriers
Responsible for receiving, sorting, storing, and dispatching parcels. Maintaining inventory accuracy, ensuring proper packaging, and supporting efficient logistics operations to meet delivery targets.
SUMO SQUID Cashier
2019 - 2020
Serve customers who will place orders and make payments""",
    "job_description": job_description,
    "target_skills": target_skills
}

# If your endpoint expects multiple target_skills as repeated keys, use:
# data = [
#     ("resume_text", "I am a Python developer with 3 years of experience."),
#     ("job_description", "We are looking for an experienced Python developer with FastAPI skills."),
#     ("target_skills", "Python"),
#     ("target_skills", "FastAPI"),
#     ("target_skills", "REST"),
# ]

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(url, data=data, headers=headers)
print(response.status_code)
print(response.text)