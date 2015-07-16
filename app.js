var access_token = 'b0y7fYe4mEiskcVybKylkw';
var merchantId = 'B7V6TAY54H5ZB';
var orderId = 0;
var xhr;
var ref = new Firebase("https://on-the-line.firebaseio.com/sqare");
var orderRef = new Firebase("https://on-the-line.firebaseio.com/order")
var newItems = false;
var queue = document.getElementById('queue');
var first1 = true;
var first2 = true;
var i=0;
var orders=[];

function order(information, items) {
	this.url = information.ref().toString();
	this.items = items;
}

if (window.XMLHttpRequest) {
    xhr = new XMLHttpRequest();
} else if (window.ActiveXObject) {
    xhr = new ActiveXObject("Microsoft.XMLHTTP");
}

xhr.onreadystatechange = function() {
	if (xhr.readyState === 4) {
		if (xhr.status === 200) {
			var response = JSON.parse(xhr.responseText);
			console.log(response);
			var itemization = response.itemizations;
			var itemList = [];
			for (var j in itemization) {
				if (itemization[j].notes) {
					itemList.push("<span class='num'>" + parseInt(itemization[j].quantity) + "</span> - " + itemization[j].name + "<div class='notes'>" + itemization[j].notes + "</div>");
				} else {
					itemList.push("<span class='num'>" + parseInt(itemization[j].quantity) + "</span> - " + itemization[j].name);
				}
			}
			orderRef.push(itemList);
		}
	} else {
		console.log('Loading');
	}	
}

ref.limitToLast(1).on('child_added', function(snapshot) {
	if (first1) {
		first1 = false;
	} else {
		var paymentInformation = snapshot.val();
		var paymentId = paymentInformation.entity_id;

		xhr.open("GET", 'https://connect.squareup.com/v1/'+merchantId+'/payments/'+paymentId);
		xhr.setRequestHeader('Authorization', 'Bearer '+ access_token);
		xhr.setRequestHeader('Accept', 'application/json');
		xhr.setRequestHeader('Content-Type', 'application/json');
		xhr.send();
	}
});

orderRef.on('child_added', function(snapshot) {
		var orderInformation = snapshot.val();
		var orderList = "";
		var notes = "";
		for (var j = 0; j < orderInformation.length; j++) {
			orderList += '<div class="food">' + orderInformation[j] + '</div>';
		}
		orders[i] = {
			key: snapshot.key(),
			items: orderList
		};
		queue.innerHTML += '<div class="box" id="' + i + '">' + orders[i].items + '</div>';
		i++;
});

$(document).on('click','.box',function()
{
    this.remove();
    var j = $(this).attr('id');
    var boxRef = new Firebase ("https://on-the-line.firebaseio.com/order/"+orders[j].key);
    boxRef.remove();
});
