import sys

from alibabacloud_cdn20180510.client import Client as Cdn20180510Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_cdn20180510 import models as cdn_20180510_models


argv = sys.argv[1:]
if len(argv) < 3:
    print('Usage: python refresh_cdn_cache.py <access_key_id> <access_key_secret> <file_path>')
    sys.exit(1)

access_key_id = argv[0]
access_key_secret = argv[1]
file_paths = argv[2:]

print('file_paths:', file_paths)


if __name__ == '__main__':
    config = open_api_models.Config(
        access_key_id=access_key_id, access_key_secret=access_key_secret
    )
    config.endpoint = 'cdn.aliyuncs.com'
    cdn_client = Cdn20180510Client(config)


    file_list = []
    directory_list = []
    for file_path in file_paths:
        if file_path.endswith('/'):
            directory_list.append(file_path)
        else:
            file_list.append(file_path)

    if file_list:
        print('Refresh file cache:', ' '.join(file_list))
        refresh_object_caches_request = cdn_20180510_models.RefreshObjectCachesRequest(
            object_path='\n'.join(file_list), object_type='File'
        )
        refresh_object_caches_response = cdn_client.refresh_object_caches(refresh_object_caches_request)
        print(refresh_object_caches_response.body)

    if directory_list:
        print('Refresh directory cache:', ' '.join(directory_list))
        refresh_object_caches_request = cdn_20180510_models.RefreshObjectCachesRequest(
            object_path='\n'.join(directory_list), object_type='Directory'
        )
        refresh_object_caches_response = cdn_client.refresh_object_caches(refresh_object_caches_request)
        print(refresh_object_caches_response.body)
    print('Done')
