class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = {}
        self.users = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[tweetId] = datetime.datetime.utcnow()
        if userId not in self.users:
            self.initializeUser(userId)

        self.users[userId]['tweets'].add(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        users = [userId]
        users.extend(self.users.get(userId, {}).get('following', []))

        tweets = set()
        for uid in users:
            tweets.update(self.users.get(uid, {}).get('tweets', []))

        tweets = sorted(tweets, key=lambda x: self.tweets[x], reverse=True)
        return tweets[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.users:
            self.initializeUser(followerId)

        if followeeId not in self.users:
            self.initializeUser(followeeId)

        self.users[followerId]['following'].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.users.get(followerId, {}).get('following', []):
            self.users[followerId]['following'].remove(followeeId)

    def initializeUser(self, userId):
        self.users[userId] = {
            'tweets': set(),
            'following': set()
        }

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)