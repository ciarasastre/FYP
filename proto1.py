from flask import Flask, render_template, request,jsonify, Response
from pylatex import Document, Section, Subsection, Command, Figure, Package
from pylatex.utils import bold, italic, NoEscape
import os
import json
import pprint
import re

app = Flask(__name__)

@app.route("/test")
def test():
	# Opening JSON file FOR HTML EDITING
	return render_template("book.json")
	#return render_template("test.html");

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

@app.route("/done", methods=["GET","POST"])
def done():

	#PageNav is a string at this point
	newText = request.form["new_text"]
	pageNav = request.form["pageNav"]

	#Open json file & edit text
	with open('./templates/json/book.json', 'r') as editBook:
		data = json.load(editBook)
	#temp = data["chapters"]["ch1"]["text"]
	#data["chapters"]["ch1"]["text"] = newText

	#attempt to create a page 3 blank here
	#data["name"] = "Lion" 
	data["chapters"]["ch1"]["p" + pageNav] = newText #str(pageNum) + str(pageNav)


	newPageNav = (int(pageNav) + 1) # converts to int to make it one value higher

	# Store page nav as a higher (next page instance)
	temp2 = data["pageNav"]
	data["pageNav"] = newPageNav

	with open('./templates/json/book.json', 'w') as editBook:
		json.dump(data, editBook)
	return render_template("KWProfile.html")

#Getting title name back from HTML
@app.route("/book", methods=["GET","POST"])
def book():

	# Build JSON Object from form in HTML
	title_name = request.form["title_name"] #Get HTML put into new var title_name
	author_name = request.form["author_name"]
	#chapter_number = request.form["chapter_number"]

	#text = request.form["text"] # All text gets put in through here

	# Create new format for JSON Here
	newBook = {
		"title_name" : title_name,
		"author_name" : author_name,
		#"chapter_number" : chapter_number,
		"pageNav" : 1,
		"chapters": 
			{
				"ch1" :{
						#"text" : "",
						},
			},
		}

	#Creates .json file in json folder
	#Uses titlename as JSON File name
	with open('./templates/json/book.json', 'w') as Book: #open('./json/'+ title_name + '.json', 'w')
		json.dump(newBook,Book)
	return render_template('KWEditor.html')

@app.route("/latex") #, methods=["GET","POST"]
def latex():

	# VARIABLES
	boldswitch = 0
	italicswitch = 0
	normalswitch = 1

	#FONT
	impactFont = '<span style=\"font-family: Impact,Charcoal,sans-serif;\">'

	#Open json file & edit text
	with open('./templates/json/book.json', 'r') as PDFBook:
		data = json.load(PDFBook)

		#Start pulling data from JSON file
		title_name = data["title_name"]
		author_name = data["author_name"]
		#chapter_num = data["chapter_number"]
		book_text = data["chapters"]["ch1"]["p1"]

	book = Document(fontenc = 'T1')

	#Images and relative paths
	scriptDir = os.path.dirname(__file__)
	imageCoverPath = "harryPotter.jpg"
	imageBabyPath = "baby.jpg"
	image_covername = os.path.join(scriptDir, imageCoverPath)
	image_baby = os.path.join(scriptDir, imageBabyPath)

	#Cover Image
	#with book.create(Figure(position='h!')) as coverImage:
	#	coverImage.add_image(image_covername, width='300px') 
	book.preamble.append(Command('title', title_name)) # Would need users input here
	book.preamble.append(Command('author', author_name)) # Would need users name
	book.preamble.append(Command('date', NoEscape(r'\today'))) 
	book.append(NoEscape(r'\maketitle')) #maketitle is an actual command

	# fill_document(book)
	#book.append(chapter_num + '\n')

	# Add image of baby
	#with book.create(Figure(position='h!')) as image:
	#	image.add_image(image_baby, width='200px') 
	

	###############################   RULES START HERE ########################################
	### FONT ###
	##### TEST FOR CUSTOM / PRETTY FONTS ############
	#book.packages.append(Package('ascii')) #asciifamily
	#book.append(NoEscape(r'\asciifamily')) 

	# IMPACT cyklop
	#book.packages.append(Package('cyklop')) #asciifamily
	#book.append(NoEscape(r'\normalfont')) 

	# GEORGIA
	# VERDANA
	# TAHOMA

	## REMOVAL RULES BEFORE SPLITTING

	####RULE FOR PARAGRAPH
	book_text = book_text.replace("<p>", "") # remove <p>
	book_text = book_text.replace("</p>", "\n") # at the end return

	#Dont need </span> tag
	book_text = book_text.replace("</span", "")

	###RULE FOR FIXING SPACE BUG THIS GOES AT THE END
	book_text = book_text.replace("<", " <") # place spaces so tags can be read
	book_text = book_text.replace(">", "> ") 

	
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

		#Run font function
		normalswitch = fontRule(book, word, normalswitch)

		#IF normal switch is on continue printing words
		if normalswitch == 1:
			book.append(word + ' ')#print the word and a space word +

	# Iterating words is over <-- Here

	# Generate PDF
	book.generate_pdf('./LaTeXFiles/' +title_name+'LaTeX', clean_tex=False)
	tex=book.dumps() # The document as a string in LaTeX syntax
	book.generate_tex() 
	return "Your Book is called %s" %(title_name)

