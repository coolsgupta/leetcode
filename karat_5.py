def getCommonSeq(user1, user2):
    n = len(user1)
    m = len(user2)
    max_seq = []
    for i in range(n):
        for j in range(m):
            if user1[i] == user2[j]:
                curr_seq = []
                x = i
                y = j
                while(x < n and y < m and user1[x] == user2[y]):
                    curr_seq.append(user1[x])
                    x += 1
                    y += 1

                if len(curr_seq) > len(max_seq):
                    max_seq = curr_seq

    print(max_seq)

if __name__ == '__main__':
    user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
    user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
    user2 = ["a", "/one", "/two"]
    user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
    user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
    user5 = ["a"]
    user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]
    getCommonSeq(user2, user1)

