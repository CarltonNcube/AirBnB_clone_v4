$(document).ready(function() {
    $.ajax({
        type: 'GET',
        url: 'http://54.173.251.99/api/v1/status/',
        success: function(data) {
            if (data.status === 'OK') {
                $('#api_status').addClass('available');
            } else {
                $('#api_status').removeClass('available');
            }
        },
        error: function() {
            console.log('Error fetching API status');
        }
    });
});
