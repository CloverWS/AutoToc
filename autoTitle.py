import codecs
import sys

toc=[]


if __name__=="__main__":
    # 原文件的路径
    path = sys.argv[1]
    # 目的文件的路径
    descpath =  path[:path.rindex("."):] + ".withtoc."+path[path.rindex(".")+1::]
    
    # 是否在代码区域中
    flag=False
    file_object = codecs.open(path,"r","utf-8")
    lines = file_object.readlines()
    file_object.close()
    
    level1 = 0
    level2 = 0
    level3 = 0
    level4 = 0
    level5 = 0
    
    for i in range(len(lines)):
        line = lines[i]
        if(line.startswith("```")):
            flag = not flag
        
        if(flag):
            continue

        if line.startswith("#####"):
            level5 = level5 + 1
            title = str(level1) + "." + str(level2) + "." + str(level3) + "."  + str(level4) + "." +str(level5)
            lines[i] = line.replace("#####","##### "+title+" ")
        elif(line.startswith("####")):
            level4 = level4 + 1
            level5 = 0
            title = str(level1) + "." + str(level2) + "." + str(level3) + "."  + str(level4)
            lines[i] = line.replace("####","#### "+title+" ")
        elif(line.startswith("###")):
            level3 = level3 + 1
            level4 = 0
            level5 = 0
            title = str(level1) + "." + str(level2) + "." + str(level3)
            lines[i] = line.replace("###","### "+title+" ")
        elif(line.startswith("##")):
            level2 = level2 + 1
            level3 = 0
            level4 = 0
            level5 = 0
            title = str(level1) + "." + str(level2)
            lines[i] = line.replace("##","## "+title+" ")
        elif(line.startswith("#")):
            level1 = level1 + 1
            level2 = 0
            level3 = 0
            level4 = 0
            level5 = 0
            title = str(level1)
            lines[i] = line.replace("#","# "+title+" ")
        else:
            pass

        
    file_object = codecs.open(descpath,"w","utf-8")
    for line in toc:
        file_object.write("\n")
        
        file_object.write(line)
        
        file_object.write("\n")
        
    for line in lines:
        file_object.write(line)
        
    file_object.close