from statistics import *
import openpyxl

class DataHandler:
    evaluator = Stat()
    
    @classmethod
    def data_from_excel(cls, filename): #2
        dic = {}
        wb = openpyxl.load_workbook(filename)
        ws = wb.active
        g = ws.rows

        for name, score in g:
            dic[name.value] = score.value

        return dic
    
    def __init__(self, filename, year_class):
        self.rawdata = DataHandler.get_data_from_excel(filename)
        self.year_class = year_class
        # 연산한 값을 저장해 두는 저장소
        # 필요할 때 연산하되 이미 연산된 값이면 연산 없이 저장된 값을 반환
        self.cache = {}
    
    def get_scores(self):
        if 'scores' not in self.cache:
            self.cache['scores'] = list(self.rawdata.values())

        return self.cache.get('scores')
    
    def get_average(self): #4
        if 'average' not in self.cache: #5
            self.cache['average'] = self.evaluator.average(self.get_scores())

        return self.cache.get('average') #6
    
    def get_variance(self):
        if 'variance' not in self.cache:
            self.cache['variance'] = self.evaluator.variance(
                self.get_scores(), self.get_average())
            
        return self.cache.get('variance')
    
    def get_standard_deviation(self):
        if 'standard_deviation' not in self.cache:
            self.cache['standard_deviation'] = self.evaluator.std_dev(
                self.get_variance())
            
        return self.cache.get('standard_deviation')
