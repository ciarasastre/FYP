function applyEdit()
{
	console.log("PAGE LOADED");
	// Pass the unique code here to access the unique json file
    var requestURL = 'http://127.0.0.1:5000/displayEdit';
    var request = new XMLHttpRequest();
    request.open('GET', requestURL);
    request.responseType = 'text';
    request.send();

    request.onload = function() 
    {
    	var booksResponse = request.response;
	    var bookEdit = JSON.parse(booksResponse);
	    
	    //Get all required data
	    getBooks = bookEdit.books; //Gets all book objects .books
	    console.log("Get books is"+ getBooks);

		for(j in getBooks)
	    {
	    	// EG 0 OBJECT
	    	info = getBooks[j];
	    	/*info = getBooks[j];
	    	console.log(j + " - " + (getBooks[j]) );

	    	//Create the card that the info will be in*/
	    	var newDiv = document.createElement("DIV");
			newDiv.setAttribute("id", "Div"+[j]);
			newDiv.setAttribute("class", "cards");
			document.getElementById("create").appendChild(newDiv); //Append it to the main html

	    	for(i in info)
		    {
		    	// EG BOOK 1
		    	console.log(i + " - " + (info[i]) );

		    	book = info[i];

		    	for(k in book)
		    	{
		    		// EG AUTH, TITLE NAME
		    		//Create the title and the author name
			    	var newWord = document.createElement("P");
					newWord.innerHTML = (book[k]);

	  				document.getElementById("Div"+[j]).appendChild(newWord); //place them in the prev d

  					//Get only the title
  					if(k == "title_n")
  					{
	  					//Create an EDIT button for this card with the title value ####################################### <- EDIT

	  					//<input type="Submit" name="form" value= CREATE/>
					    newEditBtn = document.createElement("BUTTON");

						newEditBtn.innerHTML = "EDIT "+ (book[k]);
						newEditBtn.name = "newTitle";
						newEditBtn.type = "Submit"
						newEditBtn.value = (book[k]);

						//newEditBtn.href = "/editor";
						//newEditBtn.href = "somelink url"
						document.getElementById("Div"+[j]).appendChild(newEditBtn); //place them in the prev div

						newDeleteBtn = document.createElement("BUTTON");
						newDeleteBtn.innerHTML = "DELETE "+ (book[k]);
						newDeleteBtn.name = "newTitle";
						newDeleteBtn.type = "Submit"
						newDeleteBtn.value = (book[k]);
						//newDeleteBtn.onclick = function() {deleteButton()};
						document.getElementById("delete").appendChild(newDeleteBtn); //place them in the prev div


						//THE LIBRARY BUTTON
						moveBtn = document.createElement("BUTTON");
						//moveBtn.onclick = function() {addValue()};
						moveBtn.innerHTML = "FINISH BOOK "+ (book[k]);
						moveBtn.name = "libTitle";
						moveBtn.type = "Submit"
						moveBtn.value = (book[k]);
						//console.log(book[k]);

						document.getElementById("lib").appendChild(moveBtn); //place them in the prev di
	  				}
	  			}
		    }  
	    }
    }
}

function CustomFill()
{
	document.getElementById('CustomT').style.display='block';
	
}

function addValue()
{
	//moveBtn.value = "true";
}

/*function deleteButton()
{
	//This function will delete the json book object
	// Request http GET
    var requestURL = 'http://127.0.0.1:5000/displayEdit';
    var request = new XMLHttpRequest();
    request.open('GET', requestURL);
    request.responseType = 'text';
    request.send();

    request.onload = function() 
    {
    	var booksResponse = request.response;
	    var bookDelete = JSON.parse(booksResponse);
	    
	    //Get all required data
	    getDelete = bookDelete.books; //Gets all book objects .books
	    console.log("Get Delete is"+ getDelete);

		for(a in getDelete)
	    {
	    	// EG 0 OBJECT
	    	content = getDelete[a];

	    	for(b in content)
		    {
		    	// EG BOOK 1
		    	console.log(b  + " is in b");

		    	if(b == "test")
		    	{
		    		// If you found the correct title delete it
		    		console.log("Found Test");

		    	}
		    }  
	    }

    }
}*/
