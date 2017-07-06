from django.conf import settings
from mailchimp3 import MailChimp

"""
mailchimp using v2
def subscribe_email(email):
    
    api = mailchimp.Mailchimp(settings.MAILCHIMP_API_KEY)
    api.lists.subscribe(settings.MAILCHIMP_SUBSCRIBE_LIST_ID, {'email': email})
"""

# mailchimp v3
def subscribe_email(email):
    client = MailChimp('brianjquinlan8', settings.MAILCHIMP_API_KEY)
    client.lists.members.create(settings.MAILCHIMP_SUBSCRIBE_LIST_ID,
        {'email_address': email, 'status':'pending'})

def unsubscribe_email(email):
	pass
