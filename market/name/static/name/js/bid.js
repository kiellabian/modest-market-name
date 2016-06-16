$(document).ready(function() {
    $('.btn-bid').on('click', bid);

    function bid() {
        var btn = $(this);
        var value = $('form input#name').val();
        console.log(value);

        $.ajax({
            type: 'POST',
            data: {
                value: value,
            },
            success: function(response) {
                var data = JSON.parse(response)
                $('form').next('div').remove();
                $('form').remove();
                $('.row div').append('<p>Thank you for bidding!</p>');
                $('.highest-bidder-name').text(data.new_bid.name);
                $('.highest-bid').text(data.new_bid.value);
                var li = $("<li>"+data.previous_bid.name+", $"+data.previous_bid.value+"</li>")
                $('.alert ul').prepend(li);
            },
            beforeSend: function(xhr, settings) {
                var csrftoken = Cookies.get('csrftoken');
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        });
    }

});