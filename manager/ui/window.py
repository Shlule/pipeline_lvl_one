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

        self.lv_scene.itemSelectionChanged.connect(self.selection_changed)





    def selection_changed(self):
        """

        :return: name of the selected item in lv_scene Qlistwidgets
        """
        # get selected item from the sender object
        selected_item_list = (self.sender().selectedItems())
        for item in  selected_item_list:
            item_name = item.text()
            item_data = item.data(UserRole)
        #testing entity_type of the current item
        if(validator.determine_entity_type(item_data)== 'categorie'):
            #tranform item_data into a filter
            item_data['asset_name'] = '*'

            #request data corresponding to new filter
            entities_found = requester.get_entities('asset_name',item_data)

            pprint(entities_found)
            #in case of non existing list this will be an error and go to except
            try:
                #i celar the list to re complete it with new data
                self.lv_categorie.clear()
                print('hello')
                for entity in entities_found:
                    pass

            except:
                # i create a list that contain data requested
                temp = QtWidgets.QListWidget()
                temp.setObjectName('lv_categorie')
                print(temp)
                self.l_listwidgets.addWidget(temp)

                for entity in entities_found:
                    name = entity.get('asset_name')
                    # I create item

                    item = QtWidgets.QListWidgetItem()

                    # set text to item
                    item.setText(name)

                    # set item data with entity
                    item.setData(UserRole, entity)

                    self.lv_categorie.addItem(item)



        elif(validator.determine_entity_type(item_data)=='sequence'):
            #transform item_data into a filter
            item_data['shots'] = '*'

            # request data corresponding to new filter
            entities_found = requester.get_entities('shots', item_data)

            pprint(entities_found)

        elif(validator.determine_entity_type(item_data) == 'asset_name' or validator.determine_entity_type(item_data)=='shots'):
            #transform item_data into a filter
            item_data['job'] = '*'

            #request data corresponding to new filter
            entities_found = requester.get_entities('job',item_data)

            pprint(entities_found)






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


        filter={'project': conf.project_list.get(self.cb_projects.currentText()),
                'type': self.cb_types.currentText(),
                'categorie': '*'}


        #create a list of all entity corresponding to my critere
        #using get_entities function wich need (str,dictionay) argument
        list_entity_found = list(requester.get_entities('categorie',filter))
        for entity in list_entity_found:

            name = entity.get('categorie')
            #I create item
            item = QtWidgets.QListWidgetItem()
            #set text to item
            item.setText(name)
            #set item data with entity
            item.setData(UserRole, entity)
            self.lv_scene.addItem(item)



    def choose_extension(self):
        """
        create a list of my extension to refresh my list with correspondant extension checked
        :return:
        """
        #je regarde les etat demander par le client
        my_list=[]
        if(self.cb_ma.isChecked()):
            my_list.append("ma")
        if(self.cb_mb.isChecked()):
            my_list.append("mb")
        if(self.cb_houdini.isChecked()):
            my_list.append("hipnc")
        #je compare mes etat actuelle et les precedant

        #si la list precedant est > a la liste actuelle j'appelle refresh
        #sinon je deduis ce qui a etait rajouter et je l'ajoute







    def connect(self):
        #I must conect all the button of my window to an function
        self.cb_ma.stateChanged.connect(self.choose_extension)
        self.cb_mb.stateChanged.connect(self.choose_extension)
        self.cb_houdini.stateChanged.connect(self.choose_extension)


    def do_it(self):
        """
        this is a fake factory to permit get only one method for push button
        and this method reorient to the good method in case of he button push
        :return:
        """
        #je stocke dans une variable l'item selectioné et recupere la data presente dans l'item
        x = self.lv_scene.currentItem().data(UserRole)
        #je get l'attribut et l'execute regarde la doc de getattr le deuxieme attribut est le nome correspondant
        #a la function dans l'engine
        getattr(self.my_engine,self.sender().text())(x)





def open_window():
    w = Window()
    w.show()



if __name__ == '__main__':


    app = QtWidgets.QApplication()
    open_window()
    app.exec_()

    filter = {'project': 'Microfilms',
              'type': 'assets',
              'categorie':'Prop',
              'asset_name': '*'}




