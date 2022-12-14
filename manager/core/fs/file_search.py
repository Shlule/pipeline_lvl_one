import glob
import sys

import manager.conf as conf
from manager.core import resolver


def get_categorie(filter):
    """
    this function get the correct path directly in conf module

    :param filter Type dictionnary: contain all precedent entity we must get
    :return: generator of entities
    """
    path_pattern = conf.conf_files.globing_dictionary.get('categorie')
    path = path_pattern.format(**filter)
    # path = path_pattern.format(project=filter.get('project'), type=filter.get('type'))
    path_list = glob.glob(path)
    entity_list = []
    for path in path_list:
        # create my entity using parse  thanks to path obtain with get_categorie function
        entity = resolver.parse(path, resolver.categorie_templates)
        # verify if entity doesn't None
        if (entity):
            entity_list.append(entity)
        # return the list of all entity corresponding
    yield entity_list


def get_asset_name(filter):
    """
    this function get the correct path directly in conf module

    :param filter Type dictionnary: contain all precedent entity we must get
    :return: generator of entities
    """
    path_pattern = conf.conf_files.globing_dictionary.get('asset_name')
    path = path_pattern.format(**filter)
    print(path)
    # path = path_pattern.format(project=filter.get('project'), type=filter.get('type'),categorie=filter.get('categorie'))
    path_list = glob.glob(path)
    entity_list = []
    for path in path_list:
        # create my entity using parse  thanks to path obtain with get_categorie function
        entity = resolver.parse(path, resolver.asset_name_templates)
        # verify if entity doesn't None
        if (entity):
            entity_list.append(entity)
        # return the list of all entity corresponding
    yield entity_list


def get_job(filter):
    """
    this function get the correct path directly in conf module

    :param filter Type dictionnary: contain all precedent entity we must get
    :return: generator of entities
    """

    path_pattern = conf.globing_dictionary.get('job')
    path = path_pattern.format(**filter)
    # path = path_pattern.format(project=filter.get('project'),type=filter.get('type'),categorie=filter.get('categorie'),asset_name=filter.get('asset_name'))
    path_list = glob.glob(path)
    entity_list = []
    for path in path_list:
        # create my entity using parse  thanks to path obtain with get_categorie function
        entity = resolver.parse(path, resolver.job_templates)
        #verify if entity doesn't None
        if(entity):
            entity_list.append(entity)
        # return the list of all entity corresponding
    yield entity_list


def get_files(filter, extension_list=["*"]):
    """
    this function get the correct path directly in conf module

    :param project: put the project name
    :param type: Type string; est le type de données demander souvent assets ou shaots
    :return: generator of entities
    """
    path_pattern = conf.conf_files.globing_dictionary.get('file')
    generator_list = []
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


def request_filesystem(entity_type, filter, extension_list=["*"], ):
    """
    :param filter: type Dictionary
    :param project: is the project_name
    :param type: Type string; est le type de données demander souvent assets ou shots
    :param entity_type: is the name in resolver template {categorie} etc.
    :return: generator of entity

    Warning: suivant les project il faudra changer les clefs souhaiter dans les conditions
    """
    if (entity_type == ('categorie' or 'sequence')):
        return get_categorie(filter)

    elif (entity_type == ('asset_name' or 'shots')):
        return get_asset_name(filter)

    elif (entity_type == 'job'):
        return get_job(filter)

    elif (entity_type == 'file'):
        # create variable to store result of get_files function
        path_list = get_files(filter, extension_list)
        entity_list = []
        for path in path_list:
            # create my entity using parse  thanks to path obtain with get_files function
            entity = resolver.parse(path, resolver.files_templates)
            #verify if entity doesn't None
            if(entity):
                entity_list.append(entity)
            # return the list of all entity corresponding
        return entity_list

    else:
        r = list(conf.globing_dictionary.keys())
        print('doesnt entity type')
        for name in r:
            print(name)
        print(" are expected")


if __name__ == '__main__':
    import sys

    from pprint import pprint
    from manager.test.test_data import test_dictionary

    filter = {'project': 'Microfilms',
              'type': 'assets',
              'categorie': 'prop',
              'asset_name': 'porshe911',
              'job': 'rigging'}

    pprint(request_filesystem('file',filter))

    sys.exit()
    # create a filter verification pn my class

    for item, filtres in test_dictionary.items():
        for filtre in filtres:
            try:
                print(f'testing {item}')
                pprint(filtre)
                pprint(request_filesystem(item, filtre))
                print('*' * 50)
            except Exception as e:
                print(f"that doesn't work {e}")

    # pprint(get_entities('categorie',filter))
