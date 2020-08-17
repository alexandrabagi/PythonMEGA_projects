replies = []

def sentence_maker(phrase):
    interrogatives = ("how", "what", "where", "why", "when")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        user_input = sentence_maker(user_input)
        replies.append(user_input)
        continue

print(" ".join(replies))
   