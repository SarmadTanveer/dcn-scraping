import requests
import lxml
import bs4
import json

def getAllCertificates(url,maxPage):

    data = []
    for x in range(maxPage):
        result = requests.get(url.replace('{PAGENUMBER}',str(x + 1)))
        soup = bs4.BeautifulSoup(result.text, 'lxml')
        certificates = soup.find_all('h3', class_='cards-title')
        for x in range(len(certificates)):
            data.append(
                ['https://canada.constructconnect.com/' + certificates[x].a['href'], certificates[x].a['title']])
    return data


def getMaxPage(url):

    result = requests.get(url.replace('{PAGENUMBER}', '1'))
    soup = bs4.BeautifulSoup(result.text, 'lxml')

    pages = soup.find_all(class_='page-numbers')
    numPages = []
    for element in pages:
        numPages.append(int(element.text))

    lastPage = max(numPages)
    print('Number of results: ' + str(lastPage))
    return lastPage


def parseCertificate(url):
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    # get all data associated with datalist
    allData = soup.find_all(class_='datalist')
    data = []
    # deconstruct all html tags
    for element in allData:
        data.append(element.contents)
    # remove whitespace
    for element in data:
        for tag in element:
            if (isinstance(tag, bs4.element.NavigableString)):
                element.remove(tag)
    # get string content of data
    info = []
    for element in data:
        for tag in element:
            info.append(tag.get_text().strip())
    # remove all whitespace
    for element in info:
        if (element == ''):
            info.remove(element)
    # add publication date
    pubDate = soup.find('h3', string='Publication date').next_sibling.next_sibling.get_text().strip()
    info.append('Publicaton Date')
    info.append(pubDate)
    # if certificate is of type 2(without pdfs)
    if (len(info) <= 18):
        # find and add publication date

        # find and add location and address
        location = soup.find('h4', class_='print-title')
        address = location.next_sibling.next_sibling
        location = location.get_text()
        address = address.get_text()
        info.append('Address')
        info.append(address)
        info.append('Location')
        info.append(location)
        # find and add project
        project = soup.find('h3', string='Certificate').next_sibling.next_sibling.p.get_text()
        info.append('Project')
        info.append(project)
    else:
        info.insert(0, 'Location')
        info.insert(2, 'Address')
    info.append('Certificate Number')
    info.append(url.split('/')[-1])
    # return data as an array
    return formatData(info)

def formatData(data):
    hashTable = [('owner','Name of Owner'),('contractor','Contractor'),('contract', 'Project'), ('substantially','Substantially Performed'),('Address of Certifier','Address of Consultant'),('Certifier', 'Consultant'),('certifier','Consultant'),('premises','Premises')]
    for word in hashTable:
        for entry in data:
            if (word[0] in entry):
                index = data.index(entry)
                data[index] = word[1]
    for x in range(len(data)):
        if (('Address' in data[x]) and ('Consultant' in data[x - 2])):
            data[x] = 'Consultant Address'
        if (('Address' in data[x]) and ('Owner' in data[x - 2])):
            data[x] = 'Address of Owner'
    infoDict = {}
    for x in range(len(data)):
        if (x % 2 == 0):
            key = data[x]
            value = data[x + 1]
            infoDict.update({key: value})
    return infoDict

