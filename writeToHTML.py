'''
@author: Arijit Ray
Support file for writing stuff to HTML files in python so that people can visualize stuff. 
Beware: simple and hacky : here there be experiments. Output might not look like the prettiest webpage in the world. 
10/10/16
'''

import os
import datetime
from random import shuffle
import pdb
import urllib.parse

class HTMLPage:
    def __init__(self, filename, title, append=False):
        self.fileName = filename
        if append == True:
            with open(self.fileName, "a") as f:
                print("<p> appending to file at :" + str(datetime.datetime.now()) + " </p>", file=f)
        else:
            with open(self.fileName, "w") as f:
                s='<meta charset="utf-8">\
                    <meta name="viewport" content="width=device-width, initial-scale=1">\
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">\
                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>\
                    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>'
                print(s, file=f)
                print("<title>", file=f)
                print(str(title), file=f)
                print("</title>", file=f)
                print("<head>", file=f)
                print("<h2> " + str(title) + "</h2>", file=f)
                print("<p> Run Date and Time: " + str(datetime.datetime.now()) + " </p>", file=f)
                print("</head>", file=f)
                print("<body><div class='container-fluid'>", file=f)
        self.RowStarted = False
        self.TableStarted=False
        self.ColStarted=False
        self.colHeader = False

    def writeImage(self, imageFile, width=250, height=250):
        #imageFile = self.make_url_safe(imageFile)
        with open(self.fileName, 'a') as f:
            print("<img src=\"" + imageFile + "\" width=" + str(width) + " height=" + str(height) + ">", file=f)

    def writeTextList(self, textlist):
        with open(self.fileName, 'a') as f:
            for text in textlist:
                print(" &nbsp; " + text + " &nbsp; ", file=f)

    def writeText(self, text):
        with open(self.fileName, 'a') as f:
            print(" " + str(text) + " ", file=f)

    def breakLine(self):
        with open(self.fileName, 'a') as f:
            print("<br/>", file=f)

    def horizontal_line(self):
        with open(self.fileName, 'a') as f:
            print("<hr/>", file=f)

    def startTable(self):
        with open(self.fileName, 'a') as f:
            if self.TableStarted:
                self.endTable()
            self.TableStarted = True
            print('<table class="table">', file=f)

    def endTable(self):
        self.TableStarted = False
        with open(self.fileName, 'a') as f:
            if self.ColStarted:
                if self.colHeader:
                    print("</th>", file=f)
                else:
                    print("</td>", file=f)
                self.ColStarted=False

            if self.RowStarted:
                print("</tr>", file=f)
                self.RowStarted = False
            print("</table>", file=f)

    def startRow(self):
        with open(self.fileName, 'a') as f:
            if self.ColStarted:
                if self.colHeader:
                    print("</th>", file=f)
                else:
                    print("</td>", file=f)
            if self.RowStarted:
                print("</tr>", file=f)
            self.RowStarted = True
            print("<tr>", file=f)

    def endRow(self):
        self.RowStarted = False
        with open(self.fileName, 'a') as f:
            print("</tr>", file=f)

    def startCol(self, header=False):

        with open(self.fileName, 'a') as f:
            if self.ColStarted:
                if self.colHeader:
                    print("</th>", file=f)
                else:
                    print("</td>", file=f)
            self.colHeader = header
            self.ColStarted=True
            if header == False:
                print("<td>", file=f)
            else:
                print("<th>", file=f)

    def endCol(self):
        self.ColStarted = False
        with open(self.fileName, 'a') as f:
            if self.colHeader == False:
                print("</td>", file=f)
            else:
                print("</th>", file=f)

    def closeHTMLFile(self):
        with open(self.fileName, 'a') as f:
            print("<hr />", file=f)
            print("</div></body>", file=f)
            print("</html>", file=f)

    def make_bar_chart(self, rating_array, rating_labels, max_value):
        #assumes a list of values
        s=""
        for entry, label in zip(rating_array, rating_labels): 
            s+='<div class="progress">\n'
            s+='\t<div class="progress-bar" role="progressbar" aria-valuenow="'+str(entry)+'" aria-valuemin="0" aria-valuemax="'+str(max_value)+'" style="width:'+str(entry)+'%">\n'
            s+=label + " " +str(entry)
            s+='</div></div>\n'

        with open(self.fileName, 'a') as f:
            print(s, file=f)

    
    def embed_audio(self, audio_file):
        s = ""

        #audio_file = self.make_url_safe(audio_file)
        s+='<audio controls src="'+audio_file+'"> Your browser does not support the <code>audio</code> element. </audio>'

        with open(self.fileName, 'a') as f:
            print(s, file=f)

    
    def make_url_safe(self, link):
        link_c = link.split("/")
        link_f = "/".join([urllib.parse.quote_plus(l) for l in link_c])
        return link_f

    