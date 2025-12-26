def extract_profile(user_input):
    profile = {}
    text = user_input.lower()

    # Occupation
    if "farmer" in text or "kisan" in text:
        profile["occupation"] = "farmer"

    if "worker" in text or "labour" in text:
        profile["occupation"] = "worker"

    # Gender
    if any(word in text for word in ["woman", "female", "girl", "widow"]):
        profile["gender"] = "female"

    # Widow
    if "widow" in text:
        profile["widow"] = True

    # Education
    if "student" in text or "school" in text:
        profile["education_level"] = "school"

    # Age detection
    for age in range(18, 101):
        if str(age) in text:
            profile["age"] = age
            break

    # Land
    if "land" in text or "hectare" in text:
        profile["land"] = 2

    return profile
