import re

def clean_skills(skills):
    # Example of standardizing skill names
    skills = [re.sub(r'\s+', ' ', skill.strip()).lower() for skill in skills]
    return skills

# Apply cleaning to your candidate data
cleaned_candidates = [
    {
        "name": candidate["name"],
        "skills": clean_skills(candidate["skills"]),
        "experience": candidate["experience"],
        "job_title": candidate["job_title"].lower()
    }
    for candidate in candidates
]
