//Declare variables
var title = "";
var author = "";
var chapter = 0;
var words = "";

function apply()
{
    var requestURL = 'http://127.0.0.1:5000/test';
    var request = new XMLHttpRequest();
    request.open('GET', requestURL);
    request.responseType = 'text';
    request.send();

    request.onload = function() 
    {
	    var booksText = request.response;
	    var books = JSON.parse(booksText);
	    //console.log("Books Title name is : " + books.title_name);
	    //console.log("Books Author is : " + books.author_name);
	    //console.log("Books Chapter number is : " + books.chapter_number);
	    //console.log("Books Text is : " + books.text);
	    
	    //Get all required data
	    title = books.title_name;
	    author = books.author_name;
	    chapter = books.chapter_number;
	    words = books.text;

	    //Call function to fill data
	    fillData(title, author, chapter, words)
    }

}

function fillData(title, author, chapter, words)
{
	document.getElementById("info_title").innerHTML =  "Book Title : " + title; 
	document.getElementById("info_author").innerHTML =  "Book Author : " + author;
	document.getElementById("info_chpnum").innerHTML =  "Book Chapter number : " + chapter
	document.getElementById("info_text").innerHTML =  words;
}

function saveBook()
{
	console.log("Saved!");

	//Save updated works that were written
	var textArea = document.getElementById('info_text');
	var newWords = textArea.value;
	console.log("New Words are " + newWords);
	document.getElementById("newWords").innerHTML =  newWords;

}