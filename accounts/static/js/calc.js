let counter = 0;
document.addEventListener('DOMContentLoaded', function(){
	document.querySelector('#bt').onmouseover = calc;
});

function calc(){
	//Handles number of calculator trials.
	counter++;
	document.querySelector("#counter").innerHTML = counter;
	if (counter % 10 === 0) {
		//alert("Counter is at "+counter);
			alert(`Counter is at ${counter}`)= counter;
	};

	//var type = document.getElementById("type").value;
	var price = document.getElementById("pages").value;

	var oper = document.getElementById("operators").value;
	if (oper === 'mla'){
		//document.getElementById("result").value = "$ "+parseInt(price)*650
		document.querySelector("h5").innerHTML = "$ "+parseInt(price)*650;
		document.querySelector("legend").innerHTML = "Total Cost";
	}
	if (oper === 'apa') {
		//document.getElementById("result").value = "$ "+parseInt(price)*600
			document.querySelector("h5").innerHTML = "$ "+parseInt(price)*600;
			document.querySelector("legend").innerHTML = "Total Cost";
	}

	if (oper === 'ch') {
		//document.getElementById("result").value = "$ "+parseInt(price)*700
		document.querySelector("h5").innerHTML = "$ "+parseInt(price)*700;
		document.querySelector("legend").innerHTML = "Total Cost";
	}
}