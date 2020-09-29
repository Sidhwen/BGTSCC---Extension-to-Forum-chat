def ReplaceFirst(Index, searchLine, searchString, replaceString):
    global startIndex
    startIndex = len(searchLine[0 : line.find(searchString, Index, len(searchLine))] + replaceString)
    searchLine = searchLine[0 : line.find(searchString, Index, len(searchLine))] + replaceString + searchLine[line.find(searchString, Index, len(searchLine)) + len(searchString) : len(searchLine)]
    return searchLine

print ("Process Started...")

f = open("input.txt", "r")
fw = open("output.txt", "w")

#hashmap for player colors
Rainbow = 0
playerColors = {}
colorPicker = {1:"[color=#FF0000]",2:"[color=#FFBF00]",3:"[color=#80BFFF]",4:"[color=#808080]",5:"[color=#FFBFBF]",6:"[color=#FF8080]",7:"[color=#FF8000]",8:"[color=#808040]",9:"[color=#40BF80]",10:"[color=#BF80FF]"}
maxColors = 10
currentColor = 1

for line in f:

    if (len(line) > 1 and line.find("[DM]", 0, len(line)) == -1):
        #print(line)
        #manual just to get us started
        line = "[color=#FF00FF]" + line[line.find("[", 0, len(line)) + 1: len(line)]
        startIndex = 15

        line = ReplaceFirst(startIndex, line, "]", "[/color]")
        

        currentPlayer = line[startIndex : line.find(":", startIndex, len(line))]
        
        if (currentPlayer not in playerColors):
            playerColors[currentPlayer] = colorPicker[currentColor]
            currentColor = currentColor + 1
            if (currentColor > 10):
                currentColor = 1
        
        
        if (line.find("[", startIndex, line.find("[Talk]", startIndex, len(line)) - 1) > 0 or line.find("[Shout]", 0, len(line)) > 0):
            
            if (Rainbow == 1):
                line = ReplaceFirst(startIndex, line, "[", playerColors[currentPlayer] + "[b][")
            else:
                line = ReplaceFirst(startIndex, line, "[", "[color=#BF8040][b][")
            line = ReplaceFirst(startIndex, line, "]", "][/b]")
        else:
           
            bufferIndex = len(line[0 : startIndex] + "[color=#BF8040]")
            line = line[0 : startIndex] + "[color=#BF8040]" + line[startIndex : len(line)]
            startIndex = bufferIndex
    
        #manual to remove [Shout] and [Talk] tags
        bufferIndex = len (line[0 : line.find("[", startIndex, len(line))] + "[/color]")
        line = line[0 : line.find("[", startIndex, len(line))] + "[/color]" +  line[line.find("]", startIndex, len(line)) + 2 : len(line)]
        startIndex = bufferIndex
    
        #<C=#00BFFF> chat tags
    
        NoQuit = 0
        while (line.find("<C=#00BFFF>", startIndex, len(line)) > -1 and NoQuit == 0):
            bufferLine = ReplaceFirst(startIndex, line, "<C=#00BFFF>", "[color=#0080FF]")
            if (bufferLine.find("</C>", startIndex, len(bufferLine)) == -1):
                line = bufferLine + "[/color]"
                NoQuit = 1
            else:
                line = bufferLine
                line = ReplaceFirst(startIndex, line, "</C>", "[/color]")
        
        startIndex = bufferIndex
    
        #<C=#66CC66> chat tags
    
        NoQuit = 0
        while (line.find("<C=#66CC66>", startIndex, len(line)) > -1 and NoQuit == 0):
            bufferLine = ReplaceFirst(startIndex, line, "<C=#66CC66>", "[color=#66CC66]")
            if (bufferLine.find("</C>", startIndex, len(bufferLine)) == -1):
                line = bufferLine + "[/color]"
                NoQuit = 1
            else:
                line = bufferLine
                line = ReplaceFirst(startIndex, line, "</C>", "[/color]")
        
    
        startIndex = bufferIndex
        # * chat tags
    
        NoQuit = 0
        while (line.find("*", startIndex, len(line)) > -1 and NoQuit == 0):
            bufferLine = ReplaceFirst(startIndex, line, "*", "[color=#0080FF]")
            if (bufferLine.find("*", startIndex, len(bufferLine)) == -1):
                NoQuit = 1
            else:
                line = bufferLine
                line = ReplaceFirst(startIndex, line, "*", "[/color]")
    
    #line = ReplaceFirst(startIndex, line, 
    print(line)
    
    if (line.find("Player joins:") == -1 and line.find("Player leaves:") == -1 and line.find("[Tell]") == -1):
        fw.write(line)

wait = input("PRESS ENTER TO FINISH.")

