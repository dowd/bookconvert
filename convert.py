import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

with open('highlights.json') as json_file:
    data = json.load(json_file)

file = open("output.md","w")
file.write("## "+data['title']+"\n\nAuthor: "+data['authors']+"\n\n")

for h in data['highlights']:
    file.write ("> "+h['text']+" (["+str(h['location']['value'])+"]("+h['location']['url']+")) \n\n")

file.close()
