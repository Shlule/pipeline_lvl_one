from pathlib import Path
import glob
import os

import manager.conf as conf
from manager.core import resolver

#la variable extension est une liste car nous pouvons chercher
#tout les fichier avec des extension differente.
def get_files (project_name, extension_list=["*"]):
    """

    :param project_name:  is the official name of the project maybe diferent that the file name
    :param extensions: different extension like .py .cpp .ma etc must remove "." and must be a list example['ma']
    :return: generator which contain all path in the project with the chose extension

    """

    project_path = Path(conf.project_root) / conf.projects.get(project_name)
    #create tampon list wich contain our future generator
    generators=[]
    for ext in extension_list:

        shots_pattern = conf.shots_file_pattern.format(ext=ext)
        #globbing with pathlib this create generator
        found = Path(project_path).rglob(shots_pattern)
        print(shots_pattern)
        #put our generator in our tampon list
        generators.append(found)

        #do the same thing for the Asset
        asset_pattern = conf.assets_file_pattern.format(ext=ext)
        fo = Path(project_path).rglob(asset_pattern)
        generators.append(fo)

    #read our tanpom list composed of generator
    for g in generators:
        #read generator
        for f in g:
            yield f


def get_entities(project_name, extension_list=["*"]):
    """

    :param entity_type: Type string ;  name of the entity selected exemple {categorie} or {asset_name} etc.
    :return: list of entities

    """
    files = get_files(project_name, extension_list)
    for file in files:
        data = resolver.parse(file)
        if data:
            yield data


def get_categorie(project,type):
    """
    :param project: put the project name
    :param type: Type string; est le type de données demander souvent assets ou shaots
    :return:
    """
    m_path = Path(conf.project_root) / project / type
    print (m_path)
    x = glob.glob(str(m_path)+'/*')
    print(x)

def new_get_entities(project, type, entity_type):
    """

    :param project: is the project_name
    :param type: Type string; est le type de données demander souvent assets ou shots
    :param entity_type: is the name in reslver template {categorie} etc.
    :return:
    """
    if(entity_type == 'categorie' or entity_type == 'sequence'):
        get_categorie(project,type)
    else:
        print('doesnt entity type')





if __name__ == '__main__':

    x ='Microfilms'
    y='shots'
    new_get_entities(x,y,'sequence')
