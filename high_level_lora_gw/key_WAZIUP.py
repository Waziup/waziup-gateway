####################################################
#server: CAUTION must exist
waziup_server="http://broker.waziup.io/v2"

#project name
project_name="waziup"

#your organization: CHANGE HERE
#choose one of the following: "DEF", "UPPA", "EGM", "IT21", "CREATENET", "CTIC", "UI", "ISPACE", "UGB", "WOELAB", "FARMERLINE", "C4A", "PUBD"
#organization_name="UPPA"
organization_name="UPPA"

#service tree: CHANGE HERE at your convenience
#should start with /
#use public prefix to indicate that data is public
#service_tree='/LIUPPA/T2I/CPHAM'
service_tree=''

#sensor name: CHANGE HERE but maybe better to leave it as Sensor
#the final name will contain the sensor address
sensor_name=organization_name+"Sensor"

#service path: DO NOT CHANGE HERE
service_path='/'+organization_name+service_tree

#SUMMARY
#the entity name will then be sensor_name+scr_addr, e.g. "UPPASensor1"
#the Fiware-ServicePath will be service_path which is based on both organization_name and service_tree, e.g. "/UPPA/LIUPPA/T2I/CPHAM"
#the Fiware-Service will be project_name, e.g. "waziup"

source_list=[]

####################################################