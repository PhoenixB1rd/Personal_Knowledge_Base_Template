import argparse
import json
import requests
import time


def login(api_url, email=None, password=None):
    

    return resp.json()["jwt"]["access"]


def query(api_url, jwt_token, api_token, query_type, output_file, query_param_list):
    
    


def main():
    parser = argparse.ArgumentParser(description="Query cloud account")
    parser.add_argument("--api-url", help="endpoint to connect to", default="<deafault_url>")

    args = parser.parse_args()

   
    query(args.api_url, None, args.api_token, args.query_type, args.output_json_file, args.query_params)


if __name__ == "__main__":
    main()
