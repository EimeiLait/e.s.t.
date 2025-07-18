from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import CMYKColor as CMYKcolor
from barcode.writer import ImageWriter
from PIL import Image
from reportlab.graphics.barcode import code128
import barcode
import io





pdfmetrics.registerFont(TTFont("optimaHeavy", "./fonts/OptimaNovaLTProHeavy.ttf"))
pdfmetrics.registerFont(TTFont("optimaBlack", "./fonts/OptimaNovaLTProBlack.ttf"))
pdfmetrics.registerFont(TTFont("optimaMid", "./fonts/OptimaNovaLTProMedium.ttf"))
pdfmetrics.registerFont(TTFont("oCR_B", "./fonts/OCRB.ttf"))
pdfmetrics.registerFont(TTFont("oCR_A", "./fonts/OCRA.ttf"))




natureCheck = False #to conform if the nature inputed vaild
vrifcation = 0
serialNum = 0
red = CMYKcolor(0, 1, 1, 0)
black = CMYKcolor(0, 0, 0, 1)
serialSepChar1 = 0
serialSepChar2 = 0
serialSepChar3 = 0
serialSepChar4 = 0
serialSepChar5 = 0
serialSepChar6 = 0
serialSepChar7 = 0
serialSepChar8 = 0
numFinStr = ' '
numFinInt = 0
lit = 'R'
bitFill = 0
code128Bin = ''
text = ''
space = 0


def menuNature():
    print('R = Regestered letter')
    print('V = Insured letter')
    print('L = Printed matters')
    print('')
    print('')
    return None

def numSeparating():
    global serialNum
    serialNum = input('Enter the first serial number, No spaces, 8 digits:')
    for i, char in enumerate(serialNum) :
        globals()[f'serialSepChar{i+1}'] = int(char)

def calcVrifcation(digits):
    global vrifcation
    
    weights = [8, 6, 4, 2, 3, 5, 9, 7]
    b = sum(d * w for d, w in zip(digits, weights))
    b = 11 - (b % 11)

    if 1 <= b <= 9:
        vrifcation = b
        return b
    
    elif b == 10:
        vrifcation = 0
        return 0
    
    elif b == 11:
        vrifcation = 5
        return 5


def serialCumVrifcation(serialNum):
    serialStr = str(serialNum)
    digits = [int(ch) for ch in serialStr]
    v = calcVrifcation(digits)

    if v is not None:
        numFStr = serialStr + str(v)
        numFInt = int(numFStr)
        return numFStr, numFInt


def formattedFin(serialNum, vrifcation):
    serialStr = str(serialNum)
    part1 = serialStr[:4]
    part2 = serialStr[4:]
    result = f"{nature}{litSec} {part1} {part2} {vrifcation} RD"
    return result


def code128bin(text):
    rv = io.BytesIO()
    code128 = barcode.get('code128', text, writer=ImageWriter())
    code128.write(rv, options={
    'module_height': 10,
    'module_width': 1,
    'quiet_zone': 0,
    'write_text': False,
    })

    rv.seek(0)
    img = Image.open(rv).convert('1')

    pixels = img.load()
    width, height = img.size
    binary = ''
    for x in range(width):
        binary += '0' if pixels[x, 0] == 0 else '1'

    return binary


def digiSep(serialNum):
    global serialSepChar1, serialSepChar2, serialSepChar3, serialSepChar4
    global serialSepChar5, serialSepChar6, serialSepChar7, serialSepChar8
    serialSepChar1, serialSepChar2, serialSepChar3, serialSepChar4, serialSepChar5, serialSepChar6, serialSepChar7, serialSepChar8 = [int(d) for d in str(serialNum)]
    return None



print('Welcome to Bar code generator')
print('Developed by Ei.Laitus')
print('Aug. 2025')


while not natureCheck:
    red = CMYKcolor(0, 1, 1, 0)
    menuNature()
    nature = str(input('Enter the code to Select a nature:'))
    if nature in ['R','V','L']:
        natureCheck = True

        mapping = {
            "R": "REGISTERED",
            "V": "INSURED",
            "3": "c",
            "4": "d"
        }

        natureFullEng = mapping.get(nature)

        mapping = {
            "R": "REGISTRATA",
            "V": "VALORATA",
            "3": "c",
            "4": "d"
        }
        natureFullLat = mapping.get(nature)
        
    else:
        natureCheck = False
        print('Invaild. Please retry.')

# pdf
c = canvas.Canvas("output.pdf", pagesize=(842, 595)) # unit: pt

##################################################


c.setFont("optimaHeavy", 33)
if nature == 'R':
    c.setFillColor(red)
else:
    c.setFillColor(black)

