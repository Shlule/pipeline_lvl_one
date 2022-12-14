from pathlib import Path

import Qt
from Qt.QtWidgets import QMainWindow
from Qt import QtWidgets, QtCompat,QtCore
from pprint import pprint
from manager.core import validator

from manager import conf,engine
import manager.core.fs as fs
import manager.core.requester as requester


ui_path = Path(__file__).parent / "qt" / "window_v02.ui"
file_extension = Path(ui_path).suffix



UserRole = QtCore.Qt.UserRole






class Window(QMainWindow):

    def __init__(self):
        #global variable
        self.my_engine = engine.get()
        self.ui_list_dict = dict()

        self.previous_checkbox_state = []
        self.checkbox_state = []

        super(Window, self).__init__()
        print('init window')
        QtCompat.loadUi(str(ui_path), self)
        self.update_l_button()
        self.init_comboboxes()
        self.connect()
        self.le_demo.setText("how are you ?")
        self.setWindowTitle(conf.global_name)
        self.init_principal_list()
        self.cb_types.currentIndexChanged.connect(self.comboBox_changed)





    def clearlayout(self, layout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().deleteLater()



    def list_selection_changed(self):
        """
        create new list and apply in name and data of the item selected
        :return:
        """


        # get selected item from the sender object
        selected_item = (self.sender().selectedItems())
        for item in  selected_item:
            item_name = item.text()
            item_data = item.data(UserRole)
        #testing entity_type of the current item
        if(validator.determine_entity_type(item_data)== 'categorie'):
            #tranform item_data into a filter
            item_data['asset_name'] = '*'

            #request data corresponding to new filter
            entities_found = requester.get_entities('asset_name',item_data)

            #in case of non existing list this will go to else
            if 'lv_asset_name' in self.ui_list_dict:
                #i clear the list to recomplete it with new data
                self.ui_list_dict.get('lv_asset_name').clear()
                for entity in entities_found:
                    name = entity.get('asset_name')
                    # I create item

                    item = QtWidgets.QListWidgetItem()

                    # set text to item
                    item.setText(name)

                    # set item data with entity
                    item.setData(UserRole, entity)

                    self.ui_list_dict.get('lv_asset_name').addItem(item)

            else:
                # i create a list
                temp = QtWidgets.QListWidget()

                #store this list in a dictionary
                self.ui_list_dict['lv_asset_name'] = temp

                # connect the new list slection to this same function
                temp.itemSelectionChanged.connect(self.list_selection_changed)

                #display the list
                self.l_listwidgets.addWidget(self.ui_list_dict.get('lv_asset_name'))

                #put entity in the list
                for entity in entities_found:
                    name = entity.get('asset_name')
                    # I create item

                    item = QtWidgets.QListWidgetItem()

                    # set text to item
                    item.setText(name)

                    # set item data with entity
                    item.setData(UserRole, entity)

                    self.ui_list_dict.get('lv_asset_name').addItem(item)



        elif(validator.determine_entity_type(item_data)=='sequence'):
            #transform item_data into a filter
            item_data['shots'] = '*'

            # request data corresponding to new filter
            entities_found = requester.get_entities('shots', item_data)

            if 'lv_shots' in self.ui_list_dict:
                # i clear the list to recomplete it with new data
                self.ui_list_dict.get('lv_shots').clear()
                for entity in entities_found:
                    name = entity.get('shots')
                    # I create item

                    item = QtWidgets.QListWidgetItem()

                    # set text to item
                    item.setText(name)

                    # set item data with entity
                    item.setData(UserRole, entity)

                    self.ui_list_dict.get('lv_shots').addItem(item)

            else:
                # i create a list that contain data requested
                temp = QtWidgets.QListWidget()

                # store this list in a dictionary
                self.ui_list_dict['lv_shots'] = temp

                # connect the new list slection to this same function
                temp.itemSelectionChanged.connect(self.list_selection_changed)

                # display the list
                self.l_listwidgets.addWidget(self.ui_list_dict.get('lv_shots'))

                # put entity in the list
                for entity in entities_found:
                    name = entity.get('shots')
                    # I create item

                    item = QtWidgets.QListWidgetItem()

                    # set text to item
                    item.setText(name)

                    # set item data with entity
                    item.setData(UserRole, entity)

                    self.ui_list_dict.get('lv_shots').addItem(item)



        elif(validator.determine_entity_type(item_data) == 'asset_name' or validator.determine_entity_type(item_data)=='shots'):
            #transform item_data into a filter
            item_data['job'] = '*'

            # request data corresponding to new filter
            entities_found = requester.get_entities('job', item_data)

            if 'lv_job' in self.ui_list_dict:
                #i clear the list to recomplete it with new data
                self.ui_list_dict.get('lv_job').clear()
                for entity in entities_found:
                    name = entity.get('job')
                    # I create item

                    item = QtWidgets.QListWidgetItem()

                    # set text to item
                    item.setText(name)

                    # set item data with entity
                    item.setData(UserRole, entity)

                    self.ui_list_dict.get('lv_job').addItem(item)

            else:
                # i create a list that contain data requested
                temp = QtWidgets.QListWidget()

                #store this list in a dictionary
                self.ui_list_dict['lv_job'] = temp

                # connect the new list slection to this same function
                temp.itemSelectionChanged.connect(self.list_selection_changed)

                #display the list
                self.l_listwidgets.addWidget(self.ui_list_dict.get('lv_job'))

                #put entity in the list
                for entity in entities_found:
                    name = entity.get('job')
                    # I create item

                    item = QtWidgets.QListWidgetItem()

                    # set text to item
                    item.setText(name)

                    # set item data with entity
                    item.setData(UserRole, entity)

                    self.ui_list_dict.get('lv_job').addItem(item)

        elif ( validator.determine_entity_type(item_data) == 'job'):

            choosen_extension = self.get_extension()
            if not (choosen_extension):
                choosen_extension.append('*')
            # request data corresponding to new filter
            entities_found = requester.get_entities('file', item_data, choosen_extension)

            if 'lv_file' in self.ui_list_dict:
                # i clear the list to recomplete it with new data
                self.ui_list_dict.get('lv_file').clear()
                for entity in entities_found:
                    #on format le nom des file
                    x = entity.get('asset_name')
                    y = entity.get('extension')
                    z = entity.get('version')
                    name = f'{z}/{x}.{y}'
                    # I create item

                    item = QtWidgets.QListWidgetItem()

                    # set text to item
                    item.setText(name)

                    # set item data with entity
                    item.setData(UserRole, entity)

                    self.ui_list_dict.get('lv_file').addItem(item)

            else:
                # i create a list that contain data requested
                temp = QtWidgets.QListWidget()

                # store this list in a dictionary
                self.ui_list_dict['lv_file'] = temp

                # connect the new list slection to this same function
                temp.itemSelectionChanged.connect(self.list_selection_changed)

                # display the list
                self.l_listwidgets.addWidget(self.ui_list_dict.get('lv_file'))

                # put entity in the list
                for entity in entities_found:
                    x = entity.get('asset_name')
                    y = entity.get('extension')
                    z = entity.get('version')
                    name = f'{z}/{x}.{y}'
                    # I create item

                    item = QtWidgets.QListWidgetItem()

                    # set text to item
                    item.setText(name)

                    # set item data with entity
                    item.setData(UserRole, entity)

                    self.ui_list_dict.get('lv_file').addItem(item)



    def print_item(self):
        print(self.lv_scene.currentItem().text())


    def update_l_button(self):
        """
        set dynamicly buttons in l-button between the env that we are
        :return:
        """
        #create number of buttun corresponding to my_engine.implements,they have the same name
        #in my_engine.implements
        for button in self.my_engine.implements:
            temp = QtWidgets.QPushButton(button)
            temp.setObjectName("pb_"+button)
            temp.clicked.connect(self.do_it)
            self.l_button.addWidget(temp)

    def comboBox_changed(self):

        self.clearlayout(self.l_listwidgets)
        self.ui_list_dict = {}
        self.init_principal_list()

    def init_comboboxes(self):
        """
        this function is not dynamic  if we had an other project we must add it in
        conf.conf_files
        :return:
        """
        self.cb_projects.addItems(conf.project_list.keys())
        self.cb_types.addItems(conf.translate_to_sg)

    def init_principal_list(self):
        # filter is a dictionary which must contain as keys, name in bracket in globing_dictionanry in conf_files
        #{categorie}/{job} look globing_dictionnary in conf_files
        # i create a list that contain data requested
        temp = QtWidgets.QListWidget()

        if(self.cb_types.currentText() == 'assets'):
            filter={'project': conf.project_list.get(self.cb_projects.currentText()),
                    'type': self.cb_types.currentText(),
                    'categorie': '*'}

            list_entity_found = list(requester.get_entities('categorie',filter))

            for entity in list_entity_found:

                name = entity.get('categorie')
                #I create item
                item = QtWidgets.QListWidgetItem()
                #set text to item
                item.setText(name)
                #set item data with entity
                item.setData(UserRole, entity)

                temp.addItem(item)

            # store this list in a dictionary
            self.ui_list_dict['lv_categorie'] = temp

            # connect the new list slection to this same function
            temp.itemSelectionChanged.connect(self.list_selection_changed)

            # display the list
            self.l_listwidgets.addWidget(self.ui_list_dict.get('lv_categorie'))

        elif(self.cb_types.currentText() == 'shots'):

            filter = {'project': conf.project_list.get(self.cb_projects.currentText()),
                      'type': self.cb_types.currentText(),
                      'sequence': '*'}

            list_entity_found = list(requester.get_entities('sequence', filter))
            for entity in list_entity_found:

                name = entity.get('sequence')
                #I create item
                item = QtWidgets.QListWidgetItem()
                #set text to item
                item.setText(name)
                #set item data with entity
                item.setData(UserRole, entity)

                temp.addItem(item)

            # store this list in a dictionary
            self.ui_list_dict['lv_sequence'] = temp

            # connect the new list slection to this same function
            temp.itemSelectionChanged.connect(self.list_selection_changed)

            # display the list
            self.l_listwidgets.addWidget(self.ui_list_dict.get('lv_sequence'))


    def get_extension(self):
        """
        create a list of my extension to refresh my list with correspondant extension checked
        :return: list of choosen estension
        """
        #je regarde les etat demander par le client
        my_list=[]
        if(self.cb_ma.isChecked()):
            my_list.append("ma")
        if(self.cb_mb.isChecked()):
            my_list.append("mb")
        if(self.cb_houdini.isChecked()):
            my_list.append("hipnc")
        return my_list


    def connect(self):
        #I must conect all the button of my window to an function
        self.cb_ma.stateChanged.connect(self.get_extension)
        self.cb_mb.stateChanged.connect(self.get_extension)
        self.cb_houdini.stateChanged.connect(self.get_extension)


    def do_it(self):
        """
        this is a fake factory to permit get only one method for push button
        and this method reorient to the good method in case of he button push
        :return:
        """
        #je stocke dans une variable l'item selectioné et recupere la data presente dans l'item
        data = self.ui_list_dict.get('lv_file').currentItem().data(UserRole)
        #je get l'attribut et l'execute regarde la doc de getattr le deuxieme attribut est le nome correspondant
        #a la function dans l'engine
        getattr(self.my_engine,self.sender().text())(data)





def open_window():
    w = Window()
    w.show()

def open_app():
    app = QtWidgets.QApplication().instance()
    open_window()
    app.exec_()

if __name__ == '__main__':


    app = QtWidgets.QApplication()
    open_window()
    app.exec_()

    filter = {'project': 'Microfilms',
              'type': 'assets',
              'categorie':'Prop',
              'asset_name': '*'}




