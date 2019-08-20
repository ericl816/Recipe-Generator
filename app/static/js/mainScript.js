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
	console.log("hello world");
  event.preventDefault();
  if (!validFoodInputs()) return;
	var resultsDiv = document.getElementById('div_results');
  while (resultsDiv.hasChildNodes()) resultsDiv.removeChild(resultsDiv.lastChild);
	//document.getElementById('button_search').setAttribute("style", "visibility:hidden;");
	for (var i=1; i<=foodNum; i++) {
		for (var j=i + 1; j<=foodNum; j++) {
      var newDiv = document.createElement("div");
      setAttributes(newDiv,{class:"col-sm-12",id: "div_result" + String(i) + '&' + String(j)});

			var newHeader = document.createElement("h3");
			newHeader.innerHTML = foodInputs[i] + '和' + foodInputs[j];

			// setCustomURL
			var myURL = 'https://zhidao.baidu.com/search?ct=17&pn=0&tn=ikaslist&rn=10&fr=wwwt&word=' + foodInputs[i] + '和' + foodInputs[j] + '可以一起吃吗？';
			var newIFrame = document.createElement("iframe");
			setAttributes(newIFrame,{onload:"hideLoad()",height:"40%",class:"col-sm-12",src:myURL,id:"frame_result" + String(i) + '&' + String(j)});


			newDiv.appendChild(newHeader);
			newDiv.appendChild(newIFrame);
			document.getElementById("div_results").appendChild(newDiv);
		}
	}
	//document.getElementById('button_search').setAttribute("style","visibility:visible;");
}

function validFoodInputs(){
    /*
    -is input a food term
    -thinking about using a nn to validate input
    */

	for (var i=1; i<=foodNum; i++) {
		foodInputs[i]=document.getElementById("input_food"+String(i)).value.trim();
		if (!foodInputs[i]>0){
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

	setAttributes(foodInput,{class:"input_food", type:"text", placeholder: "Item " + String(foodNum), id:"input_food" + String(foodNum), required: "required"});
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

function _scrape (output,foodA,foodB) {
	var myURL1 = 'https://zhidao.baidu.com/search?ct=17&pn=0&tn=ikaslist&rn=10&fr=wwwt&word=' + foodA + '和' + foodB +' 可以一起吃吗？';
	var dummyFrame = document.getElementById('dummyFrame');
	dummyFrame.setAttribute("src", myURL1);
	console.log(dummyFrame.contentWindow.document.innerHTML);
}

function scrape (output,foodA,foodB) {
	var myURL1 = 'https://zhidao.baidu.com/search?ct=17&pn=0&tn=ikaslist&rn=10&fr=wwwt&word=' + foodA +'和'+ foodB + ' 可以一起吃吗？';
	var proxy = 'https://cors-anywhere.herokuapp.com/';

	console.log('myURL1: '+ myURL1);
	// Execute 1st request
	var oReq1 = new XMLHttpRequest();
	oReq1.addEventListener("load", function () {
		var content = String(this.responseText);
		var x = content.indexOf('class="ti"');
		x = content.lastIndexOf('href="', x);
		x = content.indexOf('"',x);
		var y = content.indexOf('"', x + 1);
		var myURL2= content.slice(x + 1, y);
		console.log('myURL2: ' + myURL2);

		var oReq2 = new XMLHttpRequest();
		oReq2.addEventListener("load", function () {
			// var content = String(this.responseText);
			var dummyFrame = document.getElementById('dummyFrame');
			dummyFrame.contentWindow.document.write('hello');
		});
		oReq2.open("GET", proxy + myURL2);
		oReq2.send();
	});
	// Or post, etc
	oReq1.open("GET", proxy + myURL1);
	oReq1.send();
}

/*
function test () {

}
*/
