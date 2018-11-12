function apply()
{

	function loadJSON(path, success, error)
	{
	    var xhr = new XMLHttpRequest();
	    xhr.onreadystatechange = function()
	    {
	        if (xhr.readyState === XMLHttpRequest.DONE) {
	            if (xhr.status === 200) {
	                if (success)
	                    success(JSON.parse(xhr.responseText));
	            } else {
	                if (error)
	                    error(xhr);
	            }
	        }
	    };
	    xhr.open("GET", path, true);
	    xhr.send();
	}

	//http://127.0.0.1:5000/test
	loadJSON('http://127.0.0.1:5000/test', //'https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json'
         function(data) { console.log(data); },
         function(xhr) { console.error(xhr); }
	);

	console.log("Button works");

}