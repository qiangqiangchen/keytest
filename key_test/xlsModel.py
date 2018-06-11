# -*- coding: UTF-8 -*-
import xlrd
import xlwt
'''
    构建一个生成器，调用一次返回一行
'''
class readXls(object):
    def __init__(self,fileName,sheetName):
        self.fileName=fileName
        self.sheetName=sheetName
    def readDate(self):
        workbook=xlrd.open_workbook(self.fileName)
        sheet=workbook.sheet_by_name(self.sheetName)
        case_step=''
        for i in range(1,sheet.nrows):
            for j in range(sheet.ncols):
                case_step=case_step+sheet.cell_value(i,j).encode('utf-8')+','
            yield case_step
            case_step=''
            

class readCase(object):
    def __init__(self,fileName,sheetName):
        self.fileName=fileName
        self.sheetName=sheetName
    def readDate(self):
        workbook=xlrd.open_workbook(self.fileName)
        sheet=workbook.sheet_by_name(self.sheetName)
        
        case_name=sheet.cell_value(1,0)
        case=[]
        for i in range(1,sheet.nrows):
            case_step=''
            if sheet.cell_value(i,0)==case_name:
                for j in range(1,sheet.ncols):
                    case_step=case_step+sheet.cell_value(i,j).encode('utf-8')+','
                case.append(case_step)
            else:
                if 'finis' in case_name:
                    yield {"case_name":case_name,"case_step":case}
                else:
                    yield {"case_name":case_name,"case_step":case}
                    case=[]
                    case_name=sheet.cell_value(i,0)
                    #print case_name
                    case_step=''
                    for j in range(1,sheet.ncols):
                        case_step=case_step+sheet.cell_value(i,j).encode('utf-8')+','
                    case.append(case_step)
        
if __name__=="__main__":
    readXls=readCase(r'F:\testcase.xlsx','Sheet2')
    step=readXls.readDate()

    for i in step:
        print i
    