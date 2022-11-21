import lucidity
# i can automatize this conf

project_root = "D:/Elouan"

#we store projects in a dictionary
#first element(the key) is the project_name
#second element(Value) is the the name of the project in the file_system

project_list = {'micromovie': 'Microfilms'}


translate_to_sg = {'assets': 'Asset',
             'shots': 'Shot'}

#name_entity_type = ['project', 'type', 'categorie', 'sequence', 'asset_name', 'shots', 'job', 'file']

#this dictionary keys is use in function get_entities

globing_dictionary={'categorie': project_root+'/{project}/{type}/{categorie}',
                    'sequence': project_root+'/{project}/{type}/{categorie}',
                    'asset_name': project_root+'/{project}/{type}/{categorie}/{asset_name}',
                    'shots': project_root+'/{project}/{type}/{categorie}/{shots}',
                    'job': project_root+'/{project}/{type}/{categorie}/{asset_name}/{job}',
                    'file': project_root+'/{project}/{type}/{categorie}/{asset_name}/{job}/**/*.{ext}'}


# warning this dictionay was sort alphabeticaly sorted with keys
templates_dictionary={'asset_file': project_root+'/{project}/{type}/{categorie}/{asset_name}/{job}/{version}/{status}/{asset_name}.{extension}',
                      'shot_file': project_root+'/{project}/{type}/{sequence}/{shot}/{job}/{shot}.{extension}',
                      'job': project_root+'/{project}/{type}/{categorie}/{asset_name}/{job}',
                      'asset_name':project_root+'/{project}/{type}/{categorie}/{asset_name}',
                      'shot_name': project_root+'/{project}/{type}/{sequence}/{shot}',
                      'categorie':project_root+'/{project}/{type}/{categorie}',
                      'sequence': project_root+'/{project}/{type}/{sequence}'}

# this dictionary determine if we use filesyteme or database to get element

request_type_dictionary={'categorie': 'shotgun',
                          'sequence': 'shotgun',
                          'asset_name': 'database',
                          'shots': 'database',
                          'job':'database',
                          'file':'filesystem'}


# this is the shotgrid part
project_id={project_list.get('micromovie'): 1095}

