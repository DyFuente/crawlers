import json
import csv
import time

json_file = open('net_channels_info.json').read()
json_data = json.loads(json_file)



def saveDataframeToCSVonS3(rows):
    ts = time.gmtime()
    filename = "output.csv"
    with open(filename,"w",newline="") as f:  # python 2: open("output.csv","wb")
        title = 'id_canal,st_titulo,dh_inicio,dh_fim,id_programa,titulo'.split(',') 
        cw = csv.DictWriter(f,fieldnames = title)
        cw.writeheader()
        for i in range(len(rows)):
            for x in rows[i]:
                cw.writerow(x)

    #s3_resource = boto3.resource('s3')
    #s3_object = s3_resource.Object('amazonia-input', 'Cliente/clientes_{}.csv'.format(time.strftime("%Y%m%d%H%M%S", ts)))
    #s3_object.put(Body=open('/tmp/output.csv', 'rb'))

saveDataframeToCSVonS3(json_data)