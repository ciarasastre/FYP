from flask import Flask, render_template, request,jsonify
from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape
import json

app = Flask(__name__)

#Connect to the Site Here:
@app.route("/home")
def home():
	return render_template("webpageproto1.html")

#Getting title name back from HTML
@app.route("/book", methods=["GET","POST"])
def book():

	# Build JSON Object from form in HTML
	title_name = request.form["title_name"] #Get HTML put into new var title_name
	author_name = request.form["author_name"]

	Book = jsonify({"bookTitle" : title_name, "bookAuthor" : author_name}) #author_name

	with open('file.json', 'w') as Book:
		json.dump(request.form, Book)
	return render_template('webpageproto1.html')

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
