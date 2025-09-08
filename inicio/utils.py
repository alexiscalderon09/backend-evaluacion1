from datetime import date

def calcular_anios_experiencia(desde: int) -> int:
    return max(0, date.today().year - desde)

def top_skills(skills: list[str], limite: int = 5) -> list[str]:
    return skills[:limite] if len(skills) >= limite else skills
