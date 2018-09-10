import csv
import shapefile
from xlrd import open_workbook
from xlrd import empty_cell


# initialize route for which shape file has to be generated
route = "19B cut"
routes_busId = []
nodes = {}
busIds_link = {}
rb = open_workbook('input/bus_fleet.xlsx')
r_busId = rb.sheet_by_index(0)

len_rows = r_busId.nrows
w = shapefile.Writer(shapefile.POLYLINE)
w.autoBalance = 1


print "identifying bus ids related to route"

# reading bus ids from bus_fleet table related to the route
for i in range(1,len_rows):
	bus_id = r_busId.cell(i,1).value
	try:
		route_id = int(r_busId.cell(i,2).value)
	except:
		route_id = r_busId.cell(i,2).value
	if str(route_id) == route:
		routes_busId.append(float(bus_id))


#print routes_busId
print "identified bus ids"

print "finding links related to the busids"

# reading data from map matched link file
with open('input/2014-03-01_linkTime_t.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	spamreader.next()
	for row in spamreader:
		#print row
		#break
		bus_id = row[0] 
		if float(bus_id) in routes_busId:
			#print bus_id
			tail = row[1]
			head = row[2]
			link_id = row[3]
			length = row[6]
			if link_id not in busIds_link.keys():
				busIds_link[link_id] = [tail,head,length]
print "links are identified"
#print busIds_link
# initialize nodes file
with open('network_1/Nodes.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	spamreader.next()
	for row in spamreader:
		node_id = row[0]
		lat = row[1]
		lng = row[2]
		nodes[node_id]=[lat,lng]


# it will read links and get geometry for links and create shape for route
latLng = []
for key in busIds_link.iterkeys():
	point1 = nodes[busIds_link[key][0]]
	point2 = nodes[busIds_link[key][1]]
	latLng.append([float(point1[0]),float(point1[1])])
	with open('network_1/Geometry/'+key+'.csv', 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		spamreader.next()
		for row in spamreader:
			lat = float(row[0])
			lng = float(row[1])
			latLng.append([lat,lng])
	latLng.append([float(point2[0]),float(point2[1])])
	w.poly(shapeType=3, parts = [latLng])
	latLng = []
	#links_latLng[key] = latLng

# storing shapes into shapefiles folder
w.save('shapefiles/'+route+'/'+route)
print "created shape files"


# creating route csv file 
print "storing links array into a csv file"
# storing data to shape file of the route
with open('shapefiles/'+route+'_shape.csv', 'w') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|')
	for key in busIds_link.iterkeys():
		spamwriter.writerow([key,busIds_link[key][0],busIds_link[key][1],busIds_link[key][2]])
print "complete"
#    for row in spamreader: