from os import listdir,remove
from json import load
from re import match

def depurarArchivosDeCarpeta(nombreCarpeta = ''):
    files = listdir(nombreCarpeta) #['file.json','file2.json']
    limpiarCarpeta('./cleanFiles')
    for nameFile in files:
        dataFile = open(nombreCarpeta+'/'+nameFile)#./files/file.json
        fileJSON = load(dataFile)
        sequences = fileJSON['seqs']
        data = {"nameFile":nameFile,"sequences":sequences}
        escribirArchivos([data])

def limpiarCarpeta(nombreCarpeta = ''):
    files = listdir(nombreCarpeta) #['file.json','file2.json']
    for nameFile in files:
            remove(nombreCarpeta+'/'+nameFile);

def escribirArchivos(arrayChunks = [[]]):
    for arrayFileSecuences in arrayChunks:
        firstSequence = arrayFileSecuences['sequences'][0]["seq"]
        resultHeaders = concatenationHeader(firstSequence)
        headers = ','.join(resultHeaders) #c1,c2,c3,c4...,cN
        dataCSV = "id,name,start,end,"+headers+"\n"
        fileCSV = open("cleanFiles/" + arrayFileSecuences['nameFile'] + ".csv", "a")
        fileCSV.write(dataCSV)
        for i in range(len(arrayFileSecuences['sequences'])):
            sequenceObject = arrayFileSecuences['sequences'][i]
            sequenceString = sequenceObject['seq']
            if match('[CTAG\-]',sequenceString):
                dataCSV = str(sequenceObject["id"]) +"," +sequenceObject["name"] + "," + str(sequenceObject["start"]) +"," +str(sequenceObject["end"]) +"," +",".join(sequenceObject["seq"]) +"\n";
                fileCSV.write(dataCSV)

def concatenationHeader(slicesSeq = []):
    headers = []
    for index in range(len(slicesSeq)):
        headers.append("c_"+str(index+1))

    return headers;

