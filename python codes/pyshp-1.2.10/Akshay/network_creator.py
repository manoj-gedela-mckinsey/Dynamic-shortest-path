import os
import csv
import shapefile
links = {}
latLng = []
nodes = {}
#directory = os.path.join("../../","Applicatons/XAMPP/xamppfiles/htdocs/DDP/shapefiles")
#print directory
w = shapefile.Writer(shapefile.POLYLINE)
w.autoBalance = 1


# nodes initialized

with open('network_1/Nodes.csv', 'rb') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
  spamreader.next()
  for row in spamreader:
    node_id = row[0]
    lat = row[1]
    lng = row[2]
    nodes[node_id]=[lat,lng]


# clubing all csv files,filtering repetetitions and creating shape files

for root,dirs,files in os.walk('shapefiles'):
 print files
 for file in files:
  if file.endswith(".csv"):
    f=open('shapefiles/'+file, 'r')
    spamreader = csv.reader(f, delimiter=',', quotechar='|')
    for row in spamreader:
      link  = row[0]
      tail = row[1]
      head = row[2]
      length = int(float(row[3]))
      point1 = nodes[tail]
      point2 = nodes[head]
      if link not in links.keys():
        latLng.append([float(point1[0]),float(point1[1])])
        with open('network_1/Geometry/'+link+'.csv', 'rb') as csvfile:
          spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
          spamreader.next()
          for row in spamreader:
            lat = float(row[0])
            lng = float(row[1])
            latLng.append([lat,lng])
        latLng.append([float(point2[0]),float(point2[1])])
        w.poly(shapeType=3, parts = [latLng])
        latLng = []
        links[link] = [tail,head,length]
    f.close()

# saving shapefiles
w.save('shapefiles/network/network')


print "created shape files"
print len(links)
with open('links.csv', 'w') as csvfile:
  spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|')
  spamwriter.writerow(['link_id','tail','head','length'])
  for key in links.iterkeys():
    spamwriter.writerow([key,links[key][0],links[key][1],links[key][2]])

