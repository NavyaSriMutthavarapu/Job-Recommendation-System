# skill_utils.py

from role_data import job_roles


# 🔹 Optional: skill normalization (basic mapping)
skill_aliases = {
    "ml": "machine learning",
    "ai": "artificial intelligence",
    "js": "javascript"
}


def preprocess_skills(user_input):
    """
    Converts input string to cleaned skill list
    """
    skills = user_input.lower().split()
    
    # Apply alias mapping
    processed = []
    for skill in skills:
        processed.append(skill_aliases.get(skill, skill))
    
    return processed


def get_skill_gap(role, user_input):
    """
    Improved matching with preprocessing
    """
    
    required_skills = job_roles[role]["skills_required"]
    
    user_skills = preprocess_skills(user_input)
    
    missing_skills = []
    
    for req in required_skills:
        if not any(req in user_skill for user_skill in user_skills):
            missing_skills.append(req)
    
    return required_skills, missing_skills


def get_career_guidance(missing_skills):
    """
    Generates simple learning guidance
    """
    
    guidance = []
    
    for skill in missing_skills:
        guidance.append(f"Learn {skill}")
    
    return guidance