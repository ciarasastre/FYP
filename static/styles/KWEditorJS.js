//Declare variables
var title = "";
var author = "";
var chapter = "";
var words = "";
var thevalue = "";

function apply()
{
	/*console.log("works!");
	var image = document.getElementById('img');       // Image you want to save querySelector
	var saveImg = document.createElement('a');       // New link we use to save it with
	saveImg.href = "./static/img/mahog.jpg" //saveImg.href image.src                         // Assign image src to our link target
	saveImg.download = "./static/img/imagename.jpg";              // set filename for download
	saveImg.innerHTML = "Click to save image";       // Set link text
	document.body.appendChild(saveImg); */

	console.log("PAGE LOADED");
	// Pass the unique code here to access the unique json file
    var requestURL = 'http://127.0.0.1:5000/test';
    var request = new XMLHttpRequest();
    request.open('GET', requestURL);
    request.responseType = 'text';
    request.send();

    request.onload = function() 
    {
    	document.getElementById("area").value =  "main";
    	console.log(area.value);
    	var booksText = request.response;
	    var books = JSON.parse(booksText);
	    
	    //Get all required data
	    title = books.title_name;
	    author = books.author_name;
	    pages = books.chapters.ch1; 

	    //Get Buttons data
	    aknow = books.aknow;
	    toc = books.toc;
	    coverpage = books.coverpage;

	    //Pass variables through here
	    fillData(title, author, pages)
	    pdf(title)
	    loadContents(aknow, toc, coverpage)

	    // Set the froala editor
	    $(function() {$('textarea').froalaEditor('html.set', pages)});
    }

}

function fillData(title, author, pageNav, pages)
{
	document.getElementById("info_title").innerHTML =  "Book Title : " + title; 
	document.getElementById("info_author").innerHTML =  "Book Author : " + author;
}

function pdf(title)
{
	var path1 = "../static/styles/latex/";
  	var endpath = "LaTeX.pdf#toolbar=0&navpanes=0&scrollbar=0";
  	console.log("title is" + title);
  	var title_path = title;
  	var newSource = path1 + title_path + endpath;
    //var newSource = "../static/styles/latex/testLaTeX.pdf#toolbar=0&navpanes=0&scrollbar=0";

  	document.getElementById("pdfSource").src = newSource;

  	alert("Refresh the page to see your updated PDF!");

  	//setTimeout("location.reload(true);",2000); // Refresh the page after 2 seconds
}

function loadContents(aknow, toc, coverpage)
{
	//Adds main chapter 1 button
	var mainBtn = document.createElement("BUTTON");
	mainBtn.innerHTML = "Main Page";

	mainBtn.type="Submit";
	mainBtn.name="form";
	mainBtn.form = "updateForm"
	//Adding button click function
	mainBtn.onclick = function() {fillMain()};
  	document.getElementById("contents").appendChild(mainBtn); //place them in this area

	// Takes in TOC, AkNo, Coverpage and creates buttons for them
	//if its not empty create it
	if(aknow != "noAknow123")
	{
		console.log("Aknowledgements Created!");
		var aknowBtn = document.createElement("BUTTON");
		aknowBtn.innerHTML = "Acknowledgements";

		aknowBtn.type="Submit";
		aknowBtn.name="form";
		aknowBtn.form = "updateForm"

		//Adding button click function
		aknowBtn.onclick = function() {fillAknow()};
  		document.getElementById("contents").appendChild(aknowBtn); //place them in this area
	}
	else
	{
		console.log("No Aknowledgements Created");
	}

	if(toc != "noToc123")
	{
		console.log("Table of Contents Created!");
		var tocBtn = document.createElement("BUTTON");
		tocBtn.innerHTML = "Table of Contents";

		tocBtn.type="Submit";
		tocBtn.name="form";
		tocBtn.form = "updateForm"

		//Adding button click function
		tocBtn.onclick = function() {fillToc()};
  		document.getElementById("contents").appendChild(tocBtn); //place them in this area
	}
	else
	{
		console.log("No Table of Contents Created");
	}

	/*if(coverpage != "no")
	{
		console.log("Coverpage Created!");
		var coverBtn = document.createElement("BUTTON");
		coverBtn.innerHTML = "Cover Page";
		coverBtn.type="Submit";
		coverBtn.name="form";
		coverBtn.form = "updateForm"

		//Adding button click function
		coverBtn.onclick = function() {fillCp()};
  		document.getElementById("contents").appendChild(coverBtn); //place them in this area
	}*/

  	var path1 = "../static/styles/latex/";
  	var endpath = "LaTeX.pdf#toolbar=0&navpanes=0&scrollbar=0";
  	var newSource1 = path1 + title_name + endpath;
  	var newSource = "../static/styles/latex/testLaTeX.pdf#toolbar=0&navpanes=0&scrollbar=0";

  	document.getElementById("pdfSource").src = newSource

}

