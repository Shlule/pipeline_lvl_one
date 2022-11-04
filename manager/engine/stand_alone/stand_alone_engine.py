from manager.engine.base_engine import  BaseEngine
import os
from manager.core import resolver
class StandAloneEngine:

    def __init__(self):
        #declaratif, of different function that user will use
        self.implements =['open', 'build']


        print ("je suis un standAloneEngine")
    def open(self, entity):
        """

        :param path: on donne le path que l'on souhaite ouvrir
        :return: ca nous ouvre le fichier
        """
        path = resolver.format(entity)
        print(type(path))
        #print('start '+ path)
        os.system('start '+ path)

    def build(self, entity):
        print(entity)
