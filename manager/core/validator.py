def validate_filter(filter):
    """
    this function verifie the if the filter have correct key and value according the key 'type'
    :param filter: must be a dictionnary
    :return: bool true if is validate
    """

    type = filter.get('type')
    if (type == None):
        raise Exception("your filter haven't key 'type' ")
    elif(type == 'assets'):
        mandatory_keys=['categorie','asset_name']
        for key in mandatory_keys:
            if key not in filter:
                print("your filter is not valid")
                return False
        return True


    elif (type == 'shots'):
        mandatory_keys = ['sequence', 'shots']
        for key in mandatory_keys:
            if key not in filter:
                print("your filter is not valid")
                return False
        return True


def determine_entity_type(entity):
    """

    :param entity: an entity is a dictionnary
    :return: string corresponding to the entity_type
    """
    if(entity.get('extension') != None):
        return('file')
    elif(entity.get('job')!= None):
        return('job')
    elif (entity.get('shots') != None):
        return ('shots')
    elif (entity.get('asset_name') != None):
        return ('asset_name')
    elif (entity.get('sequence') != None):
        return ('sequence')
    elif (entity.get('categorie') != None):
        return ('categorie')
    else:
        print('your entity is not valid')