############# RULES #################
def fontRule(book, word, normalswitch):
	# IMPACT
	if word == 'Impact,Charcoal,sans-serif;\">':
		book.packages.append(Package('cyklop')) #asciifamily
		book.append(NoEscape(r'\normalfont'))
		normalswitch = 1

	# ARIAL
	if word == 'Arial,Helvetica,sans-serif;\">':
		book.append(NoEscape(r'\sffamily')) #Sansserrif
		normalswitch = 1

	# TIMES NEW ROMAN
	if word == 'Roman,Times,serif,-webkit-standard;\">':
		book.append(NoEscape(r'\rmfamily'))
		normalswitch = 1

	return(normalswitch)

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

@app.route("/HPDemo")
def testing():
	# Basic Book Creation with title, author
	book = Document()
	title_name = "Testing"
	book.preamble.append(Command('title', "title_name")) # Would need users input here
	book.preamble.append(Command('author', "author_name")) # Would need users name
	book.append(NoEscape(r'\maketitle')) #maketitle is an actual command

	#Attempting to apply italics
	book.append("Applying")
	italicFound = italics(book)
	book.append("is really hard...")

	#Attempting to apply Bold
	book.append("\n" + "Applying")
	boldFound = bolds(book)
	book.append("was not workin for me...")

	#Attempting to apply Underline
	#book.append(LineBreak())
	book.append("\n" + "Applying")
	underLinesFound = underlines(book)
	book.append("was the worst of all")

	book.generate_pdf('./LaTeXFiles/' +title_name+'LaTeX', clean_tex=False)
	tex=book.dumps() # The document as a string in LaTeX syntax
	book.generate_tex() 
	return "Your Book is created hopefully %s" %(title_name)

#YOU CAN PASS BOOK WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
def italics(book):
	book.append(italic(' italics '))
	return()

def bolds(book):
	book.append(bold(" bold "))
	return()

def underlines(book):
	#book.append(verbatim("underline")) #\\underline{content_separator}")
	#book.append("underline{escape} ")
	#book.append(underline(" underline "))
	verbatim = ("Setting \\underline{escape} to \\underline{False}")
	book.append(verbatim)
	return()

	#LaTex Time

	# Basic Book Creation with title, author
	#book = Document()

	#book.preamble.append(Command('title', title_name)) # Would need users input here
	#book.preamble.append(Command('author', author_name)) # Would need users name
	#book.append(NoEscape(r'\maketitle')) #maketitle is an actual command

	#fill_document(book)

	#book.generate_pdf('LaTeXUserBook', clean_tex=False)
	#tex=book.dumps() # The document as a string in LaTeX syntax
	#book.generate_tex() 
	#return Book
	#return "Your Book is called %s" %(title_name)

#Connect to JSON to view our JSON object
#@app.route("/titleJSON", methods=['GET','POST'])
#def titleJSON():

	#reading json
	#title_value = request.json["bookTitle"] # gets json object sent
	#return title_value

	#Writing JSON
	#result = "result"
	#return jsonify({"key" : result})

#Actual LaTex Generated Related Code Here
#from pylatex import Document, Section, Subsection, Command
#from pylatex.utils import italic, NoEscape


#if __name__ == '__main__':
    # Basic Book Creation with title, author, text
    #book = Document()
    
    #book.preamble.append(Command('title', 'Chapter One')) # Would need users input here
    #book.preamble.append(Command('author', 'Jane Doe')) # Would need users name
    #book.preamble.append(Command('date', NoEscape(r'\today'))) 
    #book.append(NoEscape(r'\maketitle')) #maketitle is an actual command
    
   # fill_document(book)
    
    #book.append('Words go here to write a book')
    #book.append('\nDoes this leave spaces?') #\n still leaves indents
    
    #book.generate_pdf('LaTeXProto', clean_tex=False)
    #tex=book.dumps() # The document as a string in LaTeX syntax
    #book.generate_tex() 


	#image_image1 = os.path.join(os.path.dirname(__file__), 'baby.jpg')

	#with book.create(Figure(position='h!')) as image:
	#	image.add_image(image_image1, width='100px') #width='400px'