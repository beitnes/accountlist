import boto3
import pprint

def account_list(output_format = "json"):

    #TODO: Add other output formats
    client = boto3.client('organizations')

    pretty_printer = pprint.PrettyPrinter(indent=4)

    accounts = list()

    response = client.list_accounts()

    while True:

        next_token = response.get('NextToken')

        for account in response['Accounts']:
            accounts.append(account)

        if next_token == None:
            break
        else:
            response = client.list_accounts(NextToken=next_token)

    # print("quantity: " + str(len(accounts)))

    if output_format == "json":
        pretty_printer.pprint(accounts)


def main():
    #TODO: parse args
    #TODO: Set up logging
    account_list()



if __name__ == "__main__":
    main()
