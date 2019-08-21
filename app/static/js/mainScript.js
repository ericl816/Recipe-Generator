var foodInputs = [""];
var foodNum = 2;

/*
	TODOS:
	-Hide and show buttons for each pair of searches
	-Navigation bar that follows user
*/

// Helper Functions
function setAttributes (element, attributes) {
	for (var i=0; i<Object.keys(attributes).length; i++) {
    element.setAttribute(String(Object.keys(attributes)[i]), String(Object.values(attributes)[i]))
  }
}


function search (event) {
  event.preventDefault();
  if (!validFoodInputs()) return;
}

function validFoodInputs(){
    /*
    -is input a food term
    -thinking about using a nn to validate input
    */

	for (var i=1; i<=foodNum; i++) {
		foodInputs[i]=document.getElementById("input_food"+String(i)).value.trim();
		if (!foodInputs[i].length>0 && !foodInputs[i].match(/^[a-zA-Z]+$/)) {
			document.getElementById("output_search").innerHTML="Please check your inputs";
			return false;
		}
	}
	document.getElementById("output_search").setAttribute("style","visibility:visible;");
	document.getElementById("output_search").innerHTML="Please wait...";
	return true;
}

function hideLoad() {
	document.getElementById("output_search").setAttribute("style","visibility:hidden;");
}

function addFood () {
	foodNum++;
	var listNode = document.createElement("li");
	listNode.setAttribute("id", "li_foodInput" + String(foodNum));
	var foodInput = document.createElement("INPUT");

	setAttributes(foodInput,{class:"input_food", type:"text", placeholder: "Ingredient " + String(foodNum), id:"input_food" + String(foodNum),name:"input_food" + String(foodNum), required: "required"});
	listNode.appendChild(foodInput);
	document.getElementById('button_removeFood').setAttribute("style", "visibility: visible;");
	listNode.appendChild(document.getElementById('button_removeFood'));
	document.getElementById('ul_foodInput').appendChild(listNode);
}

function removeFood () {
  var parent = document.getElementById("input_food" + String(foodNum)).parentNode;
  var grandParent = parent.parentNode;
	var button_removeFood = document.getElementById('button_removeFood');
	foodNum--;
	if (foodNum <= 2) {
		document.getElementById('button_removeFood').setAttribute("style", "visibility: hidden;");
		document.getElementById('form_foodInput').appendChild(button_removeFood);
	}
	else document.getElementById("li_foodInput" + String(foodNum)).appendChild(button_removeFood);
	grandParent.removeChild(parent);
}

function scrape () {

}
