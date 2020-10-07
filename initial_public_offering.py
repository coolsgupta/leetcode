def getUnallottedUsers(bids, totalShares):
    # Write your code here
    for x in bids:
        x[0], x[1], x[2], x[3] = x[2], -x[3], -x[1], x[0]

    bids.sort(reverse=True)
    previous_price = bids[0][0]
    bucket = []
    result = []
    flag = True

    # for bid in bids:
    for i in range(len(bids) + 1):
        if i < len(bids):
            bid = bids[i]

        if i < len(bids) and not flag:
            result.append(bid[3])

        else:
            if i < len(bids):
                current_price = bid[0]

            if i < len(bids) and current_price == previous_price:
                bucket.append(bid)

            else:
                total = 0
                for b in bucket:
                    total -= b[2]

                if totalShares >= total:
                    totalShares -= total

                    if totalShares == total:
                        flag = False

                else:
                    if totalShares >= len(bids):
                        totalShares = 0
                        flag = False

                    else:
                        for b in bucket:
                            totalShares -= 1

                            if totalShares < 0:
                                result.append(b[3])

                        totalShares = 0

                    flag = False
                bucket.clear()
                bucket.append(bid)

                previous_price = current_price

    return sorted(result)
