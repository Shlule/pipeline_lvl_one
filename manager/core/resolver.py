import os

import lucidity

templates = [lucidity.Template('asset','D:/Elouan/{project}/{type}/{categorie}/{asset_name}/{job}/{version}/{status}/{asset_name}.{extension}'),
             lucidity.Template('shots','D:/Elouan/{project}/{type}/{sequence}/{shot}/{job}/{shot}.{extension}')]



def parse(path):

    """

    :param path: Type String  using lucidity parsing for parse all of our string path
    :return:  dictionary that represent our entity
    """

    try:
        #must replace \ to /
        path = str(path).replace(os.sep,'/')

        data = lucidity.parse(path, templates)
        return data[0]
    except lucidity.error.ParseError as e:
        print(e)

def format(entity):
    """

    :param entity: dictionnay that represent our entity
    :return: string corresponding to our path deducting thanks to our entity
    """
    try:
        data = lucidity.format(entity,templates)
        return data[0]
    except lucidity.error.FormatError as e:
        print(e)


if __name__ == '__main__':
    from pprint import pprint

    m_path = 'D:/Elouan/Microfilms/assets/car/porshe911/modeling/v004/work/porshe991.ma'
    #print (templates[0].keys())
    data = parse(m_path)
    #get one elemnt of entity
    pprint(data)
    new_data=format(data)
    print(new_data)
