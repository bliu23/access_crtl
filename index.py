import auroraapi as aurora
from auroraapi.text import Text
from auroraapi.speech import listen
from auroraapi.speech import listen_and_transcribe, continuously_listen_and_transcribe
from auroraapi.speech import continuously_listen_and_transcribe


# Set your application settings
aurora.config.app_id    = "4af504f9150847924d290fcd5eac6b96"     # put your app ID here
aurora.config.app_token = "bbIt079lilS0l7lLHzVHIuDcJCHWm"  # put your app token here

captchaPhrase = "banana"


def getInput():
	print ("Please repeat the captcha.")
	speech = listen(length=2)

	prediction = speech.text()
	return prediction.text

def playCaptcha(phrase):	
	speech = Text(phrase).speech()
	speech.audio.play()

def compare(phrase, input):
	return phrase.lower() == input.lower()

def captcha(phrase):
	playCaptcha(captchaPhrase)
	userInput = getInput()
	return compare(captchaPhrase, userInput)

if captcha(captchaPhrase):
	print("Success")
else:
	print("Fail")


