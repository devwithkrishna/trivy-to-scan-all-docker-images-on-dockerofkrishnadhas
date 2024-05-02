import requests
import argparse
import json
from datetime import datetime


def get_all_images_from_dockerhub(account_name:str):
    """
    function to retrieve docker images list
    :param account_name: docker hub acccount name. default dockerofkrishnadhas
    :return:
    """
    api_endpoint = f'https://hub.docker.com/v2/repositories/{account_name}/'
    # print(api_endpoint)
    # Define pagination parameters
    per_page = 50  # Number of records per page
    page = 1  # Initial page number
    docker_image_names_list = []
    while True:
        params = {
            'per_page': per_page,  # Number of results per page
            'page': page # Page number
        }
        # API call
        response = requests.get(url=api_endpoint, params=params)
        response_json = response.json() ## Github repo details

        # Checking the API status code
        if response.status_code == 200:
            print(f"API request successful on {api_endpoint}")
            # print(response_json)
        else:
            print(f"API request failed with status code {response.status_code}:")
            # print(response_json)
            break

        for images in response_json['results']:
            docker_image_names_list.append(images['name'])

        page += 1  # Move to the next page
        file_name = f'docker_images_tags_{account_name}_results.json'
        with open(file_name, 'w') as json_file:
            json.dump(response_json['results'], json_file, indent=4)
        # Break the loop if no more pages
        if len(response_json['results']) < per_page:
            break
    print(f'Total number of images under {account_name} is : {len(docker_image_names_list)}')

    return docker_image_names_list

def get_image_tags_from_repository(account_name: str):
    """
    get the tags from a docker image
    :param account_name:
    :return:
    """
    docker_image_names_list = get_all_images_from_dockerhub(account_name=account_name)
    docker_image_tag_list = []
    for image in docker_image_names_list:
        tag_endpoint = f'https://hub.docker.com/v2/namespaces/{account_name}/repositories/{image}/tags'
        # print(tag_endpoint)
        response = requests.get(tag_endpoint)
        # Checking the API status code
        if response.status_code == 200:
            print(f"API request successful on {tag_endpoint}")
            # print(response_json)
        else:
            print(f"API request failed with status code {response.status_code}:")
            # print(response_json)
            break
        response_json = response.json()
        response_json_results = response_json['results']
        tag_count = response_json['count']
        print(f'Number of tags of {account_name}/{image} is : {tag_count}')
        for item in response_json_results:
            tag = item['name']
            docker_image_tag_list.append(f'{account_name}/{image}:{tag}')
    file_name = f'docker_images_details_{account_name}.json'
    with open(file_name, 'w') as json_file:
        json.dump(docker_image_tag_list, json_file, indent=4)
    return docker_image_tag_list

def date_time():
    """ Simple function to print time """
    now = datetime.now()
    current_time = now.strftime("%B %d %Y - %H:%M:%S")
    return current_time


def main():
    """ To test the code"""
    parser = argparse.ArgumentParser("Retrieve Docker images and tags from dockerhub registry using python")
    parser.add_argument("--account_name", help="dockerhub user name", required=True, type=str)

    args = parser.parse_args()
    account_name = args.account_name
    starting_time = date_time()
    print(f"Proccess to retrieve Docker images and tags from dockerhub registry started at {starting_time} IST......")
    docker_image_tag_list = get_image_tags_from_repository(account_name)
    print(docker_image_tag_list)
    ending_time = date_time()
    print(f"Proccess to retrieve Docker images and tags from dockerhub registry completed at {ending_time} IST......")

if __name__ == "__main__":
    main()