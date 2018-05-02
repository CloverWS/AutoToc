import codecs
import sys

toc=[]


if __name__=="__main__":
    # 要处理的文件的路径
    path = sys.argv[1]
    descpath =  path[:path.rindex("."):] + ".withtoc."+path[path.rindex(".")+1::]
    
    flag=False
    file_object = codecs.open(path,"r","utf-8")
    lines = file_object.readlines()
    file_object.close()
    
    for line in lines:
        if(line.startswith("```")):
            flag = not flag

        if(flag):
            continue

        if line.startswith("#####"):
            line = line.replace("##### ","").replace(" ","").strip()
            toc.append("\t"*4+"* ["+line+"](#"+line+")")
        elif(line.startswith("####")):
            line = line.replace("#### ","").replace(" ","").strip()
            toc.append("\t"*3+"* ["+line+"](#"+line+")")
        elif(line.startswith("###")):
            line = line.replace("### ","").replace(" ","").strip()
            toc.append("\t"*2+"* ["+line+"](#"+line+")")
        elif(line.startswith("##")):
            line = line.replace("## ","").replace(" ","").strip()
            toc.append("\t"*1+"* ["+line+"](#"+line+")")
        elif(line.startswith("#")):
            line = line.replace("# ","").replace(" ","").strip()
            toc.append("\t"*0+"* ["+line+"](#"+line+")")
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
