import requests
import hashlib
import webbrowser
import urllib

class Marvel(object):
	"""
	Esta clase consume el API de MArvel Comics
	"""

	def __init__(self):
		self.public_key = 'cb22ec41e8485872ebda6946c6573058'
		self.private_key = 'a5adfa1b3edb4d0e2232a20cd276fa5e156a4a5e'
		self.ts = '1'
		self.ha = hashlib.md5((self.ts+self.private_key+self.public_key).encode()).hexdigest()
		self.url = 'http://gateway.marvel.com/v1/public/'
		# Variables que voy ocupando
		self.personaje = ''

	def get_personaje(self,nombre):
		try:
			paramsencode={
						'ts':self.ts,
						'apikey':self.public_key,
						'hash':self.ha,
						'name':nombre
					}
			paramsencode=urllib.urlencode(paramsencode)
			print(paramsencode)
			self.personaje = requests.get(
					self.url+'characters',
					params=paramsencode).json()
			# print(self.personaje)
			description = self.personaje['data']['results'][0]['description']
			return description
		except:
			return 'Escribe bien cabron'

	def get_imagen(self):
		try: 
			return self.personaje['data']['results'][0]['thumbnail']['path']+'.'+self.personaje['data']['results'][0]['thumbnail']['extension']
		except:
			return ''