import manager.conf as conf
from manager.core.fs import file_search as fs
from manager.core.shotgun import data_search as sg


def get_entities(entity_type,filter,extensionlist=['*']):

    """

    :param entity_type: must be a string
    :param filter: must be a dictionnary
    :param extensionlist:
    :return: list of entities
    """

    # testing if  the filter given is valid

    request_type = conf.request_type_dictionary.get(entity_type)
    if (request_type == 'filesystem'):
        return fs.request_filesystem(entity_type,filter, extensionlist)
    elif(request_type == 'shotgun'):
        return sg.request_shotgun(entity_type, filter,)
    else:
        print('the database demand is not valid ')