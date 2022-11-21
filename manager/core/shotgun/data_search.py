
import manager.conf as conf
from manager.core.shotgun import connect_sg
from manager.core import validator

sg = connect_sg.get_sg()


def request_categorie(filter):

    # testing the value of the key 'type' in my filter is different to assets
    if (filter.get('type') != ('assets')):
        raise Exception("you request a categorie but in your filter the value of key 'type' isn't assets")

    project_id = conf.project_id.get(filter.get('project'))
    # initialise my list of filters and append my filter
    m_filters = []
    m_filter = ['project', 'is', {'type': 'Project', 'id': project_id}]
    m_filters.append(m_filter)

    #translate our key 'type' value in our file to shotgrid understand
    sg_type = conf.translate_to_sg.get(filter.get('type'))

    # make the request to shotgrid
    x = sg.find(sg_type, filters=m_filters, fields=['sg_asset_type'])

    # for all object in my response i only store sg_aaset_type in categorie
    categorie = []
    for item in x:
        categorie.append(item.get('sg_asset_type'))
    # casting categorie in set to only take one occurence of each type
    x = set(categorie)

    # create my entities
    entities_list = []
    for item in x:
        entity = {'project': filter.get('project'),
                  'type': filter.get('type'),
                  'categorie': item}
        entities_list.append(entity)

    return entities_list

def request_sequence(filter):

    """
    this function get the sequence thanks to the shot name in shot grid
    :param filter:
    :return:
    """

    #testing the value of the key 'type' in my filter is different to shots
    if(filter.get(list('type') != 'shots')):
        raise Exception ("you request a sequence but in your filter the value of key 'type' isn't shots")


    # search in dictionary project_id la valeur de la clef 'microfilms'
    project_id = conf.project_id.get(filter.get('project'))

    # initialise my list of filters and append my filter
    m_filters = []
    m_filter = ['project', 'is', {'type': 'Project', 'id': project_id}]
    m_filters.append(m_filter)

    # translate our key 'type' value in our file to shotgrid understand
    sg_type = conf.translate_to_sg.get(filter.get('type'))


    # make the request to shotgrid
    x = sg.find(sg_type, filters=m_filters, fields=['code'])

    #get only 'code' value
    sequence =[]
    for item in x:
        temp = item.get('code')
        split_temp=(temp.split('_'))
        sequence.append(split_temp[0])
    # casting sequence in set to only take one occurence of each type
    x=set(sequence)

    # create my entities
    entities_list = []
    for item in x:
        entity = {'project': filter.get('project'),
                  'type': filter.get('type'),
                  'sequence': item}
        entities_list.append(entity)

    return entities_list


def request_asset_name(filter):
    if(validator.validate_filter(filter)):
        # testing the value of the key 'type' in my filter is different to assets
        if (filter.get('type') != ('assets')):
            raise Exception("you request a asset_name but in your filter the value of key 'type' isn't assets")

        # search in dictionary project_id la valeur de la clef 'microfilms'
        project_id = conf.project_id.get(filter.get('project'))

        # initialise my list of filters and append my filter
        m_filters = []
        m_filter = ['project', 'is', {'type': 'Project', 'id': project_id}]
        m_filters.append(m_filter)

        # translate our key 'type' value in our file to shotgrid understand
        sg_type = conf.translate_to_sg.get(filter.get('type'))

        if(filter.get('categorie')=='*'):
            #request shotgun
            x = sg.find(sg_type, filters =m_filters, fields = ['code','sg_asset_type'])

        elif(filter.get('categorie')):
            #add a filter
            m_filter = ['sg_asset_type','is', filter.get('categorie')]
            m_filters.append(m_filter)

            #request shotgun
            x = sg.find(sg_type, filters= m_filters, fields = ['code','sg_asset_type'])


        data_list=[]
        for item in x:
            data = {'asset_name': item.get('code'),
                    'categorie': item.get('sg_asset_type')}
            data_list.append(data)


        entities_list=[]
        for item in data_list:
            entity ={'project': filter.get('project'),
                     'type': filter.get('type'),
                     'categorie': item.get('categorie'),
                     'asset_name': item.get('asset_name')}
            entities_list.append(entity)

        return entities_list

