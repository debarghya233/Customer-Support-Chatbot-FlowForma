def fallback_response(text, threshold=10):
    if len(text.strip()) < threshold:
        return "Sorry, I do not have an answer for that yet."
    return text
