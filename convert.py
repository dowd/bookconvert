import os
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#file = open("output.md","w")
directory='../books/'
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        with open(os.path.join(directory, filename)) as json_file:
            data = json.load(json_file)

            file=open((directory+filename+".md"),"w")

            file.write("## "+data['title']+"\n\nAuthor: "+data['authors']+"\n\n")

            for h in data['highlights']:
                file.write ("> "+h['text']+" (["+str(h['location']['value'])+"]("+h['location']['url']+")) \n\n")


        continue
    else:
        continue
#file.close()
