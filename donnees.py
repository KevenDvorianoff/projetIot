import requests

def envoyer(instrument,temps):
	requests.post("https://docs.google.com/forms/d/1G4nCAhnfutmmatkeVAmjOuKEkUk5dJkxOEAE86bffHA/formResponse?ifq&entry.703430851={}&entry.2075846651={}&submit=Submit".format(instrument,temps))