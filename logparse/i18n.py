"""Minimal message catalog (EN default, RU optional)."""
MESSAGES = {
    "en": {"parsed": "parsed lines", "top": "top paths"},
    "ru": {"parsed": "разобрано строк", "top": "популярные пути"},
}


def tr(lang: str, key: str) -> str:
    return MESSAGES.get(lang, MESSAGES["en"]).get(key, key)
