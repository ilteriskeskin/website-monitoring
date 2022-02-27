import requests


def url_checker(url: str) -> str:
    """
    Check if a URL is valid.
    """
    try:
        r = requests.get(f'https://{url}')

        if r.status_code == 200:
            return f'{url} is valid.'

        return f'{url} is not valid.'
    except:
        return 'Invalid URL'


def check_http_to_https(url: str) -> str:
    """
    Check if a URL is valid.
    """
    try:
        r = requests.get(f'http://{url}')

        if 'https' in r.url:
            return 'Valid HTTPS URL'
        else:
            return 'Invalid HTTPS URL'
    except:
        return 'Invalid URL'


def check_redirect_www_subdomain(url: str) -> str:
    """
    Check if a URL is redirect www or non-www subdomain.
    """
    try:
        r = requests.get(f'http://{url}')

        if 'www' in r.url:
            return 'Redirect to www subdomain'

        return 'Redirect to non-www subdomain'
    except:
        return 'Invalid URL'
