import requests
import argparse
import json
import re

api_key = "your_api_key_here"

def banner():
    print("""                                 
     coded by : KamilDogo              
     Powered By CriminalIP
     https://www.criminalip.io/
    """)


def parse_arguments():
    parser = argparse.ArgumentParser(description="Tool to search domain/ip given an orgname")
    parser.add_argument("-i", "--ips", help="extract ips adresses", action='store_true')
    parser.add_argument("-o", "--orgname", help="organization name", type=str)
    parser.add_argument("-d", "--domains", help="extract subject's common name", action='store_true')
    parser.add_argument("-s", "--offset", help="Starting position in the dataset(entering in increments of 10)",type=str)
    parser.add_argument("-a", "--san", help="extract san domains", action='store_true')
    return parser.parse_args()


def seek_domains(query,offset=0):
    url = "https://api.criminalip.io/v1/banner/search"
    headers = {
        "x-api-key": api_key
    }

    params = {
        "query": f"ssl_subject_organization:{query}",
        "offset": offset
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()["data"]["result"]
    ssl_subject_common_names = [item["ssl_subject_common_name"] for item in data]
    unique_ssl_subject_common_names = sorted(set(ssl_subject_common_names))

    for name in unique_ssl_subject_common_names:
        print(name)

def seek_san(query,offset=0):
    url="https://api.criminalip.io/v1/banner/search"
    query_params = {
        "query": f"ssl_subject_organization:{query}",
        "offset": offset
    }
    headers = {
        "x-api-key": api_key
    }

    response = requests.get(url, params=query_params, headers=headers)
    data = response.json()

    ssl_info_list = [banner.get("ssl_info", "") for banner in data.get("data", {}).get("result", [])]
    pattern = r'\b((?:[a-zA-Z0-9][a-zA-Z0-9-]{0,61}[a-zA-Z0-9]\.)+(?:[a-zA-Z]{2,}))\b'

    ssl_domains = []

    for info in ssl_info_list:
        matches = re.findall(pattern, info)
        ssl_domains.extend(matches)

        for domain in ssl_domains:
            print(domain)

def seek_ips(query,offset=0):
    url="https://api.criminalip.io/v1/banner/search"
    query_params = {
        "query": f"ssl_subject_organization:{query}",
        "offset": offset
    }
    headers = {
        "x-api-key": api_key
    }

    response = requests.get(url, headers=headers, params=query_params)
    ip_addresses = []

    if response.status_code == 200:
        data = response.json().get("data", {}).get("result", [])
        ip_addresses = list(set(item.get("ip_address") for item in data))
    else:
        print("Error:", response.status_code)

    return sorted(ip_addresses)




if __name__ == "__main__":
    banner()
    if parse_arguments().orgname:
        if parse_arguments().offset:
            if parse_arguments().san:
                seek_san(parse_arguments().orgname,parse_arguments().offset)
            if parse_arguments().domains:
                seek_domains(parse_arguments().orgname,parse_arguments().offset)
            if parse_arguments().ips:
                ips=seek_ips(parse_arguments().orgname,parse_arguments().offset)
                for i in ips:
                    print(i)        
        else:
            if parse_arguments().san:
                seek_san(parse_arguments().orgname)
            if parse_arguments().domains:
                seek_domains(parse_arguments().orgname)
            if parse_arguments().ips:
                ips=seek_ips(parse_arguments().orgname)
                for i in ips:
                    print(i)
            
