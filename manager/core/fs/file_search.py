from pathlib import Path
import glob
import os

import manager.conf as conf
from manager.core import resolver


def get_categorie(project,type):
    """
    this function get the correct path directly in conf module

    :param project: put the project name
    :param type: Type string; est le type de données demander souvent assets ou shaots
    :return: list of path
    """
    path_pattern = conf.conf_files.globing_dictionary.get("categorie")
    path = path_pattern.format(project=project, type=type)
    result = glob.glob(path)
    return result

def get_asset_name(project,type):
    """
    this function get the correct path directly in conf module
    :param project: put the project name
    :param type: Type string; est le type de données demander souvent assets ou shaots
    :return:list of path
    """
    path_pattern = conf.conf_files.globing_dictionary.get("assetName")
    path = path_pattern.format(project=project, type=type)
    result = glob.glob(path)
    return result

def get_job(project,type):
    """
   this function get the correct path directly in conf module

    :param project: put the project name
    :param type: Type string; est le type de données demander souvent assets ou shaots
    :return: list of path
    """
    path_pattern = conf.conf_files.globing_dictionary.get("job")
    path = path_pattern.format(project=project, type=type)
    result = glob.glob(path)
    return result
def get_files(project,type, extension_list=["*"]):
    """
    this function get the correct path directly in conf module

    :param project: put the project name
    :param type: Type string; est le type de données demander souvent assets ou shaots
    :return: list of path
    """
    path_pattern = conf.conf_files.globing_dictionary.get("file")
    generator_list =[]
    for ext in extension_list:
        path = path_pattern.format(project=project, type=type, ext=ext)
        found = glob.glob(path, recursive=True)
        generator_list.append(found)
    for generator in generator_list:
        for item in generator:
            yield item


def get_entities(project, type, entity_type, extension_list=["*"]):
    """

    :param project: is the project_name
    :param type: Type string; est le type de données demander souvent assets ou shots
    :param entity_type: is the name in resolver template {categorie} etc.
    :return: list of entity
    """
    if(entity_type == 'categorie' or entity_type == 'sequence'):
        #create variable to store result of get_categorie function
        path_list = get_categorie(project,type)
        entity_list =[]
        for path in path_list:
            #create my entity using parse  thanks to path obtain with get_categorie function
            entity = resolver.parse(path,resolver.categorie_templates)
            entity_list.append(entity)
            #return the list of all entity corresponding
        return entity_list


    elif (entity_type == 'asset_name' or entity_type == 'shot'):
        # create variable to store result of get_asset_name function
        path_list = get_asset_name(project, type)
        entity_list = []
        for path in path_list:
            # create my entity using parse  thanks to path obtain with get_asset_name function
            entity = resolver.parse(path, resolver.name_templates)
            entity_list.append(entity)
            # return the list of all entity corresponding
        return entity_list

    elif (entity_type == 'job'):
        # create variable to store result of get_job function
        path_list = get_job(project, type)
        entity_list = []
        for path in path_list:
            # create my entity using parse  thanks to path obtain with get_job function
            entity = resolver.parse(path, resolver.job_templates)
            entity_list.append(entity)
            # return the list of all entity corresponding
        return entity_list

    elif(entity_type == 'files'):
        # create variable to store result of get_files function
        path_list = get_files(project, type, extension_list)
        entity_list = []
        for path in path_list:
            # create my entity using parse  thanks to path obtain with get_files function
            entity = resolver.parse(path, resolver.files_templates)
            entity_list.append(entity)
            # return the list of all entity corresponding
        return entity_list

    else:
        print('doesnt entity type')





if __name__ == '__main__':
    from pprint import pprint
    x ='Microfilms'
    y='assets'
    pprint(get_entities(x,y,'files'))



