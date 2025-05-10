# pip install whoisdomain

import whoisdomain as whois


def get_domain_info(domain_name):
    try:
        domain = whois.query(domain_name)
        print(domain.__dict__)
        print(f'Domain Name     : {domain.name}')
        print(f'Registrar        : {domain.registrar}')
        print(f'Creation Date   : {domain.creation_date}')
        print(f'Expiration Date : {domain.expiration_date}')
        print(f'Name Servers    : {', '.join(domain.name_servers)}')
    except Exception as e:
        print(f'Error fetching information: {e}')
        

if __name__ == '__main__':
    domain_name = input('Enter a domain name (Exp. example.com): ')
    get_domain_info(domain_name)