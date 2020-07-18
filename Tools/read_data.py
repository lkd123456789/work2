import yaml


class ReadData():
    def read_data(self,filename):
        filepath="D:\\Program Files\\JetBrains\\pycharmProjects\\work2\\Data\\"+filename+".yaml"
        with open(filepath,"r",encoding="utf-8")as f:
            data=yaml.load(f,Loader=yaml.FullLoader)
            return data
