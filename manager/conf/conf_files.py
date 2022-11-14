import lucidity

project_root = "D:/Elouan"

#we store projects in a dictionary
#first element(the key) is the project_name
#second element(Value) is the the name of the project in the file_system
project_list = {'micromovie': 'Microfilms'}

type_list = {'assets': 'assets',
             'shots': 'shots'}




#this dictionary keys define the Name of EntityType

globing_dictionary={'categorie': project_root+'/{ok}/{type}/*',
                    'sequence': project_root+'/{project}/{type}/*',
                    'asset_name': project_root+'/{project}/{type}/{categorie}/*',
                    'shots': project_root+'/{project}/{type}/{categorie}/*',
                    'job': project_root+'/{project}/{type}/{categorie}/{asset_name}/*',
                    'file': project_root+'/{ok}/{type}/{categorie}/{asset_name}/{job}/**/*.{ext}'}


# warning this dictionay was sort alphabeticaly sorted with keys
templates_dictionary={'asset_file': project_root+'/{project}/{type}/{categorie}/{asset_name}/{job}/{version}/{status}/{asset_name}.{extension}',
                      'shot_file': project_root+'/{project}/{type}/{sequence}/{shot}/{job}/{shot}.{extension}',
                      'job': project_root+'/{project}/{type}/{categorie}/{asset_name}/{job}',
                      'asset_name':project_root+'/{project}/{type}/{categorie}/{asset_name}',
                      'shot_name': project_root+'/{project}/{type}/{sequence}/{shot}',
                      'categorie':project_root+'/{project}/{type}/{categorie}',
                      'sequence': project_root+'/{project}/{type}/{sequence}'}

# this dictionary determine is we use filesyteme or database to get element


