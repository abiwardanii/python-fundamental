#contoh import module dari folder lain dan sub folder
from mainFolder import mainFunc
from mainFolder.subFolder import subFunc

mainFunc.main_report() # output dari mainFolder
subFunc.sub_report() # output dari mainFolder/subFolder
