var completed = new Firebase("https://on-the-line.firebaseio.com/completed");
var completedQueue = document.getElementById('completedQueue');
var CompletedOrders = [];
var i = 0;

completed.on("child_added", function(snapshot) {
	var completedOrder = snapshot.val();
	var orderList = "";
	for (var j = 0; j < completedOrder.length; j++) {
		orderList += '<div class="food">' + completedOrder[j] + '</div>';
	}
	CompletedOrders[i] = {
		key: snapshot.key(),
		items: orderList
	};
	completedQueue.innerHTML += '<div class="completedBox" id="' + i + '">' + CompletedOrders[i].items + '</div>';
	i++;
});