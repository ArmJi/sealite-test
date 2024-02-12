symbolValues = [["A",1],["B",5],["Z",10],["L",50],["C",100],["D",500],["R",1000]]

def convertValue(symbols):
    contents = []
    for indexSymbols in range (len(symbols)):
        for indexSymbolValues in range (len(symbolValues)):
            symbol = symbols[indexSymbols]
            symbolValue = symbolValues[indexSymbolValues][1]
            if symbol == symbolValues[indexSymbolValues][0]:
                contents.append(symbolValue)
    result = 0
    indexContents = 0
    while indexContents < (len(contents)):
        nextIndexContents = indexContents + 1
        if indexContents != len(contents) - 1: 
            if contents[indexContents] >= contents[nextIndexContents]:
                result += contents[indexContents]
                indexContents += 1
            else:
                result += (contents[nextIndexContents] - contents[indexContents])
                indexContents += 2
        else: 
            result += contents[indexContents]
            indexContents += 1
    print("Output: ", result)

while True:
    symbols = str(input("Input: s = "))
    convertValue(symbols)
