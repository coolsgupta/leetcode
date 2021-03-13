def countClicks(input_case):
    count_map = {}
    for x in input_case:
        pair = x.split(',')
        domains = pair[1].split('.')
        curr_domain = ''
        for dom in domains[::-1]:
            if not curr_domain:
                curr_domain = dom
            else:
                curr_domain = '.'.join([dom, curr_domain])

            if curr_domain not in count_map:
                count_map[curr_domain] = 0

            count_map[curr_domain] += int(pair[0])

    return count_map


if __name__ == '__main__':

    counts = [ "900,google.com",
         "60,mail.yahoo.com",
         "10,mobile.sports.yahoo.com",
         "40,sports.yahoo.com",
         "300,yahoo.com",
         "10,stackoverflow.com",
         "20,overflow.com",
         "5,com.com",
         "2,en.wikipedia.org",
         "1,m.wikipedia.org",
         "1,mobile.sports",
         "1,google.co.uk"]

    res = countClicks(counts)
    print(res)