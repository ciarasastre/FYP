from flask import Flask, render_template, request,jsonify, Response, redirect, url_for
from pylatex import Document, Section, Subsection, Command, Figure, Package, Head, PageStyle, Foot,simple_page_number,NewPage, HugeText, MiniPage, SmallText, Enumerate, Itemize, Description, LargeText
from PyPDF2 import PdfFileWriter, PdfFileReader
from pylatex.utils import bold, italic, NoEscape
import os
import json
import pprint
import re
import PyPDF2
import base64
import urllib.request

app = Flask(__name__)

title_name = "";
num = 3;

@app.route("/img")
def img():
	
	file_path = 'static/img/'
	url = "data:image/jpeg;base64,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"
	#url = "http://127.0.0.1:5000/b6f95861-d65f-4b1f-8ab6-a310ae577824"
	file_name = "test"

	full_path = file_path + file_name + '.jpg'
	urllib.request.urlretrieve(url,full_path) # download to path

	#img(url,'static/img/',file_name)

	#base_image = new Image();
	#base_image = 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"
	#fh = open("imageToSave.png", "wb")
	#fh.write((base_image)) #str.decode
	#fh.close()

	#video_stream = "hello"

	#with open('file.webm', 'w') as f_vid:
	#    f_vid.write(base64.b64encode(video_stream))

	#with open('file.webm', 'r') as f_vid:
	#    video_stream = base64.b64decode(f_vid.read())

	#img = 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


	#with open('file.png', 'w') as f_vid:
	#	f_vid.write(base64.b64encode(img))

	#print video_stream
	return ("Done")

@app.route("/delete", methods=["GET", "POST"])
def delete():

	newTitle = request.form["newTitle"]
	
	global title_name

	#Now set new title name
	title_name = newTitle

	#open bookEdit 
	with open('./templates/json/bookEdit.json', 'r') as openBookEdit:
		contents = json.load(openBookEdit)

		# LOAD THE DATA
		books = contents["books"]

		found = None

		for i in range(len(books)):
			if title_name in books[i]:
				found = books[i]
				books.pop(i)
				break

		with open('./templates/json/bookEdit.json', 'w') as Book: #
			json.dump(contents,Book)

	return redirect(url_for('profile'))

@app.route("/test")
def test():
	#title_name = "test"
	# Opening JSON file FOR HTML EDITING
	return render_template("json/"+title_name+".json")# render_template("json/book.json")

@app.route("/displayEdit", methods=["GET"])
def displayEdit():

	return render_template("json/bookEdit.json")

@app.route("/bookMode", methods=["GET", "POST"])
def bookMode():
	#Revieve the title name and change this global title name and direct it to editor
	newTitle = request.form["bookName"]
	
	global title_name

	#Now set new title name
	title_name = newTitle
	return '', 204

@app.route("/editMode", methods=["GET", "POST"])
def editMode():
	#Revieve the title name and change this global title name and direct it to editor
	newTitle = request.form["newTitle"]
	
	global title_name

	#Now set new title name
	title_name = newTitle
	return redirect(url_for('editor'))

@app.route("/displayLibrary", methods=["GET"])
def displayLibrary():

	return render_template("json/bookLibrary.json")

@app.route("/libMode", methods=["GET", "POST"])
def libMode():

	#Revieve the title name and change this global title name and direct it to editor
	libTitle = request.form["libTitle"]
	
	global title_name

	#Now set new title name
	title_name = libTitle

	#Now open the json file with that title
	with open('./templates/json/'+title_name+'.json', 'r') as openBook:
		info = json.load(openBook)

		# LOAD THE DATA
		author_name = info["author_name"]

	#Now open library to put new info in
	with open('./templates/json/bookLibrary.json', 'r') as LibBook:
		data = json.load(LibBook)

		#First two lines reset the data
		#data = {}  
		#data["books"] = []
		data["books"].append({  
		    "book": {
		  	"auth": author_name,
		   	"title_n": title_name
		    },
	})

	#Close and write all info to it
	with open('./templates/json/bookLibrary.json', 'w') as Book: #
		json.dump(data,Book)

	#return(title_name)
	#return render_template("KWLibrary.html")
	return redirect(url_for('library'))
	

