import ipaddress
import math


def get_ip_from_raw_address(raw_address):
    '''
    str -> str
    Function gets ip address from raw ip address with prefix.
    >>> get_ip_from_raw_address('91.124.230.205/30')
    '91.124.230.205'
    >>> get_ip_from_raw_address('91.124.230.205/')

    '''
    try:
        if len(raw_address.split('/')) != 2 or raw_address.split('/')[1] == '':
            return None
        return raw_address.split('/')[0]
    except:
        return None


def get_network_address_from_raw_address(raw_address):
    """
    str -> str
    Function returns network ip address taken from the raw ip address.
    >>> get_network_address_from_raw_address('91.124.230.205/30')
    '91.124.230.204'
    >>> get_network_address_from_raw_address('91.124.230.205/')

    """
    try:
        bin_ip = \
            conv_to_bin(get_ip_from_raw_address(raw_address)).split('.')
        bin_mask = \
            conv_to_bin(get_mask_from_raw_address(raw_address)).split('.')
        answ = [str(int(bin_ip[x], 2) & int(bin_mask[x], 2)) for x in range(4)]
        return '.'.join(answ)
    except:
        return None


def get_binary_network_address_from_raw_address(raw_address):
    '''
    str -> str
    Function returns binary network ip address taken from raw ip address.
    >>> get_binary_network_address_from_raw_address('91.124.230.205/30')
    '01011011.01111100.11100110.11001100'
    >>> get_binary_network_address_from_raw_address('91.124.230.205')

    '''
    try:
        return conv_to_bin(get_network_address_from_raw_address(raw_address))
    except:
        return None


