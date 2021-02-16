from collector import links
from collector import certParser
from collector import excel
from collector import jsonConv
import math

searchTerm = 'martinway'
fileName = 'martinway-cont'
sheetName = 'Martinway Contracting Ltd'

url = 'https://canada.constructconnect.com/dcn/certificates-and-notices?ccpage={PAGENUMBER}&phrase='+searchTerm


lastPage = links.getMaxPage(url)
certificates = links.getAllCertificates(url, lastPage)
jsonConv.writeList(fileName + '-links', {'length': len(certificates), 'data':certificates})

data = jsonConv.readList(fileName+'-links')
lenData = data['length']
data = data['data']
links=[]

for link in data:
    links.append(link[0])

sliceLen = 60

x = 0
y = 0
while(x<lenData):
    certificates=[]
    targetCertificates = links[x:x+sliceLen]
    for link in targetCertificates:
        certificates.append(certParser.parseCertificate(link))
        x+=1
    #change
    jsonConv.writeList(fileName+'-certificates-'+str(y), {'length': len(certificates), 'data': certificates})
    y+= 1


headings = ['Certificate Number','Address','Location','Project', 'Name of Owner', 'Address of Owner', 'Consultant', 'Substantially Performed', 'Publication Date']


excel.createSheet('certificates.xlsx', sheetName, headings)

numCertFiles = math.ceil(lenData/sliceLen)
for x in range(numCertFiles):
    #Change
    certificates = jsonConv.readList(fileName+'-certificates-'+str(x))['data']
    for certificate in certificates:
        print(certificate)
        writableCert = []
        for heading in headings:
            try:
                writableCert.append(certificate[heading])
            except KeyError as error:
                writableCert.append(" ")
        #Change
        excel.saveData('certificates.xlsx', sheetName, writableCert)

