//Declare variables
var title = "";
var author = "";
var chapter = "";
var words = "";


function apply()
{
	// Pass the unique code here to access the unique json file
    var requestURL = 'http://127.0.0.1:5000/test';
    var request = new XMLHttpRequest();
    request.open('GET', requestURL);
    request.responseType = 'text';
    request.send();

    request.onload = function() 
    {
	    var booksText = request.response;
	    var books = JSON.parse(booksText);
	    //console.log("Books Text is : " + books.text);
	    
	    //Get all required data
	    title = books.title_name;
	    author = books.author_name;
	    chapter = books.chapter_number;
	    pageNav = books.pageNav;

	    p0 = books.chapters.ch1.text; //problem here with hardcoding

	    // This will need to store an array of pages to then iterate over when editing

	    fillData(title, author, chapter, p0, pageNav)
    }

}

function fillData(title, author, chapter, p1, pageNav)
{
	document.getElementById("info_title").innerHTML =  "Book Title : " + title; 
	document.getElementById("info_author").innerHTML =  "Book Author : " + author;
	document.getElementById("info_chpnum").innerHTML =  "Book Chapter number : " + chapter;
	document.getElementById("info_text").innerHTML =  p0;
	document.getElementById("info_pageNav").value =  pageNav;
}

function saveBook(pages)
{
	console.log("Saved!");

	console.log("Pages contains ")

	var pageContents = ["p0"];

	console.log(pageContents[0]);

	// pages[1] for example would be
	// pages[1] = books.chapters.ch1.p1;

	//Save updated works that were written
	//var textArea = document.getElementById('info_text');
	//var newWords = textArea.value;
	//console.log("New Words are " + newWords);
	//document.getElementById("newWords").innerHTML =  newWords;
}

//Goes to the next page of the book
function nextPage()
{

	//You need to save P1 and move onto P2
	document.getElementById("info_text").innerHTML =  p0;
	
}

//Goes to the previous page of the book
function prevPage()
{
	//The text are needs to change from P1(text) to P2
	document.getElementById("info_text").innerHTML =  p0;

	//You need to save P1 and move onto P2
}

function bold() 
{
	//document.getElementsByTagName("input").style.fontWeight = 'bold';
	//console.log("Bold Works");
    //document.getElementById("info_text").style.fontWeight = 'bold'; 

    //If its already bold put it back to normal

	if(document.getElementById("info_text").style.fontWeight == 'bold')
	{
		document.getElementById("info_text").style.fontWeight = "normal";
	}
	else
	{
		document.getElementById("info_text").style.fontWeight = 'bold';
	}
}

function italic() 
{
	//If its already italics put it back to normal
	if(document.getElementById("info_text").style.fontStyle == "italic")
	{
		document.getElementById("info_text").style.fontStyle = "normal";
	}
	else
	{
		document.getElementById("info_text").style.fontStyle = "italic";
	}
}