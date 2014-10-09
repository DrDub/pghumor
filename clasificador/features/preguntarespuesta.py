# -*- coding: utf-8 -*-
from __future__ import absolute_import
import re

from clasificador.features.feature import Feature

patron = re.compile(ur'^((-|—)\s*)?¿[^\?]+\?+[^¿\?]+$', re.UNICODE)


class PreguntaRespuesta(Feature):
    def __init__(self):
        super(PreguntaRespuesta, self).__init__()
        self.nombre = "PreguntaRespuesta"
        self.descripcion = """
            Esta característica mide si existe en el tweet preguntas y respuestas
        """

    def calcular_feature(self, tweet):
        tweet.features[self.nombre] = patron.search(tweet.texto) is not None