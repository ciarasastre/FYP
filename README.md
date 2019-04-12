# FYP
Fourth Year Project </br>

Title : TypeWriter </br>
Student number : C15355361 </br>
Student name : Ciara Sastre </br>
Supervisor : Paul Doyle </br>

**How To Run:** </br>
To run this application, Click the start.bat file to get the server running locally </br>
Then go onto http://127.0.0.1:5000/ to see the application. </br>

**Files:** </br>
There are Four Folders: </br>

-> JSON = Contains all JSON files created by my program </br>
-> Static/Styles = Contains all CSS and JS files I created </br>
-> Static/Styles/latex = Contains all LaTeX and PDF generated files </br>
-> Templates = Contains all HTML files I created </br>
-> LaTeXFiles = Contains all LaTeX and Tex Files generated from program. WARNING THESE ARE OLD AND UNUSED NOW </br>

The proto1.py is the main python file I developed that runs this program.



**Classes:** </br>

**Proto1.py**</br>
def done(): This class is run by the proto1.py python file. It manages book editing by opening a JSON file</br>
            Re-writing in it, and closing it. This saves the new JSON file and the users book is updated.</br>
            
def book(): This class is run by the proto1.py python file. It manages the create a book section of the program.</br>
            It will create a JSON file and store the users input in it.</br>
            
def latex(): This class is run by the proto1.py python file. It manages converting the JSON to LaTeX. It opens the JSON file</br>
            stores the information into variables. These variables are put through a series of LaTeX rules for example :</br>
            book.preamble.append(Command('title', title_name))</br>
            This takes the title name the user input, into the title of the LaTeX PDF book. As well as the images.</br>
            This code also generates a PDf and Tex file.</br>
	   
	    
@app.route("/")</br>
def hello(): This along with the other classes are just rendering the HTML templates. Using return render_template("webpageproto1.html")</br>
	
def test(): This is a test to open the JSON file and render it on a server so the front end can access it using XMLHTTP Requests.</br>	

**KWProfile.js**</br>
function apply(): This calls a XMLHTTP request to the JSON file that is run on def test() above. It parses this data and stores</br>
                  it in variables.</br>

function fillData(): This uses those variables to fill the HTML page with the data.</br>

function save(): This is activated when the user pushes th Save button. Any text that was modified in the text editor is now</br>
                  modified in the JSON file.</br>


**Scripts:** </br>
The Start Bat file is a batch file that quickly runs Flask. I also wrote this, it writes a series of commands in the commandline</br>
such as setting the environment and debug mode.</br>
