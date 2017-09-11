$(document).ready(function() {
    $("#post-reference").submit(function ( event ) {
        event.preventDefault();
        $.ajax({
            url: $(this).attr('url'),
            type: 'post',
            data: $(this).serialize(),
            success: function(data) {
                console.log(data)
            }
        });
    });
});