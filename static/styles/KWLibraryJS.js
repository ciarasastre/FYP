var auth = "yes";
var title = "yes";

function applyLibrary()
{
	console.log("PAGE LOADED");
	// Pass the unique code here to access the unique json file
    var requestURL = 'http://127.0.0.1:5000/displayLibrary';
    var request = new XMLHttpRequest();
    request.open('GET', requestURL);
    request.responseType = 'text';
    request.send();

    request.onload = function() 
    {
    	var booksResponse = request.response;
	    var bookLib = JSON.parse(booksResponse);
	    
	    //Get all required data
	    getBooks = bookLib.books; //Gets all book objects .books
	    console.log("Get books is"+ getBooks);

	    const addBooks = document.querySelector('#addBooks');

		for(j in getBooks)
	    {
	    	// EG 0 OBJECT
	    	info = getBooks[j];
	    	console.log(j + " - " + (getBooks[j]) );

	    	//Create the card that the info will be in
	    	const contentDiv = document.createElement('div');
	    	contentDiv.classList.add('w3-third');
	    	contentDiv.classList.add('w3-margin-bottom');
	    	addBooks.appendChild(contentDiv);

			// Create the image
	    	const img = document.createElement('img');
	    	img.src = '/static/img/wtpcover2.jpg';
	    	img.style.width = '50%';
	    	img.classList.add('w3-hover-opacity');
	    	img.onclick = (event) => {
	    		document.getElementById('CABPopup').style.display = 'block';
	    	};
	    	contentDiv.appendChild(img);
	    	
	    	//Add the title
	    	const containerDiv = document.createElement('div');
	    	containerDiv.classList.add('w3-container');
	    	containerDiv.classList.add('w3-white');
	    	containerDiv.style.width = '50%';

	    	contentDiv.appendChild(containerDiv);

	    	for(i in info)
		    {
		    	// EG BOOK 1
		    	console.log(i + " - " + (info[i]) );

		    	book = info[i];

		    	for(k in book)
		    	{
		    		// EG AUTH, TITLE NAME
	  				if(k == "auth")
  					{
		  				auth = book[k];
		  				console.log("auth is " + auth);
	  				}

  					//Get only the title
  					if(k == "title_n")
  					{
  						title = book[k];			
				    	img.name = "bookName";
				    	img.value = (book[k]);
  						console.log("title is " + title);
	  				}
	  			}
		    }

		    containerDiv.innerHTML = '<p><b>'+ title +' </b></p>';
		    containerDiv.innerHTML += '<p class="w3-opacity">' + auth + '</p>';
	    }
    }
}
