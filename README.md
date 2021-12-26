# Common Utils

For now, I just added the script I use to output visualizations in HTML from Python. Will add more utils eventually

## Simple hacky tool for writing HTML files using Python
Beware, here there be bugs and experiments. 

Bare bones syntax:

```
web = html.HTMLPage(filename="vis.html", title="vis") # starts the html file

# let's make a table
web.startTable()

web.startRow()
web.startCol(header=True)
web.writeText("some header")
web.endCol()
web.startCol(header=True)
web.writeText("Another header")
web.endCol() 
web.startCol(header=True)
web.writeText("yet another header")
web.endCol() # these endCol and endRow's are optional, but safer to include them. 
web.endRow() # these endCol and endRow's are optional, but safer to include them.

web.startRow()
web.startCol()
web.writeText("<b> some text </b>") # can include any html tags in the writeText()
web.endCol()
web.startCol()
web.writeImage("/path/to/image/file.png", width=290, height=290)
web.endCol()
web.startCol()
web.embed_audio("/path/to/audio/file.mp3")
web.endCol()
web.endRow()

web.endTable()
```