#Connect to the Site Here:
@app.route("/")
def hello():
	return render_template("KWHome.html")

#Have all links here:
@app.route("/home")
def home():
	return render_template("KWHome.html")

@app.route("/profile")
def profile():
	return render_template("KWProfile.html")

@app.route("/library")
def library():
	return render_template("KWLibrary.html")

@app.route("/soon")
def soon():
	return render_template("KWSoon.html")

@app.route("/editor")
def editor():
	return render_template("KWEditor.html")

#End of new links

@app.route("/edit")
def edit():
	return render_template("bookEdit.html");

@app.route("/updateChap", methods=["GET","POST"])
def updateChap():

	global title_name;

	num = request.form["chapter"]

	#Open json file & edit text
	#with open('./templates/json/'+title_name+'.json', 'r') as editBook:
	#	data = json.load(editBook)

	#Now if new chapter is added it should be saved
	#data = {}  
	#data["chapters"] = []
	#data["chapters"].append({  
	#	    "chp" + num: "This is another chapter!"
	#	})


	#with open('./templates/json/' +title_name+ '.json', 'w') as editBook:
	#	json.dump(data, editBook)
	#return render_template("KWProfile.html")
	return '', 204


@app.route("/update", methods=["GET","POST"])
def update():

	global title_name;

	newText = request.form["new_text"]
	area = request.form["area"]

	#Open json file & edit text
	with open('./templates/json/'+title_name+'.json', 'r') as editBook:
		data = json.load(editBook)

	#Starting
	if area == "start":
		data["chapters"]["ch1"]= newText

	# PUT TEXT IN THEIR PROPER AREAS
	if area == "cp":
		data["template"]["coverpage"] = newText
		
	if area == "aknow":
		data["aknow"] = newText

	if area == "main":
		data["chapters"]["ch1"] = newText

	if area == "toc":
		data["toc"] = newText

	#Now if new chapter is added it should be saved

	with open('./templates/json/' +title_name+ '.json', 'w') as editBook:
		json.dump(data, editBook)
	#return render_template("KWProfile.html")
	return '', 204
	
#Getting title name back from HTML
@app.route("/book", methods=["GET","POST"])
def book():

	global title_name;

	# Build JSON Object from form in HTML
	title_name = request.form["title_name"] #Get HTML put into new var title_name
	author_name = request.form["author_name"]
	template = request.form["template"]

	#First create book in the editor
	#Open to edit
	with open('./templates/json/bookEdit.json', 'r') as EditBook:
		data = json.load(EditBook)

		# LOAD THE DATA

		#First two lines reset the data
		#data = {}  
		#data["books"] = []
		data["books"].append({  
		    title_name: {
		  	"auth": author_name,
		   	"title_n": title_name
		    },
		})

	#Close and write all info to it
	with open('./templates/json/bookEdit.json', 'w') as Book: #with open('./templates/json/book.json', 'w') as Book:
		json.dump(data,Book)

	#Then go onto the creation of the books json

	# Check templates first
	if template == "default":
		templateType = "default"
		fontfamily = "Times"
		border = "no"
		align = "left"
		coverpage = "default"
		aknow = "yes"
		toc = "yes"

	if template == "harrypotter":
		templateType = "harrypotter"
		fontfamily = "Arial"
		border = "yes"
		align = "left"
		coverpage = "harrypotter"
		aknow = "yes"
		toc = "yes"

	if template == "wtp":
		templateType = "wtp"
		fontfamily = "Impact"
		border = "yes"
		align = "center"
		coverpage = "wtp"
		aknow = "yes"
		toc = "yes"

	if template == "custom":
		templateType = "custom"
		coverpage = "default"
		fontfamily = request.form["fontfamily"]
		border = request.form["border"]
		align = request.form["align"]
		aknow = request.form["aknow"]
		toc = request.form["toc"]

	# Create new format for JSON Here
	newBook = {
		"title_name" : title_name,
		"author_name" : author_name,
		"chapters": 
			{
				"ch1" : "Begin writing your story here...",
			},
		"template": 
			{
				"type": templateType,
				"coverpage": coverpage,
				"fontfamily" : fontfamily,
				"border": border,
				"align": align,
			},
	}

	# Include aknowledgements if they asked
	if aknow == 'yes':
		newBook["aknow"] = "This is your acknowledgements section"
	else:
		newBook["aknow"] = "noAknow123"

	# Include table of contents if they asked
	if toc == 'yes':
		newBook["toc"] = "This is your table of contents section"
	else:
		newBook["toc"] = "noToc123"

	#Creates .json file in json folder
	#Uses titlename as JSON File name
	with open('./templates/json/' + title_name + '.json', 'w') as Book: #with open('./templates/json/book.json', 'w') as Book:
		json.dump(newBook,Book)

	#return '', 204
	#return render_template('KWEditor.html')
	return redirect(url_for('editor'))
	
