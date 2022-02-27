from importlib import import_module
from utils.domain_name_expiration import get_domain_expiration
from utils.check_ssl_certificate import check_ssl_certificate
from utils.url_response_checker import url_checker, check_http_to_https, check_redirect_www_subdomain
from utils.sitemap.sitemap_main import healt_check


def main():
    while True:
        print("\
            0- Quit\n\
            1- Domain Name Expired\n\
            2- Domain Name SSL Certificate\n\
            3- URL Response Status\n\
            4- Check HTTP to HTTPS Redirect\n\
            5- Check Redirect www or non-www subdomain\n\
            6- Sitemap Health Check")
        choice = int(input("Enter your choice: "))

        if choice == 0:
            break
        elif choice == 1:
            domain_name = input("Enter domain name: ")
            print('****************')
            print(get_domain_expiration(domain_name))
            print('****************')
        elif choice == 2:
            domain_name = input("Enter domain name: ")
            print('****************')
            print(check_ssl_certificate(domain_name))
            print('****************')
        elif choice == 3:
            url = input("Enter URL: ")
            print('****************')
            print(url_checker(url))
            print('****************')
        elif choice == 4:
            url = input("Enter URL: ")
            print('****************')
            print(check_http_to_https(url))
            print('****************')
        elif choice == 5:
            url = input("Enter URL: ")
            print('****************')
            print(check_redirect_www_subdomain(url))
            print('****************')
        elif choice == 6:
            sitemap_url = input("Enter sitemap url: ")
            print('****************')
            print(healt_check(sitemap_url))
            print('****************')
        else:
            print("Invalid choice")


main()
