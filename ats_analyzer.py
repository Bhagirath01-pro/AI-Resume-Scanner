import re


SKILLS = [
    "python",
    "java",
    "c++",
    "sql",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "power bi",
    "tableau",
    "excel",
    "html",
    "css",
    "javascript",
    "git",
    "github",
    "communication",
    "teamwork"
]


def find_skills(text):
    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        pattern = r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)"

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills


def calculate_match_score(resume_text, job_description):

    resume_skills = find_skills(resume_text)
    job_skills = find_skills(job_description)

    matching_skills = list(
        set(resume_skills).intersection(set(job_skills))
    )

    missing_skills = list(
        set(job_skills).difference(set(resume_skills))
    )

    if len(job_skills) == 0:
        score = 0
    else:
        score = (len(matching_skills) / len(job_skills)) * 100

    return (
        round(score, 2),
        matching_skills,
        missing_skills
    )