@app.route("/latex") #, methods=["GET","POST"]
def latex():

	global title_name;

	# VARIABLES
	boldswitch = 0
	italicswitch = 0
	normalswitch = 1

	#title_name = "test" # NEEDS TITLE HERE

	#Open json file & edit text
	with open('./templates/json/' +title_name+ '.json', 'r') as PDFBook:
		data = json.load(PDFBook)

		#Start pulling data from JSON file
		title_name = data["title_name"]
		author_name = data["author_name"]
		mainText = data["chapters"]["ch1"]
		fontfamily = data["template"]["fontfamily"]
		coverpage = data["template"]["coverpage"]
		border = data["template"]["border"]
		align = data["template"]["align"]
		aknow = data["aknow"]
		toc = data["toc"]

	book = Document(fontenc = 'T1')

	##RULE FOR COVERPAGE
	#if coverpage == 'yes':
	coverpage = coverpage.replace("<p>", "") # remove <p>
	coverpage = coverpage.replace("</p>", "") # remove <p>
	coverpageRule(book, coverpage)
	book.append(NewPage())

	
	####RULE FOR AKNOW
	aknow = aknow.replace("<p>", "") # remove <p>
	aknow = aknow.replace("</p>", "\n") # at the end return

	#Dont need </span> tag
	aknow = aknow.replace("</span", "")

	###RULE FOR FIXING SPACE BUG THIS GOES AT THE END
	aknow = aknow.replace("<", " <") # place spaces so tags can be read
	aknow = aknow.replace(">", "> ")

	aknow = aknow.replace("&", " &") # place spaces so tags can be read
	aknow = aknow.replace(";", "; ") 

	## Center the Aknow ###
	book.append(Command('centering'))

	if aknow == "noAknow123":
		aknow = ""

	book_text = aknow

	for word in book_text.split(): #Iterate through each word

		### RULE FOR BOLD ###
		if word == '<strong>':
			boldswitch = 1  #turn switch on
			normalswitch = 0
			boldFound = boldRule(book,word,book_text)

		#Is you reached the end turn the switch off
		if word == '</strong>':
			boldswitch = 0
			normalswitch = 1
			# skip this word here

		### RULE FOR ITALICS ###
		if word == '<em>':
			italicswitch = 1  #turn switch on
			normalswitch = 0
			italicFound = italicRule(book,word,book_text)

		#Is you reached the end turn the switch off
		if word == '</em>':
			italicswitch = 0
			normalswitch = 1
			# skip this word here

		## RULE FOR FONT ##
		if word == '<span':
			normalswitch = 0

		#IF normal switch is on continue printing words
		if normalswitch == 1:
			if word != '</strong>':
				if word!= '</em>':
					if word!= '&nbsp;':
						book.append(word + ' ')#print the word and a space word +


	## AKNOWLEDGEMENTS GET APPENDED ####
	#book.append(aknow)
	book.append(NewPage())

	##TABLE OF CONTENTS HAS ITS OWN STYLE ###
	####RULE FOR AKNOW
	toc = toc.replace("<p>", "") # remove <p>
	toc = toc.replace("</p>", "\n") # at the end return

	#Dont need </span> tag
	toc = toc.replace("</span", "")

	###RULE FOR FIXING SPACE BUG THIS GOES AT THE END
	toc = toc.replace("<", " <") # place spaces so tags can be read
	toc = toc.replace(">", "> ")

	toc = toc.replace("&", " &") # place spaces so tags can be read
	toc = toc.replace(";", "; ") 

	## Center the Aknow ###
	book.append(Command('centering'))

	if toc == "noToc123":
		toc = ""

	book_text = toc

	for word in book_text.split(): #Iterate through each word

		### RULE FOR BOLD ###
		if word == '<strong>':
			boldswitch = 1  #turn switch on
			normalswitch = 0
			boldFound = boldRule(book,word,book_text)

		#Is you reached the end turn the switch off
		if word == '</strong>':
			boldswitch = 0
			normalswitch = 1
			# skip this word here

		### RULE FOR ITALICS ###
		if word == '<em>':
			italicswitch = 1  #turn switch on
			normalswitch = 0
			italicFound = italicRule(book,word,book_text)

		#Is you reached the end turn the switch off
		if word == '</em>':
			italicswitch = 0
			normalswitch = 1
			# skip this word here

		## RULE FOR FONT ##
		if word == '<span':
			normalswitch = 0

		#IF normal switch is on continue printing words
		if normalswitch == 1:
			if word != '</strong>':
				if word!= '</em>':
					if word!= '&nbsp;':
						book.append(word + ' ')#print the word and a space word +

	book.append(NewPage())

	book.preamble.append(Command('title', title_name)) # Would need users input here
	book.preamble.append(Command('author', author_name)) # Would need users name
	book.preamble.append(Command('date', NoEscape(r'\today'))) 
	book.append(NoEscape(r'\maketitle')) #maketitle is an actual command
	

	###############################   RULES START HERE ########################################

	## REMOVAL RULES BEFORE SPLITTING

	##RULE FOR FONT#####
	fontRule(book, fontfamily)

	####RULE FOR PARAGRAPH
	mainText = mainText.replace("<p>", "") # remove <p>
	mainText = mainText.replace("</p>", "\n") # at the end return

	#Dont need </span> tag
	mainText = mainText.replace("</span", "")

	###RULE FOR FIXING SPACE BUG THIS GOES AT THE END
	mainText = mainText.replace("<", " <") # place spaces so tags can be read
	mainText = mainText.replace(">", "> ")

	mainText = mainText.replace("&", " &") # place spaces so tags can be read
	mainText = mainText.replace(";", "; ") 

	## RULE FOR ALIGN ###
	if align == 'left':
		book.append(Command('flushleft'))

	if align == 'center':
		book.append(Command('centering'))

	if align == 'right':
		book.append(Command('flushright'))

	book_text = mainText
	for word in book_text.split(): #Iterate through each word

		### RULE FOR BOLD ###
		if word == '<strong>':
			boldswitch = 1  #turn switch on
			normalswitch = 0
			boldFound = boldRule(book,word,book_text)

		#Is you reached the end turn the switch off
		if word == '</strong>':
			boldswitch = 0
			normalswitch = 1
			# skip this word here

		### RULE FOR ITALICS ###
		if word == '<em>':
			italicswitch = 1  #turn switch on
			normalswitch = 0
			italicFound = italicRule(book,word,book_text)

		#Is you reached the end turn the switch off
		if word == '</em>':
			italicswitch = 0
			normalswitch = 1
			# skip this word here

		## RULE FOR FONT ##
		if word == '<span':
			normalswitch = 0

		#IF normal switch is on continue printing words
		if normalswitch == 1:
			if word != '</strong>':
				if word!= '</em>':
					if word!= '&nbsp;':
						book.append(word + ' ')#print the word and a space word +

	# Iterating words is over <-- Here

	# Generate PDF
	#book.generate_pdf('./LaTeXFiles/' +title_name+'LaTeX', clean_tex=False)

	book.generate_pdf('./static/styles/latex/' +title_name+'LaTeX', clean_tex=False)
	tex=book.dumps() # The document as a string in LaTeX syntax
	book.generate_tex() 
	#return "Your Book is called %s" %(title_name)
	
	if border == 'yes':
		borderRule(title_name)

	#return "Your Book is called %s" %(title_name)
	#return render_template('KWLibrary.html')
	return '', 204
	#return redirect(url_for('editor'))