def request_shots(filter):

    if(validator.validate_filter(filter)):
        # testing the value of the key 'type' in my filter is different to assets
        if (filter.get('type') != ('shots')):
            raise Exception("you request a asset_name but in your filter the value of key 'type' isn't assets")

        # search in dictionary project_id la valeur de la clef 'microfilms'
        project_id = conf.project_id.get(filter.get('project'))

        # initialise my list of filters and append my filter
        m_filters = []
        m_filter = ['project', 'is', {'type': 'Project', 'id': project_id}]
        m_filters.append(m_filter)

        # translate our key 'type' value in our file to shotgrid understand
        sg_type = conf.translate_to_sg.get(filter.get('type'))

        if(filter.get('sequence')=='*'):
            #request shotgun
            x = sg.find(sg_type, filters =m_filters, fields = ['code'])

        elif(filter.get('sequence')):
            #add a filter
            m_filter = ['code','starts_with', filter.get('sequence')]
            m_filters.append(m_filter)

            #request shotgun
            x = sg.find(sg_type, filters= m_filters, fields = ['code'])

        data_list=[]
        for item in x:
            temp = item.get('code')
            split_temp = (temp.split('_'))
            data={'code': temp,
                  'sequence': split_temp[0] }
            data_list.append(data)

        entities_list=[]
        for item in data_list:
            entity ={'project': filter.get('project'),
                     'type': filter.get('type'),
                     'sequence': item.get('sequence'),
                     'shots': item.get('code')}
            entities_list.append(entity)

        return entities_list

def request_job(filter):


    if(validator.validate_filter(filter)):
        # search in dictionary project_id la valeur de la clef 'microfilms'
        project_id = conf.project_id.get(filter.get('project'))

        # initialise my list of filters and append my filter
        m_filters = []
        m_filter = ['project', 'is', {'type': 'Project', 'id': project_id}]
        m_filters.append(m_filter)

        # translate our key 'type' value in our file to shotgrid understand
        sg_type = conf.translate_to_sg.get(filter.get('type'))

        # two different behavior because assets filter and shots filter aren't the same
        if(sg_type == 'Asset'):
            if(filter.get('categorie')!= '*'):
                #filter if the demand categorie match with the categorie in shotgun
                m_filter = ['entity.'+sg_type+'.sg_asset_type', 'is', filter.get('categorie')]
                m_filters.append(m_filter)

            if(filter.get('asset_name') != '*'):
                #filter if the demand asset_name match with the asset_anme in shotgrid
                m_filter = ['entity.'+sg_type+'.code', 'is', filter.get('asset_name')]
                m_filters.append(m_filter)

            if(filter.get('job')!= '*'):
                #filter if the demand job match with the job in shotgrid
                m_filter = ['content', 'is', filter.get('job')]
                m_filters.append(m_filter)

        elif(sg_type == 'Shot'):
            if (filter.get('sequence') != '*'):
                # create a new filter depending of the categorie or sequence
                m_filter = ['entity.' + sg_type + '.sg_asset_type', 'is', filter.get('sequence')]
                m_filters.append(m_filter)

                # create a new filter depending of the asset_name or shots
            m_filter = ['entity.' + sg_type + '.code', 'is', filter.get('shots')]
            m_filters.append(m_filter)

        # make shotgun request
        x = sg.find('Task', filters = m_filters, fields = ['content','entity.'+sg_type+'.code','entity.'+sg_type+'.sg_asset_type'])

        data_list =[]
        for item in x:
            data ={'content': item.get('content'),
                   'asset_type': item.get('entity.'+sg_type+'.sg_asset_type'),
                   'asset_name': item.get('entity.'+sg_type+'.code')}
            data_list.append(data)


        if(sg_type == 'Asset'):
            entities_list = []
            for item in data_list:
                entity = {'project': filter.get('project'),
                          'type': filter.get('type'),
                          'categorie': item.get('asset_type') ,
                          'asset_name': item.get('asset_name'),
                          'job': item.get('content')}
                entities_list.append(entity)

            return entities_list
        elif(sg_type == 'Shot'):

            entities_list = []
            for item in data_list:
                temp = item.get('asset_name')
                split_temp = (temp.split('_'))
                entity = {'project': filter.get('project'),
                          'type': filter.get('type'),
                          'sequence': split_temp[0],
                          'shots': item.get('asset_name'),
                          'job': item.get('content')}
                entities_list.append(entity)

            return entities_list
    else:
        return []


def request_shotgun(entity_type,filter):
    """

    :param entity_type: type of entity request
    :param filter:
    :return: list of entity
    """

    # this is default request categorie
    if(entity_type == 'categorie'):
        return(request_categorie(filter))

    #this is default request_sequence
    elif(entity_type == 'sequence'):
        return(request_sequence(filter))

    # this is default 'asset_name
    elif(entity_type == 'asset_name'):
        return(request_asset_name(filter))

    elif(entity_type == 'shots'):
        return(request_shots(filter))

    elif(entity_type == 'job'):
        return(request_job(filter))


if __name__ == '__main__':
    import sys
    from pprint import pprint
    from manager.test.test_data import test_dictionary

    filter = {'project': 'Microfilms',
              'type': 'assets',
              'categorie': 'prop',
              'asset_name': '*'}

    print(request_shotgun('asset_name',filter))


    sys.exit()
    for item, filtres in test_dictionary.items():
        for filtre in filtres:
            try:
                print(f'testing {item}')
                pprint(filtre)
                pprint(request_shotgun(item, filtre))
                print('*'*50)
            except Exception as e:
                print(f"that doesn't work {e}")

