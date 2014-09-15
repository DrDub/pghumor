from __future__ import absolute_import

import herramientas.utils
import re

class TreeTagger:

	def __init__(self, texto):
		command = 'echo "' + herramientas.utils.escapar(texto) + '" |  tree-tagger-spanish'
		resultado = herramientas.utils.ejecutarComando(command)
		self.tokens = []
		for line in resultado:
			matcheo = re.search('^(.*)\t(.*)\t(.*)\n', line)
			if matcheo != None:
				detalle = TokenTT()
				detalle.token = matcheo.group(1)
				detalle.tag = matcheo.group(2)
				detalle.lemma = matcheo.group(3)

				self.tokens.append(detalle)

#Datatype
class TokenTT:

	def __init__(self):
		self.token = ""
		self.tag = ""
		self.lemma = ""