############# RULES #################
def coverpageRule(book, coverpage):
	#doc.packages.append(Package('fullpage'))

	#Images and relative paths
	scriptDir = os.path.dirname(__file__)

	if coverpage == "default":
		imageCoverPath = "./static/img/defaultcover.jpg" 

	if coverpage == "harrypotter":
		imageCoverPath = "./static/img/harryPotter.jpg" 

	if coverpage == "wtp":
		imageCoverPath = "./static/img/wtpcover.jpg"

	
	image_covername = os.path.join(scriptDir, imageCoverPath)

	#doc.append(Package(image_covername, base='includegraphics', option='scale=0.5'))
	#COVER PAGE SECTION
	with book.create(Figure(position='h!')) as coverImage: #h!
	    coverImage.add_image(image_covername, width='300px')  
	   
	#book.append(NewPage())
	return()

def borderRule(title_name):
	# This combines the background PDF with the wording (base) PDF 
	input_pdf='./static/styles/latex/'+title_name+'LaTeX.pdf' #'./LaTeXFiles/'+title_name+'LaTeX.pdf'	#'./static/watermark/HarryPBase.pdf'
	output_pdf='./static/styles/latex/'+title_name+'LaTeX.pdf' #'./LaTeXFiles/'+title_name+'LaTeX.pdf'#'./LaTeXFiles/'+title_name+'FINALLaTeX.pdf' #This replaces previous file
	watermark_pdf='./static/watermark/HarryPBG.pdf'

	#Setting up here
	watermark = PdfFileReader(watermark_pdf)
	watermark_page = watermark.getPage(0)
	pdf = PdfFileReader(input_pdf)
	pdf_writer = PdfFileWriter()
		
	for page in range(pdf.getNumPages()):
		#If its the first page skip it for merging
		#But still write it
		if page == 0:
			pdf_page = pdf.getPage(page)
			pdf_writer.addPage(pdf_page)
		else:
			pdf_page = pdf.getPage(page)
			pdf_page.mergePage(watermark_page)
			pdf_writer.addPage(pdf_page)

	with open(output_pdf, 'wb') as fh:
		pdf_writer.write(fh)
	return()

