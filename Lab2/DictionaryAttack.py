import csv, re

def LetterFreq(cypherTextIn):
    letterFreq = {}
    letters = ["Z","Y","X","W","V","U","T","S","R","Q","P","O","N","M","L","K","J","I","H","G","F","E","D","C","B","A"]
    output = []
    words = cypherTextIn.split(" ")
    for word in words:
        for letter in word:
            if letter not in letterFreq.keys():
                letterFreq[letter] = letters.pop()
    stageOutput = []
    for word in words:
        for letter in word:
            stageOutput.append(letterFreq[letter])
        output.append(''.join(stageOutput))
        stageOutput = []
    return output

def CsvCompare(filePath, letterFreq):
    dictOfFreq = {}
    outputArrayStage = []
    with open(filePath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # line_count = 0
        for row in csv_reader:
            dictOfFreq[str(row[1])] = str(row[0])
    csv_file.close()
    for word in letterFreq:
        try:
            outputArrayStage.append(dictOfFreq[str(' '+word)])
        except:
            outputArrayStage.append('NOT_IN_DICT')
    return ' '.join(outputArrayStage)

inputCypherTextVar = "YVZ PDND FE IO INZFEZ. PD QDEFNDE ZH GIFOZ JHV ZPD QNDIMFDEZ, EPIQFDEZ, LVFDZDEZ, MHEZ DOAPIOZFOR YFZ HX NHMIOZFA SIOQEAIGD FO ISS ZPD CISSDJ HX ZPD EIAH. WPIZ FE ZPD APFDX DSDMDOZ PD DMGSHJE? ZPDND EZIOQ PFE ZNDDE, DIAP WFZP I PHSSHW ZNVOU, IE FX I PDNMFZ IOQ I ANVAFXFB WDND WFZPFO; IOQ PDND ESDDGE PFE MDIQHW, IOQ ZPDND ESDDG PFE AIZZSD; IOQ VG XNHM JHOQDN AHZZIRD RHDE I ESDDGJ EMHUD. QDDG FOZH QFEZIOZ WHHQSIOQE WFOQE I MIKJ WIJ, NDIAPFOR ZH HCDNSIGGFOR EGVNE HX MHVOZIFOE YIZPDQ FO ZPDFN PFSS-EFQD YSVD. YVZ ZPHVRP ZPD GFAZVND SFDE ZPVE ZNIOADQ, IOQ ZPHVRP ZPFE GFOD-ZNDD EPIUDE QHWO FZE EFRPE SFUD SDICDE VGHO ZPFE EPDGPDNQ'E PDIQ, JDZ ISS WDND CIFO, VOSDEE ZPD EPDGPDNQ'E DJD WDND XFBDQ VGHO ZPD MIRFA EZNDIM YDXHND PFM. RH CFEFZ ZPD GNIFNFDE FO TVOD, WPDO XHN EAHNDE HO EAHNDE HX MFSDE JHV WIQD UODD-QDDG IMHOR ZFRDN-SFSFDE—WPIZ FE ZPD HOD APINM WIOZFOR?—WIZDN—ZPDND FE OHZ I QNHG HX WIZDN ZPDND! WDND OFIRINI YVZ I AIZINIAZ HX EIOQ, WHVSQ JHV ZNICDS JHVN ZPHVEIOQ MFSDE ZH EDD FZ? WPJ QFQ ZPD GHHN GHDZ HX ZDOODEEDD, VGHO EVQQDOSJ NDADFCFOR ZWH PIOQXVSE HX EFSCDN, QDSFYDNIZD WPDZPDN ZH YVJ PFM I AHIZ, WPFAP PD EIQSJ ODDQDQ, HN FOCDEZ PFE MHODJ FO I GDQDEZNFIO ZNFG ZH NHAUIWIJ YDIAP? WPJ FE ISMHEZ DCDNJ NHYVEZ PDISZPJ YHJ WFZP I NHYVEZ PDISZPJ EHVS FO PFM, IZ EHMD ZFMD HN HZPDN ANIKJ ZH RH ZH EDI? WPJ VGHO JHVN XFNEZ CHJIRD IE I GIEEDORDN, QFQ JHV JHVNEDSX XDDS EVAP I MJEZFAIS CFYNIZFHO, WPDO XFNEZ ZHSQ ZPIZ JHV IOQ JHVN EPFG WDND OHW HVZ HX EFRPZ HX SIOQ? WPJ QFQ ZPD HSQ GDNEFIOE PHSQ ZPD EDI PHSJ? WPJ QFQ ZPD RNDDUE RFCD FZ I EDGINIZD QDFZJ, IOQ HWO YNHZPDN HX THCD? EVNDSJ ISS ZPFE FE OHZ WFZPHVZ MDIOFOR. IOQ EZFSS QDDGDN ZPD MDIOFOR HX ZPIZ EZHNJ HX OINAFEEVE, WPH YDAIVED PD AHVSQ OHZ RNIEG ZPD ZHNMDOZFOR, MFSQ FMIRD PD EIW FO ZPD XHVOZIFO, GSVORDQ FOZH FZ IOQ WIE QNHWODQ. YVZ ZPIZ EIMD FMIRD, WD HVNEDSCDE EDD FO ISS NFCDNE IOQ HADIOE. FZ FE ZPD FMIRD HX ZPD VORNIEGIYSD GPIOZHM HX SFXD; IOQ ZPFE FE ZPD UDJ ZH FZ ISS"
cleanCyperTextIn = re.sub("[^a-zA-Z ]", "", inputCypherTextVar)
cleanText = []
for word in cleanCyperTextIn.split(" "):
    cleanText.append(CsvCompare('/home/potatoesmkchips/github/2022-UoP-Secrypt/Lab2/english-dict.csv', LetterFreq(cleanCyperTextIn)))
print(' '.join(cleanText))
