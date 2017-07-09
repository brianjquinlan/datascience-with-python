from django.conf import settings
from mailchimp3 import MailChimp

from requests.exceptions import HTTPError

# mailchimp v3
def subscribe_email(email):

    client = MailChimp('brianjquinlan8', settings.MAILCHIMP_API_KEY)
    
    try:
        client.lists.members.create(settings.MAILCHIMP_SUBSCRIBE_LIST_ID,
            {'email_address': email, 'status':'pending'})

        return 200

    except HTTPError as e:
        # 400 error
        print(e)
        code = e.response.status_code
        if code == 400:
            return code

def unsubscribe_email(email):
	pass
