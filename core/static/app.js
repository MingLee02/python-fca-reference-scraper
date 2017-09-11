$(document).ready(function() {
    $("#post-reference").submit(function ( event ) {
        event.preventDefault();
        $.ajax({
            url: $(this).attr('url'),
            type: 'post',
            data: $(this).serialize(),
            success: function(data) {
                console.log(data)
                $('#content').append(
                    "<table>" +
                    "<tr><th>Company</th><th>address</th><th>email</th><th>phone</th><th>website</th></tr>"
                );
                for(var i = 0; i < data.length; i++) {
                    $('#content').append(
                        "<tr><td>" + 
                        data[i].fields.name + "</td><td>" + 
                        data[i].fields.address.replace(/[\[\]']+/g,'')  + "</td><td>" + 
                        data[i].fields.email + "</td><td>" +
                        data[i].fields.phone + "</td><td>" +
                        data[i].fields.website + "</td></tr>" 
                    );
                }
                $('#content').append(
                    "</table>"
                );
            }
        });
    });
});