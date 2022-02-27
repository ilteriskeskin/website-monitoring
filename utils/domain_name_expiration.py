import whois

from datetime import datetime


def get_domain_expiration(domain_name: str) -> str:
    """
    Returns the expiration date of the domain.
    """
    try:
        now = datetime.now()
        whois_info = whois.whois(domain_name)
        exp_date = whois_info['expiration_date']

        if type(whois_info.expiration_date) == list:
            whois_info.expiration_date = whois_info.expiration_date[0]
        else:
            whois_info.expiration_date = whois_info.expiration_date

        timedelta = whois_info.expiration_date - now
        days_to_expire = timedelta.days

        return days_to_expire

    except:
        return 'No expiration date'
