import argparse



def query(api_url):
    
    return


def main():
    parser = argparse.ArgumentParser(description="Query something")
    parser.add_argument("--api-url", help="endpoint to connect to", default="<deafault_url>")

    args = parser.parse_args()

   
    query(args.api_url)


if __name__ == "__main__":
    main()
