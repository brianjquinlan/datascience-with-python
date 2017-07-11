// subscribe to mailchimp via ajax
$(document).ready(function(){
    
    $('#subscribe').submit(function(e) {
        e.preventDefault();
        var email_id = $('#email_id').val();

        if (email_id) {
            var csrfmiddlewaretoken = csrftoken;
            var email_data = {'email_id': email_id,
                'csrfmiddlewaretoken': csrfmiddlewaretoken };
            
            swal({
                title: "Are you sure?",
                text: "Confirm to Subscribe",
                type: "info",
                showCancelButton: true,
                closeOnConfirm: false,
                showLoaderOnConfirm: true,
            },
            function(){
		        $.ajax({
		            type: 'POST',
		            url: '/blog/subscribe/',
		            dataType: 'json',
		            data: email_data,
		            success: function(response) {
		                $('#email_id').val('');

		                if (response.status_code == '400') {
		                    sweetAlert("oops...", "This email may already be part of this list.  If this is not the case then please try again.", "error");

		                } else {
		                    swal("Thank you for subscribing" , "Check your email to confirm.", "success");
		                }
		            },
		            error: function(response) {
		                swal("Something went wrong. Please Try again.");
		                $('#email_id').val('');
		            }
		        });
            });

            return false;
        } else {
            sweetAlert('Error', 'Please provide correct email', "error");
        }
    });

});