def get_mask_from_raw_address(raw_address):
    """
    str -> str
    Function returns the mask taken from the raw ip address.
    >>> get_mask_from_raw_address('91.124.230.205/30')
    '255.255.255.252'
    >>> get_mask_from_raw_address('91.124.230.205')

    """
    try:
        mask = [0, 0, 0, 0]
        for var in range(0, int(raw_address.split('/')[1])):
            mask[var // 8] += 1 << (7 - var % 8)

        return '.'.join([str(el) for el in mask])
    except:
        return None


def get_second_usable_ip_address_from_raw_address(raw_address):
    """
    str -> str
    Function returns second usable ip address taken from raw ip address.
    >>> get_second_usable_ip_address_from_raw_address('91.124.230.205/30')
    '91.124.230.206'
    >>> get_second_usable_ip_address_from_raw_address('91.124.230.205')

    """
    try:
        if len(raw_address.split('/')) != 2 or raw_address.split('/')[1] == '':
            return None
        ip_add = raw_address.split('/')[0]
        ips_number = get_total_number_of_ips_from_raw_address(raw_address)
        address_numb = int(ip_add.split('.')[3])
        network_id = math.floor(address_numb/ips_number)*ips_number
        return '.'.join(ip_add.split('.')[0:3] + [str(network_id + 2)])
    except:
        return None


def get_last_usable_ip_address_from_raw_address(raw_address):
    """
    str -> str
    Function returns last usable ip address taken from raw ip address.
    >>> get_last_usable_ip_address_from_raw_address('91.124.230.205/30')
    '91.124.230.206'
    >>> get_last_usable_ip_address_from_raw_address('91.124.230.205')
    """
    try:
        if len(raw_address.split('/')) != 2 or raw_address.split('/')[1] == '':
            return None
        ips_number = get_total_number_of_ips_from_raw_address(raw_address)
        ip_ad = raw_address.split('/')[0]
        network_id = math.floor(int(ip_ad.split('.')[3])/ips_number)*ips_number
        last_numb = str(network_id + ips_number - 2)
        return '.'.join(ip_ad.split('.')[0:3] + [last_numb])
    except:
        return None


def get_total_number_of_ips_from_raw_address(raw_address):
    """
    str -> int
    Function returns total number of ip addresses taken from raw ip address.
    >>> get_total_number_of_ips_from_raw_address('91.124.230.205/30')
    4
    >>> get_total_number_of_ips_from_raw_address('91.124.230.205')

    """
    try:
        if len(raw_address.split('/')) != 2 or raw_address.split('/')[1] == '':
            return None
        pref = raw_address.split('/')[1]
        if pref == '24':
            return 256
        if pref == '25':
            return 128
        if pref == '26':
            return 64
        if pref == '27':
            return 32
        if pref == '28':
            return 16
        if pref == '29':
            return 8
        if pref == '30':
            return 4
    except:
        return None


def get_number_of_usable_hosts(raw_address):
    """
    str -> int
    Function returns total number of usable hosts taken from raw ip address.
    >>> get_number_of_usable_hosts('192.168.20.166/25')
    126
    >>> get_number_of_usable_hosts('192.168.20.166')

    """
    try:
        if len(raw_address.split('/')) != 2 or raw_address.split('/')[1] == '':
            return None
        return get_total_number_of_ips_from_raw_address(raw_address) - 2
    except:
        return None


def get_ip_class_from_raw_address(raw_address):
    """
    str -> str
    Function returns class of ip address taken from raw ip address.
    >>> get_ip_class_from_raw_address('192.168.230.205/30')
    'C'
    >>> get_ip_class_from_raw_address('192.168.230.205')
    """
    try:
        if len(raw_address.split('/')) != 2 or raw_address.split('/')[1] == '':
            return None
        ip_add = raw_address.split('/')[0].split('.')[0]
        if 1 <= int(ip_add) <= 126:
            return 'A'
        if 128 <= int(ip_add) <= 191:
            return 'B'
        if 192 <= int(ip_add) <= 223:
            return 'C'
        if 224 <= int(ip_add) <= 239:
            return 'D'
        if 240 <= int(ip_add) <= 247:
            return 'E'
    except:
        return None


def get_ip_address_type_from_raw_address(raw_address):
    """
    str -> str
    Function returns type of ip address taken from raw address.
    >>> get_ip_address_type_from_raw_address('91.124.230.205/30')
    'Public'
    >>> get_ip_address_type_from_raw_address('91.124.230.205/')

    """
    try:
        if len(raw_address.split('/')) != 2 or raw_address.split('/')[1] == '':
            return None
        ip_add = raw_address.split('/')[0]
        var = ipaddress.IPv4Address(ip_add)
        if var.is_private:
            return 'Private'
        return 'Public'
    except:
        return None


def conv_to_bin(addrs):
    """
    str -> str
    Function returns ip address converted from decimal to binary.
    >>> conv_to_bin('255.255.255.252')
    '11111111.11111111.11111111.11111100'
    >>> conv_to_bin('255.255.255')

    """
    try:
        if len(addrs.split('.')) != 4 or '' in addrs.split('.'):
            return None
        return '.'.join(['0'*(8-len(str(bin(int(el)).replace('0b', '')))) +
            str(bin(int(el)).replace('0b', '')) for el in addrs.split('.')])
    except:
        return None


def convert_to_dec(addrs):
    """
    str -> str
    Function returns ip address converted from binary to decimal.
    >>> convert_to_dec('10101100.00010100.00000000.00000000')
    '172.20.0.0'
    >>> convert_to_dec('10101100.00010100.0000000')

    """
    try:
        if len(addrs.split('.')) != 4 or '' in addrs.split('.'):
            return None
        return '.'.join([str(int(el, 2)) for el in addrs.split('.')])
    except:
        return None


def main():
    """
    None -> str
    Main function of the module.
    """

    ip_add_mask = input().strip()
    try:
        ip_add = ip_add_mask.split('/')[0]
        ip_mask = ip_add_mask.split('/')[1]
    except:
        print('Error')
        return None

    if '/' not in ip_add_mask:
        print('Missing prefix')
        return None

    if not 24 <= int(ip_mask) <= 30:
        print('Error')
        return None

    if ip_mask == "":
        print('Missing prefix')
        return None
        if len(ip_add.split('.')) != 4:
            print('Error')
            return None
    try:
        for var in ip_add.split('.'):
            int(var)
            if len(var) > 3:
                print('Error')
                return None
    except:
        print('Error')
        return None
    print(get_ip_from_raw_address(ip_add_mask))
    print(get_network_address_from_raw_address(ip_add_mask))
    print(get_binary_network_address_from_raw_address(ip_add_mask))
    print(get_mask_from_raw_address(ip_add_mask))
    print(get_second_usable_ip_address_from_raw_address(ip_add_mask))
    print(get_last_usable_ip_address_from_raw_address(ip_add_mask))
    print(get_total_number_of_ips_from_raw_address(ip_add_mask))
    print(get_number_of_usable_hosts(ip_add_mask))
    print(get_ip_class_from_raw_address(ip_add_mask))
    print(get_ip_address_type_from_raw_address(ip_add_mask))


if __name__ == "__main__":
    main()