x = 74
y = 555
for i in range(4):
    c.drawString(x, y, f"{nature}")
    y = y - 64
    c.drawString(x, y, f"{nature}")
    y = y - 34
    c.drawString(x, y, f"{nature}")
    y = y - 57.5

    c.drawString(x, y, f"{nature}")
    y = y - 64
    c.drawString(x, y, f"{nature}")
    y = y - 34
    c.drawString(x, y, f"{nature}")
    y = y - 32

    #

    c.drawString(x, y, f"{nature}")
    y = y - 64
    c.drawString(x, y, f"{nature}")
    y = y - 34
    c.drawString(x, y, f"{nature}")
    y = y - 57.5

    c.drawString(x, y, f"{nature}")
    y = y - 64
    c.drawString(x, y, f"{nature}")
    y = y - 34
    c.drawString(x, y, f"{nature}")
    
    x = x + 170
    y = 555
    

c.setFont("optimaHeavy", 20)
if nature == 'R':
    c.setFillColor(red)
else:
    c.setFillColor(black)



x = 72
y = 436

for i in range(4):
    
    c.drawString(x, y, f"{nature}")
    y = y - 283
    c.drawString(x, y, f"{nature}")

    y = 436
    x = x + 97

    c.drawString(x, y, f"{nature}")
    y = y - 283
    c.drawString(x, y, f"{nature}")

    y = 436
    x = x + 74
    


c.setFont("optimaBlack", 13)
c.setFillColor(black)

x = 100
y = 568

for i in range(4):
    
    c.drawString(x, y, f"{natureFullEng}")
    y = y - 155
    c.drawString(x, y, f"{natureFullEng}")
    y = y - 128

    c.drawString(x, y, f"{natureFullEng}")
    y = y - 155
    c.drawString(x, y, f"{natureFullEng}")

    y = 570
    x = x + 170



c.setFont("optimaMid", 12)
c.setFillColor(black)

x = 100
y = 555

for i in range(4):
    
    c.drawString(x, y, f"{natureFullLat}")
    y = y - 155
    c.drawString(x, y, f"{natureFullLat}")
    y = y - 128

    c.drawString(x, y, f"{natureFullLat}")
    y = y - 155
    c.drawString(x, y, f"{natureFullLat}")

    y = 557
    x = x + 170

##12343455

c.setFont("optimaBlack", 9)
c.setFillColor(black)

x = 89
y = 442

for i in range(4):
    
    c.drawString(x, y, f"{natureFullEng}")
    x += 96
    c.drawString(x, y, f"{natureFullEng}")
    y -= 284

    c.drawString(x, y, f"{natureFullEng}")
    x -= 96
    c.drawString(x, y, f"{natureFullEng}")

    y = 442
    x = x + 170


c.setFont("optimaMid", 7)
c.setFillColor(black)

x = 89
y = 435

for i in range(4):
    
    c.drawString(x, y, f"{natureFullLat}")
    x += 96
    c.drawString(x, y, f"{natureFullLat}")
    y -= 284

    c.drawString(x, y, f"{natureFullLat}")
    x -= 96
    c.drawString(x, y, f"{natureFullLat}")

    y = 435
    x = x + 170





################

serialNum = input('Enter the first 8-digits serial number')

while True:  
    litSec = input('Enter the second letter, from A to Z expect I, J, O, W')
    if litSec not in ('I', 'J', 'O', 'W'):
        break
    else:
        print('Retry')

while True:
    serialNum = str(serialNum)
    if serialNum.isdigit() and len(serialNum) == 8:
        serialNum = int(serialNum)
        print('Enter the font for serial numbers')
        numFont = input('OCR A(a or A) or OCR B(b or B):')
        if numFont == 'A' or numFont == 'a':
            numFont = 'oCR_A'
            break
        elif numFont == 'B' or numFont == 'b':
            numFont = 'oCR_B'
            break
    else:
        print = ('Retry')



c.setFont("optimaHeavy", 33)
c.setFillColor(black)

x = 207
y = 555
for i in range(4):
    c.drawString(x, y, f"{litSec}")
    y = y - 64
    y = y - 34
    y = y - 57.5

    c.drawString(x, y, f"{litSec}")
    y = y - 64
    y = y - 34
    y = y - 32

    #

    c.drawString(x, y, f"{litSec}")
    y = y - 64
    y = y - 34
    y = y - 57.5

    c.drawString(x, y, f"{litSec}")
    y = y - 64
    y = y - 34
    
    x = x + 170
    y = 555

print('Generating.       .')
#### Start printing serial numbers

c.setFont(numFont, 9)
c.setFillColor(black)

x = 99
y = 522

