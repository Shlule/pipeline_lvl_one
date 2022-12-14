from manager.engine.base_engine import  BaseEngine
import maya.cmds as cmds
from manager.core import resolver


class MayaEngine(BaseEngine):



    def __init__(self):

        self.implements =['open','build','reference']
        print("je suis une mayaEngineObject")


    def open(self , entity):
        print(entity)
        path = resolver.format(entity, resolver.files_templates)
        print(path)
        cmds.file(path ,open = True)
        print("open button pressed ")

    def reference(self , entity):
        path = resolver.format(entity, resolver.files_templates)
        print("je suis le button refrence")
        cmds.file(path, reference=True)

