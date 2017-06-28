import mailchimp
import settings

def mailchimplist():
    
    api = mailchimp.Mailchimp(settings.MAILCHIMP_API_KEY)
    api.lists.subscribe(settings.MAILCHIMP_SUBSCRIBE_LIST_ID, {'email', 'test@email.com'})
