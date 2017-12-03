import fileWriter as c

def importDataSet():
    try:
        file = open("copyPaste.csv", "a",newline='')
        f = c.writeToFile("C:/Users/Zoe Tagboto/Documents/Fall 2017/Robotics Class/Final Project/Tensor Flow Edition/Images/train",100,100,file)
        f.buildFile()
        file.close()
    except:
        pass

importDataSet()
    
