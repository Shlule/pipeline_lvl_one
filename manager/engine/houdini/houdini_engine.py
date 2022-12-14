from manager.engine.base_engine import  BaseEngine
from manager.core import resolver
import hou


class HoudiniEngine(BaseEngine):



    def __init__(self):

        self.implements =['open','merge', 'saveAndIncrement']
        print("je suis un houdiniEngine")


    def open(self , entity):
        path = resolver.format(entity, resolver.files_templates)
        hou.load(path)
        print("open button pressed ")

    def merge(self, entity):
        path = resolver.format(entity, resolver.files_templates)
        hou.hipFile.merge(path)
        print("merge button pressed")

    def saveAndIncrement(self,entity):
        path = resolver.format(entity,resolver.files_templates)
        hou.hipFile.saveAndIncrementFileName()
        print("saveAndIncrement button pressed")