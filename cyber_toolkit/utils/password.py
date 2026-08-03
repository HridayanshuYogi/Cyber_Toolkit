import re

def check_password_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"[0-9]", password): score += 1
    if re.search(r"[{}[\]:;.,?~_+\-=!@#$%^&*()]", password): score += 1
    
    strengths = {1: "Very Weak", 2: "Weak", 3: "Medium", 4: "Strong", 5: "Very Strong"}
    return strengths.get(score, "Very Weak")