for i in range(4):
    for j in range(2):
    
        numFStr, numFInt = serialCumVrifcation(serialNum)
        formatted = formattedFin(serialNum, vrifcation)
        c.drawString(x, y, f"{formatted}")
        y = y - 155
        serialNum += 1
        
        numFStr, numFInt = serialCumVrifcation(serialNum)
        formatted = formattedFin(serialNum, vrifcation)
        c.drawString(x, y, f"{formatted}")
        y = y - 128
        serialNum += 1
    
    y = 522
    x = x + 170
print('Generating..      .')
#########

c.setFont(numFont, 9)
c.setFillColor(black)

x = 111
y = 487

serialNum -= 16
for i in range(4):
    for j in range(2):
    
        numFStr, numFInt = serialCumVrifcation(serialNum)
        formatted = formattedFin(serialNum, vrifcation)
        c.drawString(x, y, f"{formatted}")
        y = y - 34

        numFStr, numFInt = serialCumVrifcation(serialNum)
        formatted = formattedFin(serialNum, vrifcation)
        c.drawString(x, y, f"{formatted}")
        y = y - 120
        
        serialNum += 1
        
        numFStr, numFInt = serialCumVrifcation(serialNum)
        formatted = formattedFin(serialNum, vrifcation)
        c.drawString(x, y, f"{formatted}")
        y = y - 34

        numFStr, numFInt = serialCumVrifcation(serialNum)
        formatted = formattedFin(serialNum, vrifcation)
        c.drawString(x, y, f"{formatted}")
        y = y - 95
        
        serialNum += 1

    y = 487
    x = x + 170
print('Generating...     .')
########

serialNum -= 16
c.setFillColor(black)
text = c.beginText()

x = 72
y = 425
print('Generating....    .')

for i in range(4):
    for j in range(2):
        
        numFStr, numFInt = serialCumVrifcation(serialNum)
        formatted = formattedFin(serialNum, vrifcation)

        digiSep(serialNum)
        text.setTextOrigin(x, y)
        text.setCharSpace(-1.2)
        text.textOut(f"{nature}{litSec}{serialSepChar1}{serialSepChar2}{serialSepChar3}{serialSepChar4}")
        c.drawText(text)
        x += 33

        text.setTextOrigin(x, y)
        text.textOut(f"{serialSepChar5}{serialSepChar6}{serialSepChar7}{serialSepChar8}")
        c.drawText(text)
        x += 21

        text.setTextOrigin(x, y)
        text.textOut(f"{vrifcation}")
        c.drawText(text)
        x += 6
        text.textOut("RD")
        c.drawText(text)

        x = x + 35
        serialNum += 1


        numFStr, numFInt = serialCumVrifcation(serialNum)
        formatted = formattedFin(serialNum, vrifcation)

        digiSep(serialNum)
        text.setTextOrigin(x, y)
        text.setCharSpace(-1.2)
        text.textOut(f"{nature}{litSec}{serialSepChar1}{serialSepChar2}{serialSepChar3}{serialSepChar4}")
        c.drawText(text)
        x += 33

        text.setTextOrigin(x, y)
        text.textOut(f"{serialSepChar5}{serialSepChar6}{serialSepChar7}{serialSepChar8}")
        c.drawText(text)
        x += 21

        text.setTextOrigin(x, y)
        text.textOut(f"{vrifcation}")
        c.drawText(text)
        x += 6
        text.textOut("RD")
        c.drawText(text)

        serialNum += 1

        x -= 155
        y -= 283

    
    y = 425
    x = x + 170
print('Generating.....   .')

###############barcode

codeX = 60
codeY = 532
serialNum -= 16

for k in range(4):
    for i in range(2):
        for j in range(2):
            
            numFStr, numFInt = serialCumVrifcation(serialNum)
            formatted = formattedFin(serialNum, vrifcation)
            formattedCleaned = formatted.replace(" ", "")
            barcodeObj = code128.Code128(formattedCleaned, barHeight=20, barWidth=0.95)
            barcodeObj.drawOn(c, codeX, codeY)
                
            serialNum += 1
            codeY -= 154
        codeY += 22
        
    codeX += 170
    codeY = 532

print('Generating......  .') 

codeX = 80
codeY = 497
serialNum -= 16
print('Generating....... .') 
for l in range(4):
    for k in range(2):
        for j in range(2):
            for i in range(2):

                numFStr, numFInt = serialCumVrifcation(serialNum)
                formatted = formattedFin(serialNum, vrifcation)
                formattedCleaned = formatted.replace(" ", "")
                barcodeObj = code128.Code128(formattedCleaned, barHeight=20, barWidth=0.85)
                barcodeObj.drawOn(c, codeX, codeY)
                            
                codeY -= 34

            codeY -= 87
            serialNum += 1

        codeY += 25

    codeX += 170
    codeY = 497

print('Generating.........') 
c.save()

input('Completed. Press [Enter] to exit')

