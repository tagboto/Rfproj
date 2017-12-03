import templateMatching as t
import numpy as np
import cv2
import csv
from os import listdir
from os.path import isfile, join

class writeToFile:
  
    def __init__(self,path,height,width,file):
        if not path.endswith('/'):
            path = path + "/"
        self.path = path
        self.file = file
        self.height = height
        self.width = width
        self.type = type
        self.onlyfiles = [f for f in listdir(self.path) if isfile(join(self.path, f))]


    def prepareImage(self,pathx):
        path          = self.path + pathx
        img           = cv2.imread(path,600)
        img           = cv2.resize(img,(self.width,self.height), interpolation = cv2.INTER_CUBIC)
        img = np.reshape(img,(1,3,self.width,self.height))
        return (img)

    def myLabel(self,file):
        dash          = file.rfind("_")
        dot           = file.rfind(".")
        classtype     = file[dash+1:dot]

        if classtype == '1':
            return 'A'

        elif classtype =='2':
            return 'B'

        elif classtype =='3':
            return 'C'

        elif classtype == '4':
            return 'D'

        elif classtype =='5':
            return 'E'

        elif classtype =='6':
            return 'F'

        elif classtype == '7':
            return 'G'

        elif classtype == '8':
            return 'H'

        elif classtype =='9':
            return 'I'

        else:
            return 'not found'

    def buildFile(self):
        counter = 0
        chk = []
        comma = ","
        self.labels  = np.empty([len(self.onlyfiles)],dtype="int32")
        for file in self.onlyfiles:
            q = self.prepareImage(file)
            #(label)
            if (counter != 0):
                hull = t.recognize(file)
                label = self.myLabel(file)
                z = csv.writer(self.file,delimiter='\t')
                z.writerow([file,hull])
                print("done",file,label)#,"hull is",hull)
            else:
                self.global_matrix = q
    
            counter = counter + 1

    
