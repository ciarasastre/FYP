function convert()
{
	console.log("func works");
	// Grab elements from textarea and Laytex area
	var textArea = document.getElementById('userInput');
	var latexArea = document.getElementById('userOutput');
	
	//Put text in a variable
	var text = textArea.value;
	latexArea.innerHTML = text;

	/*var dict = {"one" : [15, 4.5],
	"two" : [34, 3.3],
	"three" : [67, 5.0],
	"four" : [32, 4.1]};

	var dictstring = JSON.stringify(dict);
	var fs = require('fs');
	fs.writeFile("thing.json", dictstring);

	console.log(dictstring);*/
}

