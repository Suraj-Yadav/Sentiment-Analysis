function extractData() {
	var reviews,count;
	if(localStorage.getItem("reviews"))
		reviews = localStorage.getItem("reviews");
	else
		reviews = "";

	if(localStorage.getItem("count"))
		count = Number(localStorage.getItem("count"));
	else
		count = 0;	

	temp = document.getElementsByClassName('review-text');
	for (var i = 0; i < temp.length; i++) {
		if((temp.item(i).innerHTML.length < 300) && (temp.item(i).innerHTML.length > 30)){	
			if(count===50)
			{
				console.log("50 reached");
				console.log(reviews);
				localStorage.removeItem("reviews");
				localStorage.removeItem("count");
				return 5;
			}	
			reviews = reviews + "\n[" + temp.item(i).innerHTML + "]" + '\n';
			count++;}
			
	}

	localStorage.setItem("reviews", reviews);
	localStorage.setItem("count", count);
	
	var link = document.getElementsByClassName("a-last");
	if (link[0].children[0].getAttribute("href") != null)
		window.location = link[0].children[0].getAttribute("href");
	else{
		console.log(reviews);
		localStorage.removeItem("reviews");
	}
}

var a = extractData();