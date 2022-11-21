import os
from manager.conf.conf_files import templates_dictionary
import lucidity

files_templates = [lucidity.Template('asset_file',templates_dictionary.get('asset_file')),
            lucidity.Template('shot_file',templates_dictionary.get('shot_file'))]

asset_name_templates =[ lucidity.Template('asset_name', templates_dictionary.get('asset_name')),
               lucidity.Template('shot_name',templates_dictionary.get('shot_name'))]

categorie_templates = [lucidity.Template('categorie', templates_dictionary.get('categorie')),
                    lucidity.Template('sequence',templates_dictionary.get('sequence'))]

job_templates = [lucidity.Template('job',templates_dictionary.get('job'))]

def parse(path, template_type):

    """
    :param template_type:
    :param path: Type String  using lucidity parsing for parse all of our string path
    :return:  dictionary that represent our entity
    """

    try:
        #must replace \ to /
        path = str(path).replace(os.sep,'/')

        data = lucidity.parse(path,template_type)
        return data[0]
    except lucidity.error.ParseError as e:
        print(e)

def format(entity, template_type):
    """
    :param template_type:
    :param entity: dictionnay that represent our entity
    :return: string corresponding to our path deducting thanks to our entity
    """
    try:
        data = lucidity.format(entity,files_templates)
        return data[0]
    except lucidity.error.FormatError as e:
        print(e)


if __name__ == '__main__':
    from pprint import pprint

    m_path = 'D:/Elouan/Microfilms/assets/car/porshe911/modeling/v004/work/porshe911.ma'
    x= parse(m_path,files_templates)
    pprint(x)

