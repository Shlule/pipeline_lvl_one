from pathlib import Path
import glob
import os

import manager.conf as conf
from manager.core import resolver
from manager.core.shotgun import connect_sg


def get_categorie(filter):
    """
    this function get the correct path directly in conf module

    :param filter Type dictionnary: contain all precedent entity we must get
    :return: list of path
    """
    path_pattern = conf.conf_files.globing_dictionary.get(list(conf.globing_dictionary.keys())[0])
    path = path_pattern.format(**filter)
    #path = path_pattern.format(project=filter.get('project'), type=filter.get('type'))
    result = glob.glob(path)
    return result

def get_asset_name(filter):
    """
    this function get the correct path directly in conf module

    :param filter Type dictionnary: contain all precedent entity we must get
    :return: list of path
    """
    path_pattern = conf.conf_files.globing_dictionary.get(list(conf.globing_dictionary.keys())[2])
    path = path_pattern.format(project=filter.get('project'), type=filter.get('type'),categorie=filter.get('categorie'))
    result = glob.glob(path)
    return result

def get_job(filter):
    """
    this function get the correct path directly in conf module

    :param filter Type dictionnary: contain all precedent entity we must get
    :return: list of path
    """
    path_pattern = conf.conf_files.globing_dictionary.get(list(conf.globing_dictionary.keys())[4])
    path = path_pattern.format(project=filter.get('project'),
                               type=filter.get('type'),
                               categorie=filter.get('categorie'),
                               asset_name=filter.get('asset_name'))
    result = glob.glob(path)
    return result
def get_files(filter, extension_list=["*"]):
    """
    this function get the correct path directly in conf module

    :param project: put the project name
    :param type: Type string; est le type de données demander souvent assets ou shaots
    :return: list of path
    """
    path_pattern = conf.conf_files.globing_dictionary.get(list(conf.globing_dictionary.keys())[5])
    generator_list =[]
    for ext in extension_list:
        path = path_pattern.format(**filter,
                                   ext=ext)
        found = glob.glob(path, recursive=True)
        generator_list.append(found)
    for generator in generator_list:
        for item in generator:
            yield item


def get_entities( entity_type, filter , extension_list=["*"],):
    """
    :param filter: type Dictionary
    :param project: is the project_name
    :param type: Type string; est le type de données demander souvent assets ou shots
    :param entity_type: is the name in resolver template {categorie} etc.
    :return: list of entity

    Warning: suivant les project il faudra changer les clefs souhaiter dans les conditions
    """
    if(entity_type == list(conf.globing_dictionary.keys())[0]
            or entity_type == list(conf.globing_dictionary.keys())[1] ):
        #create variable to store result of get_categorie function
        path_list = get_categorie(filter)
        entity_list =[]
        for path in path_list:
            #create my entity using parse  thanks to path obtain with get_categorie function
            entity = resolver.parse(path,resolver.categorie_templates)
            entity_list.append(entity)
            #return the list of all entity corresponding
        return entity_list


    elif (entity_type == list(conf.globing_dictionary.keys())[2]
          or entity_type == list(conf.globing_dictionary.keys())[3]):
        # create variable to store result of get_asset_name function
        path_list = get_asset_name(filter)
        entity_list = []
        for path in path_list:
            # create my entity using parse  thanks to path obtain with get_asset_name function
            entity = resolver.parse(path, resolver.name_templates)
            entity_list.append(entity)
            # return the list of all entity corresponding
        return entity_list

    elif (entity_type == list(conf.globing_dictionary.keys())[4]):
        # create variable to store result of get_job function
        path_list = get_job(filter)
        entity_list = []
        for path in path_list:
            # create my entity using parse  thanks to path obtain with get_job function
            entity = resolver.parse(path, resolver.job_templates)
            entity_list.append(entity)
            # return the list of all entity corresponding
        return entity_list

    elif(entity_type == list(conf.globing_dictionary.keys())[5]):
        # create variable to store result of get_files function
        path_list = get_files(filter, extension_list)
        entity_list = []
        for path in path_list:
            # create my entity using parse  thanks to path obtain with get_files function
            entity = resolver.parse(path, resolver.files_templates)
            entity_list.append(entity)
            # return the list of all entity corresponding
        return entity_list

    else:
        r=list(conf.globing_dictionary.keys())
        print('doesnt entity type')
        for name in r:
            print(name)
        print(" are expected")





if __name__ == '__main__':
    from pprint import pprint
    sg = connect_sg.get_sg()
    project_id = 1095
    filters = [["sg_status_list", "is", "wtg"]]
    filter = ['project', 'is', {'type': 'Project', 'id': project_id}]
    filters.append(filter)

    r=sg.find("Shot", filters=filters, fields=["code", "sg_status_list"])
    pprint(r)




    x ='Microfilms'
    y='assets'
    filter={'ok': 'Microfilms',
            'type':'assets',
            'categorie':'*',
            'asset_name':'*',
            'job':'rigging'}
    pprint(list(get_entities('file',filter)))




