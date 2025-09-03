import pandas as pd
import numpy as np
from faker import Faker
from tqdm import tqdm
import random
import os

fake = Faker()
NUM_CANDIDATES = 100_000
NUM_JOBS = 2_000
NUM_RECRUITERS = 500
NUM_APPLICATIONS = 300_000
NUM_INTERVIEWS = 250_000
NUM_FEEDBACKS = 200_000

os.makedirs("output", exist_ok=True)

# 1. Candidates
candidates = pd.DataFrame({
    "candidate_id": range(1, NUM_CANDIDATES + 1),
    "full_name": [fake.name() for _ in range(NUM_CANDIDATES)],
    "email": [fake.email() for _ in range(NUM_CANDIDATES)],
    "phone": [fake.phone_number() for _ in range(NUM_CANDIDATES)],
    "education_level": [random.choice(["Bachelors", "Masters", "PhD", "Diploma"]) for _ in range(NUM_CANDIDATES)],
    "years_of_experience": np.random.randint(0, 20, size=NUM_CANDIDATES)
})
candidates.to_csv("output/candidates.csv", index=False)

# 2. Jobs
jobs = pd.DataFrame({
    "job_id": range(1, NUM_JOBS + 1),
    "job_title": [fake.job() for _ in range(NUM_JOBS)],
    "department": [random.choice(["Engineering", "Sales", "HR", "Marketing", "Product"]) for _ in range(NUM_JOBS)],
    "location": [fake.city() for _ in range(NUM_JOBS)],
    "salary": np.random.randint(40000, 150000, size=NUM_JOBS)
})
jobs.to_csv("output/jobs.csv", index=False)

# 3. Recruiters
recruiters = pd.DataFrame({
    "recruiter_id": range(1, NUM_RECRUITERS + 1),
    "recruiter_name": [fake.name() for _ in range(NUM_RECRUITERS)],
    "email": [fake.company_email() for _ in range(NUM_RECRUITERS)],
    "region": [random.choice(["APAC", "NA", "EMEA", "LATAM"]) for _ in range(NUM_RECRUITERS)]
})
recruiters.to_csv("output/recruiters.csv", index=False)

# 4. Applications
applications = pd.DataFrame({
    "application_id": range(1, NUM_APPLICATIONS + 1),
    "candidate_id": np.random.randint(1, NUM_CANDIDATES + 1, NUM_APPLICATIONS),
    "job_id": np.random.randint(1, NUM_JOBS + 1, NUM_APPLICATIONS),
    "recruiter_id": np.random.randint(1, NUM_RECRUITERS + 1, NUM_APPLICATIONS),
    "application_date": [fake.date_this_year() for _ in range(NUM_APPLICATIONS)]
})
applications.to_csv("output/applications.csv", index=False)

# 5. Interviews
interviews = pd.DataFrame({
    "interview_id": range(1, NUM_INTERVIEWS + 1),
    "application_id": np.random.randint(1, NUM_APPLICATIONS + 1, NUM_INTERVIEWS),
    "interview_stage": [random.choice(["Screening", "Technical", "Managerial", "HR"]) for _ in range(NUM_INTERVIEWS)],
    "interview_date": [fake.date_this_year() for _ in range(NUM_INTERVIEWS)],
    "interviewer": [fake.name() for _ in range(NUM_INTERVIEWS)]
})
interviews.to_csv("output/interviews.csv", index=False)

# 6. Feedback
feedback = pd.DataFrame({
    "feedback_id": range(1, NUM_FEEDBACKS + 1),
    "interview_id": np.random.randint(1, NUM_INTERVIEWS + 1, NUM_FEEDBACKS),
    "score": np.random.randint(1, 6, size=NUM_FEEDBACKS),
    "remarks": [fake.sentence() for _ in range(NUM_FEEDBACKS)]
})
feedback.to_csv("output/feedback.csv", index=False)

print("✅ Recruitment dataset generated in 'output/' folder")
