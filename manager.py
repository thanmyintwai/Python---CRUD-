#Developer Name: Than Myint Wai-13119134
#Date          : 16th to 30th May 2016
#Description   : In this program, there are 4 main features. These are as follow:
#                   - Let the user to retrieve the data(item information-ID,Name,Description,Price,AvailableToHire)
#                   - Let the user to hire the items these are available
#                   - Let the user to return the items these were hired
#                   - Let the user to add new items
#               : All of these information or data about items are stored in a csv file

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from csvHandling import csvHandling
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import csv

'''
class MainScreen(Screen):
    pass

class AddingScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass
'''
presentation = Builder.load_file("screen.kv")

class Manager(App):


    def build(self):
        self.whohaveclicked = []
        return presentation


    ######################################################
    def clear(self):
        temp = []
        self.whohaveclicked = temp [:]
    '''
    def whichscreen(self,f):
        whattodo = f
        if self.where == 'm':
            self.root.current = 'main'
        if whattodo == 'l':
            self.itmlist()
    '''
    def messageClear(self):
        self.root.ids.msg.text = ''

    def listDetail(self,args):
        ids = str(args.id)


        id = ids.strip('l')
        id = int(id)
        print (id)
        res = csvHandling.listing(self)
        hired = []
        nothired = []
        for i in range(len(res)):
            if res[i][3]=='n':
                nothired.append(i)
            else:
                hired.append(i)
        if id in hired:
            self.root.ids.msg.text = format('%s  is  available  to  hire  with  $%s'%(str(res[id][1]),str(res[id][2])))
        else:
            self.root.ids.msg.text = format('%s  is  currently not available  to  hire. Price is $%s'%(str(res[id][1]),str(res[id][2])))
        temp = []
        hired = temp[:]
        nothired = temp[:]

    def itmlist(self):



        self.messageClear()

        print(csvHandling.listing(self))
        #self.root.ids.msg.text='Listing'
        result = csvHandling.listing(self)
        hired = []
        for i in range(len(result)):
            if result[i][3]=='n':
                hired.append(i)

        no = len(result)
        self.root.ids.message.clear_widgets()
        self.clear()
        for i in range(no):
            if i in hired:
                #background_color=(0,0,255,0.1)
                self.root.ids.message.add_widget(Button(background_normal='./hired1.png',text= str(result[i][1]),id=(result[i][0]+'l'),on_press=self.listDetail))
            else:
                self.root.ids.message.add_widget(Button(text= str(result[i][1]),id=(result[i][0]+'l'),on_press=self.listDetail))

        for i in range(no):
            id = result[i][0]+'l'
            print(id)
    def hiring(self,*args):

        if args:
            self.root.ids.btn_confirm.disabled=False

        for arg in args:
            #print (arg.id)
            id = arg.id
            state = arg.state
            temp = (id,state)
            place = []
            self.whohaveclicked.append(temp)
            for i in range(len(self.whohaveclicked)):
                wid = self.whohaveclicked[i][0]
                wstate = self.whohaveclicked[i][1]
                if wid == id and wstate != state:
                    self.whohaveclicked[i] = temp
                else:
                    self.whohaveclicked.append(temp)
        tem = self.whohaveclicked
        no = []
        selectedItem = []

        tem.reverse()
        if len(tem)>0:
            for i in range(len(tem)):
                no.append(tem[i][0])
            no = list(set(no))
            for j in range(len(no)):
                for k in range(len(tem)):
                    if tem[k][1] == 'down' and tem[k][0] == no[j]:
                        selectedItem.append(no[j])
        selectedItem = list(set(selectedItem))
        print(selectedItem)
        price = 0
        priceLists = csvHandling.priceof(self)
        if len(selectedItem) > 0:
            for i in range(len(selectedItem)):
                val = selectedItem[i].strip('h')
                val = int(val)
                price = price + priceLists[val]
        str(price)
        self.root.ids.msg.text= format('Sub total of hiring price for selected items are $%s'%price)
    def itmhire(self):
        self.messageClear()
        result = csvHandling.hring(self)
        no = len(result)
        self.root.ids.message.clear_widgets()
        self.clear()
        for i in range(no):
            button = ToggleButton(text= str(result[i][1]),id=str('h'+result[i][0]),on_press=self.hiring)
            self.root.ids.message.add_widget(button)
    def returning(self,*args):

        if args:
            self.root.ids.btn_confirm.disabled=False

        for arg in args:
            #print (arg.id)
            id = arg.id
            state = arg.state
            temp = (id,state)
            place = []
            self.whohaveclicked.append(temp)
            for i in range(len(self.whohaveclicked)):
                wid = self.whohaveclicked[i][0]
                wstate = self.whohaveclicked[i][1]
                if wid == id and wstate != state:
                    self.whohaveclicked[i] = temp
                else:
                    self.whohaveclicked.append(temp)
    def itmreturn(self):
        self.messageClear()
        result = csvHandling.returning(self)
        no = len(result)
        self.root.ids.message.clear_widgets()
        self.clear()
        for i in range(no):
            button = ToggleButton(text= str(result[i][1]),id=('r'+result[i][0]),on_press=self.returning)
            self.root.ids.message.add_widget(button)

    '''
    def addChecking(self):
        valname = self.input1
        valdescription = self.input2
        valprice = self.input3

        if not valname or valname == '':
            print("Please Type in name")
    '''

    def itmConfirm(self):
        self.messageClear()
        #self.root.ids.msg.text='Confirm'

        val = len(self.whohaveclicked)
        if val > 0:

            temp = list(set(self.whohaveclicked))

        #####I made some change in here for adding (if statement)

            print("Other Functions")
            self.messageClear()
            #self.callingClear()

            result = []
            for i in range(len(self.whohaveclicked)):
                stateis = str(self.whohaveclicked[i][1])
                if stateis == 'down':

                    result.append(str(self.whohaveclicked[i][0]))
            result =list(set(result))

            if len(result) > 0:
                if result [0][0] == 'h':
                    print ("It is for hire")
                    print(result)

                    for i in range(len(result)):
                        result[i] = int(result[i][1])
                    temp = csvHandling.listing(temp)
                    print("Original :",temp)
                    for k in range(len(result)):
                        temp[result[k]][3]= 'n'

                    print("Update one :",temp)
                    csvHandling.updating(csvHandling,temp)
                    self.itmhire()
                    self.root.ids.btn_confirm.disabled=True

                else:
                    print("It is for return")
                    print(result)

                    for j in range(len(result)):
                        result[j] = int(result[j][1])
                    temp = csvHandling.listing(temp)
                    print("Original :",temp)
                    for m in range(len(result)):
                        temp[result[m]][3]= 'y'

                    print("Update one :",temp)
                    csvHandling.updating(csvHandling,temp)
                    self.itmreturn()
                    self.root.ids.btn_confirm.disabled=True


            self.itmlist()
        else:
            #print("adding function")

            self.msg = []
            self.temp = ''
            if not self.input1._get_text():

                self.msg.append('Name')
            if not self.input2._get_text():
                self.msg.append('Description')
            if not self.input3._get_text():
                self.msg.append("Price")
            else:
                try :
                    self.price = float(self.input3._get_text())
                except ValueError:
                    self.msg.append("Price(Only Number)")
                if self.price <= 0:
                    self.msg.append("Price(Greater than Zero)")

            if len(self.msg) <= 0:
                print('OK')
            else:
                if len(self.msg) == 1:
                    self.temp = self.msg[0]
                elif len(self.msg) == 2:
                    self.temp = self.msg[0] + ' & ' + self.msg[1]
                else:
                    self.temp = self.msg[0] + ', ' + self.msg[1] + ' & ' + self.msg[2]
            print(self.temp)
            if len(self.temp)>0:


                self.root.ids.msg.text = 'Please insert '+ self.temp

            else:
                self.root.ids.msg.text = "Item is saved into the system"
                #self.temp = ''

                data = [0,self.input1._get_text()+':'+self.input2._get_text(),self.input3._get_text(),'y']
                position = 0
                with open('items.csv') as file_object:
                    reader = csv.reader(file_object)
                    your_list = list(reader)
                    toAddPosition = len(your_list)
                    data[0] = toAddPosition
                position = toAddPosition
                your_list.append(data)
                data = your_list
                file_object.close()
                with open("items.csv","w")as file_writer_obj:
                    writer = csv.writer(file_writer_obj,lineterminator='\n')
                    writer.writerows(data)
                file_writer_obj.close()

                
                print(data)
                self.itmlist()
                self.messageClear()
                self.callingClear()
            '''
            else:
                if len(self.msg) == 1:
                    if self.msg[0] == 'Price':
                        try:
                            price = float(self.input3._get_text())
                        except ValueError:
                            self.temp = self.msg[0]+'(Only Digit)'
                        else:
                            self.temp = self.msg[0]

                elif len(self.msg) == 2:
                    for i in range(len(self.msg)):
                        if self.msg[i] == 'Price':
                            try:
                                price = float(self.input3._get_text())
                            except ValueError:
                                self.temp = self.msg[i] + '(Only Digit)'
                            else:
                                self.temp = self.msg[i]
                            self.temp = self.msg[0] + ' & ' + self.msg[1]
                        else:
                            self.temp = self.temp + self.msg[i]
                    #self.temp = self.msg[0] + ' & ' + self.msg[1]
                else:
                    self.temp = self.msg[0] + ', ' + self.msg[1] + ' & ' + self.msg[2]
                #self.root.ids.msg.text = format('%s  is  currently not available  to  hire. Price is $%s'%(str(res[id][1]),str(res[id][2])))
                self.root.ids.msg.text = 'Please insert '+ self.temp
                print(self.temp)

            '''



            '''
            while self.ok==False:
                if not self.input1.text:
                    self.input1.focus=True
                    #self.root.ids.msg.text = "Plese Inset Item Name"
                    print("Pls Name")
                    self.ok = False
                    continue
                    #self.messageClear()
                elif not self.input2._get_text():

                    self.ok = False
                    #self.root.ids.msg.text = "Plese Inset Item Description"
                    print("Pls Des")
                elif not self.input3._get_text():

                    print("Pls Pri")
                    self.ok = False
                    self.root.ids.msg.text = "Plese Inset Item Price"
                else:
                    self.ok = True
            '''


    def callingClear(self,*args):
        #self.root.ids.iname.text = ''
        print("It is calling")
        self.input1.text = ''
        self.input2.text = ''
        self.input3.text = ''
        #value = self.root.ids.iname.text
        #print(value)

    def enable(self):
        print("It is calling")
        self.root.ids.btn_confirm.disabled=True

    def itmadd(self):
        print("Hello")
        self.root.ids.btn_confirm.disabled=False
        '''
        self.root.ids.results.clear_widgets()
        label = Label(text='Enter Description')
        textinput = TextInput(id='text1')
        button = Button(text='ADD', on_press=self.add_item)
        self.root.ids.results.add_widget(label)
        self.root.ids.results.add_widget(textinput)
        self.root.ids.results.add_widget(button)
        added_item = [label, textinput, button]
        '''
        self.root.ids.message.clear_widgets()
        label1 = Label(text = "Add Item")
        self.root.ids.message.add_widget(label1)
        label2 = Label(text = "Item Name")
        self.root.ids.message.add_widget(label2)
        self.input1 = TextInput(hint_text = 'Type In Item Name',id = 'iname')
        #input1 = TextInput(id = 'iname')
        self.root.ids.message.add_widget(self.input1)
        label3 = Label(text="Description")
        self.root.ids.message.add_widget(label3)
        self.input2 = TextInput(hint_text = 'Type In Item Description',id = 'idescription')
        #input2 = TextInput(id = 'idescription')
        self.root.ids.message.add_widget(self.input2)
        label4 = Label(text="Price")
        self.root.ids.message.add_widget(label4)
        self.input3 = TextInput(hint_text = 'Type In Item Price',id = 'iprice')
        #input3 = TextInput(id = 'iprice')
        self.root.ids.message.add_widget(self.input3)
        bun1 = Button(text = "Cancel",id = 'icancel',on_press=self.callingClear)
        self.root.ids.message.add_widget(bun1)







Manager().run()
