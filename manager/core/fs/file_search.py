from pathlib import Path
import glob
import os

import manager.conf as conf
from manager.core import resolver


def get_categorie(filter):
    """
    this function get the correct path directly in conf module

    :param filter Type dictionnary: contain all precedent entity we must get
    :return: list of path
    """
    path_pattern = conf.conf_files.globing_dictionary.get("categorie")
    path = path_pattern.format(project=filter.get('project'), type=filter.get('type'))
    result = glob.glob(path)
    return result

def get_asset_name(filter):
    """
    this function get the correct path directly in conf module

    :param filter Type dictionnary: contain all precedent entity we must get
    :return: list of path
    """
    path_pattern = conf.conf_files.globing_dictionary.get("asset_name")
    path = path_pattern.format(project=filter.get('project'), type=filter.get('type'),categorie=filter.get('categorie'))
    result = glob.glob(path)
    return result

def get_job(filter):
    """
    this function get the correct path directly in conf module

    :param filter Type dictionnary: contain all precedent entity we must get
    :return: list of path
    """
    path_pattern = conf.conf_files.globing_dictionary.get("job")
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
    path_pattern = conf.conf_files.globing_dictionary.get("file")
    generator_list =[]
    for ext in extension_list:
        path = path_pattern.format(project=filter.get('project'),
                                   type=filter.get('type'),
                                   categorie=filter.get('categorie'),
                                   asset_name=filter.get('asset_name'),
                                   job=filter.get('job'),
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
    """
    if(entity_type == 'categorie' or entity_type == 'sequence'):
        #create variable to store result of get_categorie function
        path_list = get_categorie(filter)
        entity_list =[]
        for path in path_list:
            #create my entity using parse  thanks to path obtain with get_categorie function
            entity = resolver.parse(path,resolver.categorie_templates)
            entity_list.append(entity)
            #return the list of all entity corresponding
        return entity_list


    elif (entity_type == 'asset_name' or entity_type == 'shot'):
        # create variable to store result of get_asset_name function
        path_list = get_asset_name(filter)
        entity_list = []
        for path in path_list:
            # create my entity using parse  thanks to path obtain with get_asset_name function
            entity = resolver.parse(path, resolver.name_templates)
            entity_list.append(entity)
            # return the list of all entity corresponding
        return entity_list

    elif (entity_type == 'job'):
        # create variable to store result of get_job function
        path_list = get_job(filter)
        entity_list = []
        for path in path_list:
            # create my entity using parse  thanks to path obtain with get_job function
            entity = resolver.parse(path, resolver.job_templates)
            entity_list.append(entity)
            # return the list of all entity corresponding
        return entity_list

    elif(entity_type == 'files'):
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
        print('doesnt entity type')





if __name__ == '__main__':
    from pprint import pprint
    x ='Microfilms'
    y='assets'
    filter={'project': 'Microfilms',
            'type':'assets',
            'categorie':'*',
            'asset_name':'*',
            'job':'rigging'}
    print(list(get_entities('categorie',filter,["ma"])))




