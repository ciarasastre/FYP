from flask import Flask, render_template
app = Flask(__name__)

#Connect to the Site Here:
@app.route("/")
def home():
	return render_template("webpageproto1.html")


#Actual LaTex Generated Related Code Here
from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape


if __name__ == '__main__':
    # Basic Book Creation with title, author, text
    book = Document()
    
    book.preamble.append(Command('title', 'Chapter One')) # Would need users input here
    book.preamble.append(Command('author', 'Jane Doe')) # Would need users name
    book.preamble.append(Command('date', NoEscape(r'\today'))) 
    book.append(NoEscape(r'\maketitle')) #maketitle is an actual command
    
   # fill_document(book)
    
    book.append('Words go here to write a book')
    book.append('\nDoes this leave spaces?') #\n still leaves indents
    
    book.generate_pdf('LaTeXProto', clean_tex=False)
    #tex=book.dumps() # The document as a string in LaTeX syntax
    book.generate_tex() 
