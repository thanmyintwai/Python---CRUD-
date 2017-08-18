import csv
class csvHandling(object):
    def updating(self,lis):
        updatingList = lis
        with open("items.csv","w")as file_writer_obj:
                writer = csv.writer(file_writer_obj,lineterminator='\n')
                writer.writerows(updatingList)
        file_writer_obj.close()
    def listing(self):
        with open("items.csv") as f_obj_read:
            reader_List = csv.reader(f_obj_read)
            reader_List = list(reader_List)
        f_obj_read.close()
        return reader_List

    def hring(self):
        with open('items.csv') as f_obj_hiring:
            reader_hire_list = csv.reader(f_obj_hiring)
            reader_hire_list = list(reader_hire_list)
        f_obj_hiring.close()
        temps = []
        for i in range(len(reader_hire_list)):
            if reader_hire_list[i][3] == 'y':
                temps.append(reader_hire_list[i])
        return temps

    def returning(self):
        with open('items.csv') as f_obj_returning:
            reader_return_list = csv.reader(f_obj_returning)
            reader_return_list = list(reader_return_list)
        f_obj_returning.close()
        temps = []
        for i in range(len(reader_return_list)):
            if reader_return_list[i][3] == 'n':
                temps.append(reader_return_list[i])
        return temps

    def priceof(self):
        value = csvHandling.listing(self)
        ans = []
        for i in range(len(value)):
            ans.append(int(value[i][2]))
        return ans

