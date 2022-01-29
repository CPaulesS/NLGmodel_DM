def check_punctuation(message):
    last_character = message[-1]
    if last_character != "." and last_character != "?" and last_character != "!":
        message += "."
    return message

def correct_response(text_generated):
    response = text_generated.split("\n")
    if response[0].isspace():
        return response[1]
    else:
        return response[0]