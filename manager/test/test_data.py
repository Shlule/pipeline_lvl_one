
filter1 = {'project': 'Microfilms',
              'type': 'shots',
              'sequence': '*',
              'shots': 'sq010_sh010',
              'job': '*'}

filter2 = {'project': 'Microfilms',
          'type': 'assets',
          'sequence': '*',
          'shots': 'porshe911',
          'job': '*'}

filter3={'project': 'Microfilms',
          'type': 'assets',
          'categorie': 'vehicle',
          'asset_name': 'porshe911',
          'job': 'modeling'}

filter4 = {'project': 'Microfilms',
           'type': 'assets',
           'categorie': 'vehicle',
           'asset_name': '*',
           'job': 'modeling'}

filter5 = {'project': 'Microfilms',
           'type': 'assets',
           'categorie': '*',
           'asset_name': 'porshe911',
           'job': 'modeling'}

#pprint(request_shotgun('job',filter3))

test_dictionary = {'job':[filter1, filter2, filter3, filter4, filter5],
                   'asset_name': [filter1, filter2, filter3, filter4, filter5],
                   'shots': [filter1, filter2, filter3, filter4, filter5],
                   'categorie': [filter1, filter2, filter3, filter4, filter5]
                    }