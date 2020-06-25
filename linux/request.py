from requests_kerberos import HTTPKerberosAuth, REQUIRED
import logging
import sys
import requests
import json
from requests_ntlm import HttpNtlmAuth

if __name__ == '__main__':
    import configparser
    config = configparser.ConfigParser()
    config.read('config.ini')
    logging.basicConfig(level=logging.DEBUG, filename="ntlm.log", format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    url = sys.argv[1]
    type = sys.argv[2]
    type_auth = config['TYPE']['type']
    auth = None
    if type_auth == 'kerberos':
        auth = HTTPKerberosAuth(mutual_authentication=REQUIRED, sanitize_mutual_error_response=False)
    else:
        auth = HttpNtlmAuth(sys.argv[3], sys.argv[4])
    s = requests.Session()
    s.headers.update({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, '
                                    'like Gecko) Chrome/39.0.2171.95 Safari/537.36'})

    r = None
    if type == 'get':
        r = s.get(url, auth=auth)
    elif type == 'post':
        data = sys.argv[3]
        r = s.post(url,
                          auth=auth,
                          data=data
                          )
    elif type == 'patch':
        data = sys.argv[3]
        r = s.patch(url,
                          auth=auth,
                          data=data
                          )
    elif type == 'delete':
        r = s.patch(
            url,
            auth=auth,
            data=json.dumps({
                "DeletionMark": True
            })
        )
    if 'json' not in r.headers['Content-Type']:
        print({'result': r.text, 'code': r.status_code})
    else:
        print({'result': r.json(), 'code': r.status_code})