def fontRule(book, fontfamily):
	##RULE FOR FONT#####
	# IMPACT
	if fontfamily == 'Impact':
		book.packages.append(Package('cyklop')) #asciifamily
		book.append(NoEscape(r'\normalfont'))

	# ARIAL
	if fontfamily == 'Arial':
		book.append(NoEscape(r'\sffamily')) #Sansserrif

	# TIMES NEW ROMAN
	if fontfamily == 'Times':
		book.append(NoEscape(r'\rmfamily'))

	# If its empty default to times new roman
	if fontfamily == '':
		book.append(NoEscape(r'\rmfamily'))

def boldRule(book,word,book_text):
	#bold rules:
	startbold = "<strong>"
	endbold = "</strong>"
	boldWord = book_text[book_text.find(startbold) + len(startbold):book_text.find(endbold)] # middle word
	book.append(bold(boldWord))
	return()

def italicRule(book,word,book_text):
	#italic rules:
	startitalic = "<em>"
	enditalic = "</em>"
	italicWord = book_text[book_text.find(startitalic) + len(startitalic):book_text.find(enditalic)] # middle word
	book.append(italic(italicWord))
	return()
###################################################################################################################

@app.route("/HPDemo")
def testing():
	#import pylatex.config as cf

	#Images and relative paths
	scriptDir = os.path.dirname(__file__)
	imageCoverPath = "./static/img/harryPotter.jpg" #harryPotter.jpg
	imageBabyPath = "./static/img/baby.jpg"
	image_covername = os.path.join(scriptDir, imageCoverPath)
	image_baby = os.path.join(scriptDir, imageBabyPath)
	
	book = Document('Basic', inputenc = 'utf8x', fontenc = 'T1')#textcomp = None lmodern = False,

	#COVER PAGE SECTION
	with book.create(Figure(position='h!')) as coverImage:
	    coverImage.add_image(image_covername, width='300px')  
	   
	book.append(NewPage())
	
	##### TEST FOR CUSTOM / PRETTY FONTS ############
	book.packages.append(Package('ascii')) #asciifamily
	book.append(NoEscape(r'\asciifamily')) 
	
	
	#NB This adds controls which are in LATEX to PYLATEX very handy
	#book.append(NoEscape(r'\ttfamily')) #Teletype font
	#book.append(NoEscape(r'\sffamily')) #Sansserrif
	#book.append(NoEscape(r'\rmfamily')) #Roman font AKA Normal
	#book.append(NoEscape(r'\scshape')) # Small Capitol
	book.append(Command('centering'))
	book.append(HugeText(bold("HARRY POTTER \n")))
	book.append(LargeText(bold("And the Philosopher's Stone")))
	book.append(NewPage())
	# ALSO BY SECTION
	
	with book.create(Section('ALSO BY J.K ROWLING',numbering=False)):
		with book.create(Subsection('Harry Potter and the Sorcerers Stone',numbering=False)):
			book.append("Year One at Hogwarts")
			
		with book.create(Subsection('Harry Potter and the Chamber of Secrets',numbering=False)):
			book.append("Year Two at Hogwarts")
			 
		with book.create(Subsection('Harry Potter and the Prisoner of Azkaban',numbering=False)):
			book.append("Year Three at Hogwarts")
			
		with book.create(Subsection('Harry Potter and the Goblet of Fire',numbering=False)):
			book.append("Year Four at Hogwarts")
			
		with book.create(Subsection('Harry Potter and the Oder of the Phoenix',numbering=False)):
			book.append("Year Five at Hogwarts")
			
		with book.create(Subsection('Harry Potter and the Half-Blood Prince',numbering=False)):
			book.append("Year Six at Hogwarts")
			
		with book.create(Subsection('Harry Potter and the Deathly Hallows',numbering=False)):
			book.append("Year Seven at Hogwarts")
			      
	book.append(NewPage())
	
	#AKNOWLEDGEMENTS SECTION
	book.append(LargeText(bold("For Sean D. F Harris \n \n")))
	book.append(LargeText(bold("Getaway Driver and Foul-Weather Friend \n"))) 

	book.append(SmallText('''Text copywrite @ 1999 by J.K Rowling.
	Donec pellentesque libero id tempor aliquam. Maecenas a diam at metus varius
			rutrum vel in nisl. Maecenas a est lorem. Vivamus tristique nec eros ac
			hendrerit. Vivamus imperdiet justo id lobortis luctus. Sed facilisis ipsum ut
			tellus pellentesque tincidunt. Mauris libero lectus, maximus at mattis ut,
			venenatis eget diam. Fusce in leo at erat varius laoreet. Mauris non ipsum
			pretium, convallis purus vel, pulvinar leo. Aliquam lacinia lorem dapibus
			tortor imperdiet, quis consequat diam mollis.'''))
			              
	book.append(NewPage())
	# TABLE OF CONTENTS SECTION
	book.append(Command('centering'))
	with book.create(Section('CONTENTS Numbering',numbering=False)):
		with book.create(Description()) as desc:
			book.append(Command('centering'))
			desc.add_item("ONE", "The first item")
			desc.add_item("TWO", "The second item")
			desc.add_item("THREE", NoEscape("The third etc \\ldots"))
	
	# TRY HAVE SECTION SUB SECTION ETC
	book.append(Command('centering'))
	with book.create(Section('CONTENTS Sections',numbering=False)):
		with book.create(Subsection('ONE',numbering=False)):
			book.append("The first item")
			  
		with book.create(Subsection('TWO',numbering=False)):
			book.append("The second item")
			   
		with book.create(Subsection('THREE',numbering=False)):
			book.append("The third etc \\ldots")
	      
	book.append(NewPage())
	
	# Create center header
	header = PageStyle("header")

	with header.create(Head("C")): # C for Centre
		header.append("CHAPTER ONE")

	# Create center footer with the page numbers
	with header.create(Foot("C")):
		#header.append(simple_page_number())
		book.preamble.append(header)
		book.change_document_style("header") 

	# Add image of baby
	with book.create(Figure(position='h!')) as image:
		image.add_image(image_baby, width='200px')

	#book.append(Command('centering'))
	with book.create(Section('THE BOY WHO LIVED',numbering=False)):
		book.append(Command('flushleft'))
		book.append(''' Not for the first time, an argument had broken out over breakfast at number four, Privet Drive.
	Mr. Vernon Dursley had been woken in the early hours of the morning by a loud, hooting noise from his nephew
	Harry’s room.“Third time this week!” he roared across the table. “If you can’t control that owl, it’ll have to go!” 
	Harry tried, yet again, to explain.“She’s bored,” he said. “She’s used to flying around outside.
	If I could just let her out at night —” “Do I look stupid?” snarled Uncle Vernon, a bit of fried egg dangling
	from his bushy mustache. “I know what’ll happen if that owl’s let out.” He exchanged dark looks with his wife, Petunia. 
	Harry tried to argue back but his words were drowned by a long, loud belch from the Dursleys’ son, Dudley.
	“I want more bacon.” “There’s more in the frying pan, sweetums,” said Aunt Petunia,
	turning misty eyes on her massive son. “We must build you up while we’ve got the chance. . . .
	I don’t like the sound of that school food. . . .” “Nonsense, Petunia, I never went hungry when I was at Smeltings,”
	said Uncle Vernon heartily. “Dudley gets enough, don’t you, son?” 

	Dudley, who was so large his bottom drooped over either side of the kitchen chair, grinned and turned to Harry.
	“Pass the frying pan.” “You’ve forgotten the magic word,” said Harry irritably.
	The effect of this simple sentence on the rest of the family was incredible: Dudley gasped and fell off his chair
	with a crash that shook the whole kitchen; Mrs. Dursley gave a small scream and clapped her hands to her mouth;
	Mr. Dursley jumped to his feet, veins throbbing in his temples. “I meant ‘please’!” said Harry quickly.
	“I didn’t mean —” “WHAT HAVE I TOLD YOU,” thundered his uncle, spraying spit over the table,
	“ABOUT SAYING THE ‘M’ WORD IN OUR HOUSE?” “But I —” “HOW DARE YOU THREATEN DUDLEY!” roared Uncle Vernon,
	pounding the table with his fist. “I just —” “I WARNED YOU! I WILL NOT TOLERATE MENTION OF YOUR ABNORMALITY
	UNDER THIS ROOF!” Harry stared from his purple-faced uncle to his pale 
	aunt, who was trying to heave Dudley to his feet. 

	Dudley hitched up his trousers, which were slipping down his fat bottom. “Why’re you staring at the hedge?” 
	he said suspiciously. “I’m trying to decide what would be the best spell to set it on fire,” said Harry.
	Dudley stumbled backward at once, a look of panic on his fat face. “You c-can’t — Dad told you you’re
	not to do m-magic — he said he’ll chuck you out of the house — and you haven’t got anywhere else to 
	go — you haven’t got any friends to take you —” “Jiggery pokery!” said Harry in a fierce voice. 
	“Hocus pocus — squiggly wiggly —” “MUUUUUUM!” howled Dudley, tripping over his feet as he dashed
	back toward the house. “MUUUUM! He’s doing you know what!” Harry paid dearly for his moment of fun.
	As neither Dudley nor the hedge was in any way hurt, Aunt Petunia knew he hadn’t really done magic,
	but he still had to duck as she aimed a heavy blow at his head with the soapy frying pan.
	Then she gave him work to do, with the promise he wouldn’t eat again until he’d finished.
	While Dudley lolled around watching and eating ice cream, Harry cleaned the windows,
	washed the car, mowed the lawn, trimmed the flowerbeds, pruned and watered the roses, 
	and repainted the garden bench. The sun blazed overhead, burning the back of his neck. 
	Harry knew he shouldn’t have risen to Dudley’s bait, but Dudley had said the very thing
	Harry had been thinking himself . . . maybe he didn’t have any friends at Hogwarts. . . . 
	Wish they could see famous Harry Potter now, he thought savagely as he spread manure on the flower beds,
	his back aching, sweat running down his face. It was half past seven in the evening when at last, exhausted,
	he heard Aunt Petunia calling him. “Get in here! And walk on the newspaper!” Harry moved gladly
	into the shade of the gleaming kitchen. On top of the fridge stood tonight’s pudding: a huge mound of 
	whipped cream and sugared violets. A loin of roast pork was sizzling in the oven. “Eat quickly!
	The Masons will be here soon!” snapped Aunt Petunia, pointing to two slices of bread and a lump
	of cheese on the kitchen table. She was already wearing a salmon-pink cocktail dress. Harry 
	washed his hands and bolted down his pitiful supper. The moment he had finished, Aunt Petunia
	whisked away his plate. “Upstairs! Hurry!” 

	As he passed the door to the living room, Harry caught a glimpse of Uncle Vernon and Dudley in bow ties
	and dinner jackets. He had only just reached the upstairs landing when the doorbell rang and 
	Uncle Vernon’s furious face appeared at the foot of the stairs. “Remember, boy — one sound —” 
	Harry crossed to his bedroom on tiptoe, slipped inside, closed the door, and turned to collapse on his bed.
	The trouble was, there was already someone sitting on it.''')


	book.generate_pdf('./static/watermark/HarryPBase',clean_tex=False) #clean_tex=False src="/static/img/hp.jpg"
	tex=book.dumps() # The document as a string in LaTeX syntax
	book.generate_tex()
	

	# This combines the background PDF with the wording (base) PDF 
	input_pdf='./static/watermark/HarryPBase.pdf'
	output_pdf='./LaTeXFiles/HarryPotterDEMO.pdf'
	watermark_pdf='./static/watermark/HarryPBG.pdf'

	watermark = PdfFileReader(watermark_pdf)
	watermark_page = watermark.getPage(0)
	pdf = PdfFileReader(input_pdf)
	pdf_writer = PdfFileWriter()
		
	for page in range(pdf.getNumPages()):
		pdf_page = pdf.getPage(page)
		pdf_page.mergePage(watermark_page)
		pdf_writer.addPage(pdf_page)

	with open(output_pdf, 'wb') as fh:
		pdf_writer.write(fh)
	return render_template('KWLibrary.html')