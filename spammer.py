#!/usr/bin/python

# - Spammer v3.1
# | Description: spams a phone number by sending it a lot of sms by using Grab API
# | Author: UMAR.MG & Z fisher 🎭 
# | Date: 1/01/2025
# | Disclaimer: Editing author will not make you the real coder
# | What's New?
# | - Fixed 403 forbidden
# | - Use less CPU

import spammer_class
spammer = spammer_class.Spammer()
spammer.author = "UMAR.MG & Z fisher"
try:
    spammer.main()
except KeyboardInterrupt:
    print spammer_class.color.FAIL+spammer_class.color.REVERSE+"\r[!][except] KeyboardInterrupt detected! Exiting . . ."+spammer_class.color.ENDC+"\n"
    exit()
