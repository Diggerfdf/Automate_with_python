#! python3

import regex as re
import pyperclip

# Create regex for phone number

phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

(
((\d\d\d) | (\(\d\d\d\)))?     # area code (optional)
(\s|-)               # first separator
\d\d\d               # first 3 digits
-                    # separator
\d\d\d\d             # last 4 digits
((ext(\.)?\s | x)    # extension word part (optional)
(\d{2,5}))?          # extension number part(optional)
)
''', re.VERBOSE)

# Create a regex for e-mail address
emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5}))?.xxx

[a-zA-z0-9_.+]+   # name part
@                 # @ symbol
[a-zA-z0-9_.+]+   # Domain name part

''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# TODO: Extract the email/phone from this text
phoneRegex.findall(text)

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# TODO Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
