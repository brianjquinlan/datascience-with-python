// subscribe to mailchimp via ajax
$(document).ready(function(){
    $('#subscribe').submit(function(e) {
        e.preventDefault();
        var email_id = $('#email_id').val();

        if (email_id) {
            var csrfmiddlewaretoken = csrftoken;
            var email_data = {'email_id': email_id,
                'csrfmiddlewaretoken': csrfmiddlewaretoken };
            
            $.ajax({
                type: 'POST',
                url: '/blog/subscribe/',
                dataType: 'json',
                data: email_data,
                success: function(response) {
                    $('#email_id').val('');

                    if (response.status_code == '400') {
                        alert("This email is already part of this list");

                    } else {
                        alert("Thank you for subscribing Check your email to confirm.");
                    }
                },
                error: function(response) {
                    alert("Something went wrong");
                    $('#email_id').val('');
                }
            });
            return false;
        } else {
            alert('Please provide correct email');
        }
    });

});
