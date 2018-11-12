function convert()
{
	console.log("func works");
	// Grab elements from textarea and Laytex area
	var textArea = document.getElementById('userInput');
	var latexArea = document.getElementById('userOutput');
	
	//Put text in a variable
	var text = textArea.value;
	latexArea.innerHTML = text;
}
