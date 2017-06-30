import mailchimp
from django.conf import settings

def subscribe_email(email):
    
    api = mailchimp.Mailchimp(settings.MAILCHIMP_API_KEY)
    api.lists.subscribe(settings.MAILCHIMP_SUBSCRIBE_LIST_ID, {'email': email})
