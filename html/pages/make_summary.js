const http = new XMLHttpRequest();

//http.open("GET", "http://localhost/pages/summary_data.php")
http.open("GET", "summary_data.php");
http.send();

http.onreadystatechange = (e) => {

	let data = JSON.parse(http.responseText);
	let summarySection = document.getElementById("route-summary-section");
	let uList = document.createElement("ul");
	summarySection.innerHTML = "";
	summarySection.appendChild(uList);
	
	for (key in data) {
		let item = document.createElement("li"); 
		item.innerHTML = key + ": " + data[key];
		console.log(item.innerHTML);
		uList.appendChild(item);
	}
}