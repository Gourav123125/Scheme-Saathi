import json

def load_schemes():
    with open("data/schemes.json", "r", encoding="utf-8") as f:
        return json.load(f)

def match_schemes(profile):
    schemes = load_schemes()
    matched = []

    for scheme in schemes:
        score = 0

        if scheme.get("occupation") == profile.get("occupation"):
            score += 1

        if scheme.get("gender") == profile.get("gender"):
            score += 1

        if scheme.get("education_level") == profile.get("education_level"):
            score += 1

        if "min_age" in scheme and profile.get("age", 0) >= scheme["min_age"]:
            score += 1

        if "max_land" in scheme and profile.get("land", 10) <= scheme["max_land"]:
            score += 1

        # Widow priority
        if "widow" in scheme.get("name", "").lower() and profile.get("widow"):
            score += 2

        if score > 0:
            matched.append((score, scheme))

    matched = sorted(matched, key=lambda x: x[0], reverse=True)
    return [item[1] for item in matched[:3]]