function refresh()
{
	console.log("refresh works");
	setTimeout("location.reload(true);",2000); // Refresh the page after 2 seconds
	//location.reload(true); This should reload the cache but is not doing so
}

var num = 1;
function createButton()
{
	num++;
	//Buttons are not stylaized YET
	console.log("Button Created!");
  	var btn = document.createElement("BUTTON");
  	btn.innerHTML = "Chapter " + num;

  	btn.name = "chapter";
	//btn.type = "Submit"
	btn.value = "num";

  	document.getElementById("chapters").appendChild(btn); //place them in this area
}

/*function fillCp()
{
	// Request http GET
    var requestURL = 'http://127.0.0.1:5000/test';
    var request = new XMLHttpRequest();
    request.open('GET', requestURL);
    request.responseType = 'text';
    request.send();

    request.onload = function() 
    {
    	document.getElementById("area").value =  "cp";
    	console.log(area.value);
    	// Load things here
	    var booksText = request.response;
	    var books = JSON.parse(booksText);

	    //Get Buttons data
	    newText = books.template.coverpage;

		// Set the froala editor
		$(function() {$('textarea').froalaEditor('html.set', newText)});
    }

    document.getElementById("currentPage").innerHTML =  "Current Page: Cover Page";

}*/

function fillAknow()
{
	// Request http GET
    var requestURL = 'http://127.0.0.1:5000/test';
    var request = new XMLHttpRequest();
    request.open('GET', requestURL);
    request.responseType = 'text';
    request.send();

    request.onload = function() 
    {
    	document.getElementById("area").value =  "aknow";
    	console.log(area.value);
    	// Load things here
	    var booksText = request.response;
	    var books = JSON.parse(booksText);

	    //Get Buttons data
	    newText = books.aknow;
	    oldText = books.chapters.ch1; //oldText is a temporary var with old data

		// Set the froala editor
		$(function() {$('textarea').froalaEditor('html.set', newText)});
    }

    document.getElementById("currentPage").innerHTML =  "Current Page: Aknowledgements Page";
}

function fillMain()
{
	// Request http GET
    var requestURL = 'http://127.0.0.1:5000/test';
    var request = new XMLHttpRequest();
    request.open('GET', requestURL);
    request.responseType = 'text';
    request.send();

    request.onload = function() 
    {
    	document.getElementById("area").value =  "main";
    	console.log(area.value);

	    var booksText = request.response;
	    var books = JSON.parse(booksText);

	    //Get Buttons data
	    oldAknow = books.aknow;
	    newText = books.chapters.ch1; //oldText is a temporary var with old data

		// Set the froala editor
		$(function() {$('textarea').froalaEditor('html.set', newText)});
    }

    document.getElementById("currentPage").innerHTML =  "Current Page: Main Page";

}

function fillToc()
{
	// Request http GET
    var requestURL = 'http://127.0.0.1:5000/test';
    var request = new XMLHttpRequest();
    request.open('GET', requestURL);
    request.responseType = 'text';
    request.send();

    request.onload = function() 
    {
    	document.getElementById("area").value =  "toc";
    	console.log(area.value);

	    var booksText = request.response;
	    var books = JSON.parse(booksText);

	    //Get Buttons data
	    oldAknow = books.aknow;
	    newText = books.toc;

		// Set the froala editor
		$(function() {$('textarea').froalaEditor('html.set', newText)});
    }

    document.getElementById("currentPage").innerHTML =  "Current Page: Table of Contents Page";

}

function saved()
{
	alert("Saved!");
}

