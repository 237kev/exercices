"""
Forwarded this email? Subscribe here for more
You’re currently a free subscriber. If you like today’s article, consider upgrading to paid to unlock project code solutions.

Upgrade to paid

Password Strength Checker with NLTK and Regex
Level 3: Real-World
Dec 26





READ IN APP

Project Level 3: Real-World
This project is designed for learners who know Python fundamentals and are learning to build real-world programs.

Project Description
Build a command-line application that evaluates the strength of a password entered by the user. The app will analyze the password based on these criteria:

Length (at least 8 characters long)

The inclusion of uppercase and lowercase letters, numbers, special characters (using the re regular expression library)

Dictionary word detection (the program uses the nltk library to detect if the user is using any common English words and it will not accept such words to make the password more secure).

Here is an example when the user submits a weak password (e.g., mypass):"""

import re
import nltk
from nltk.corpus import words


def passwort_check(word: str )-> bool:
    check = {
        "password_len": False,
        "has_lower": False,
        "has_upper": False,
        "has_digit": False,
        "has_special": False,
        "no_common_word": True  # New rule: Password should not be a dictionary word
    }
    pattern = r"[!@#$%^&*()_+={}\[\]:;\"'<>,.?/\\|`~\-]"

    nltk.download("words")
    english_words = set(word.lower() for word in words.words())
    print("asgawrggg" in english_words)  # Should return True

    # Check if the password is a common dictionary word
    if word.lower() in english_words:
        check["no_common_word"] = False
        print(f"no_common word: {check['no_common_word']}")
    if len(word) > 7:
        check['password_len'] = True
    for i in word:
        if i.islower() :
            check['has_lower'] = True
            print('passwort contain lower case')
        if i.isupper():
            check['has_upper'] = True
            print('passwort contain upper')

        if i.isdigit():
            check['has_digit']=True
            print('passwort contain digit')

    if re.search(pattern,word):
            check['has_special']=True
            print('special caracter')

    # Print the status
    for key, value in check.items():
        if value:
            print(f"✅ {key.replace('_', ' ').capitalize()} detected")
        else:
            print(f"❌ {key.replace('_', ' ').capitalize()} missing")



    check_pass_value = check.values()
    if any(check_pass_value):
        print('passwort OK')
        return True
    else: return False

while True:
    password_entered = input("enter your password: ")

    if passwort_check(password_entered):
        print('STRONG PASSWORT')
    else :
        print('WEAK PASSWORT')
        break
