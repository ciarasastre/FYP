from flask import Flask, render_template, request,jsonify
from pylatex import Document, Section, Subsection, Command, Figure
from pylatex.utils import italic, NoEscape
import os
import json
import pprint

app = Flask(__name__)

@app.route("/test")
def test():
	# Opening JSON file FOR HTML EDITING
	return render_template("book.json")
	#return render_template("test.html");

#Connect to the Site Here:
@app.route("/")
def hello():
	return render_template("userPage.html")

@app.route("/home")
def home():
	return render_template("userPage.html")

@app.route("/edit")
def edit():
	return render_template("bookEdit.html");

@app.route("/done", methods=["GET","POST"])
def done():
	newText = request.form["new_text"]
	#return(newText)

	#Open json file & edit text
	with open('./templates/book.json', 'r') as editBook:
		data = json.load(editBook)

	temp = data["text"]
	data["text"] = newText

	with open('./templates/book.json', 'w') as editBook:
		json.dump(data, editBook)
	return render_template("userPage.html")

#Getting title name back from HTML
@app.route("/book", methods=["GET","POST"])
def book():

	# Build JSON Object from form in HTML
	title_name = request.form["title_name"] #Get HTML put into new var title_name
	author_name = request.form["author_name"]
	chapter_number = request.form["chapter_number"]
	text = request.form["text"]

	Book = jsonify({"bookTitle" : title_name,
	"bookAuthor" : author_name,
	"bookChapter" : chapter_number,
	"Text" : text }) 

	#Creates .json file in json folder
	#Uses titlename as JSON File name
	with open('./templates/book.json', 'w') as Book: #open('./json/'+ title_name + '.json', 'w')
		json.dump(request.form, Book)
	return render_template('bookEdit.html')

@app.route("/latex", methods=["GET","POST"])
def latex():
	
	#Open json file & edit text
	with open('./templates/book.json', 'r') as PDFBook:
		data = json.load(PDFBook)

		#Start pulling data from JSON file
		title_name = data["title_name"]
		author_name = data["author_name"]
		chapter_num = data["chapter_number"]
		book_text = data["text"]

	book = Document()

	#Images and relative paths
	scriptDir = os.path.dirname(__file__)
	imageCoverPath = "harryPotter.jpg"
	imageBabyPath = "baby.jpg"
	image_covername = os.path.join(scriptDir, imageCoverPath)
	image_baby = os.path.join(scriptDir, imageBabyPath)

	#Cover Image
	with book.create(Figure(position='h!')) as coverImage:
		coverImage.add_image(image_covername, width='300px') 
	book.preamble.append(Command('title', title_name)) # Would need users input here
	book.preamble.append(Command('author', author_name)) # Would need users name
	book.preamble.append(Command('date', NoEscape(r'\today'))) 
	book.append(NoEscape(r'\maketitle')) #maketitle is an actual command

	# fill_document(book)
	#book.append(chapter_num + '\n')

	# Add image of baby
	with book.create(Figure(position='h!')) as image:
		image.add_image(image_baby, width='200px') 
	book.append(book_text)

	book.generate_pdf('./LaTeXFiles/' +title_name+ 'LaTeX', clean_tex=False)
	tex=book.dumps() # The document as a string in LaTeX syntax
	#book.generate_tex() 
	return "Your Book is called %s" %(title_name)

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