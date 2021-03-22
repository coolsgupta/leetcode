import requests
def totalTransactions(locationId, transactionType):
    numPages = 1
    currPage = 1
    dataMap = {}
    while currPage <= numPages:
        res = requests.get("https://jsonmock.hackerrank.com/api/transactions/search?txnType={}debit&page={}".format(transactionType, str(currPage)))
        if res.status_code == 200:
            dataJson = res.json()
            numPages = dataJson['total_pages']
            for record in dataJson['data']:
                if record['location']['id'] == locationId:
                    if record['id'] not in dataMap:
                        dataMap[record['id']] = 0

                    dataMap[record['id']] += float(record['amount'][1:].replace(',', ''))

        currPage += 1

    if not dataMap:
        return [-1,-1]

    return sorted(list(map(lambda x: [x[0], int(x[1])], dataMap.items())))

if __name__ == '__main__':
    print(totalTransactions(1, 'debit'))