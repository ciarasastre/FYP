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
	    

	    document.getElementById("info_title").innerHTML =  "Book Title : " + books.title_name; 
	    document.getElementById("info_author").innerHTML =  "Book Author : " + books.author_name;
	    document.getElementById("info_chpnum").innerHTML =  "Book Chapter number : " + books.chapter_name;
	    document.getElementById("info_text").innerHTML =  books.text;
    }


	console.log("Button works");

}