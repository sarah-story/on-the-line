function reload() {
    $('#main').load('/orders/completed #completedQueue');
}
setInterval(reload,5000);