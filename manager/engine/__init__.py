import sys

def get():
    """
    this is a factory , we detect in witch context we are and the factory give us the good engine appropriate
    to the context example we are in maya it give us a maya engine.
    :return:
    """


    #get the .exe that we actuall working on
    my_env = sys.executable
    print(my_env)
    if(my_env == "C:\Autodesk\Maya2022\\bin\maya.exe"):
        from manager.engine.maya.maya_engine import MayaEngine
        return MayaEngine()

    else:
        print ("je suis en stand alone")
        from manager.engine.stand_alone.stand_alone_engine import StandAloneEngine
        return StandAloneEngine()

    selected ="dummy"
    #print(f'engine Factory selected:{selected}')

    return selected

if __name__ == '__main__':
    get()