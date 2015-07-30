function reload() {
    $('#main').load('/orders #queue');
}
setInterval(reload,5000);

$('#main').on('dblclick','.box', function() {
    var pk = $(this).attr('id');
    var phone = $(this).attr('number');
    data1 = pk;
    $.post(location+'to_completed/', data1)
    $(this).remove();
    data2 = phone;
    $.post(location+'text/', data2)
});


