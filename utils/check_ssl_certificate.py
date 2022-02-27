import requests

def check_ssl_certificate(domain: str) -> str:
    try:
        requests.get(f'https://{domain}', verify=False)
        return 'Valid SSL certificate'
    except:
        return 'Invalid SSL certificate'