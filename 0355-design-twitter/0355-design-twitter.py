class Twitter:
    """
    Time: O(klogn)
    Space: O(n)

    We are storing the tweets (which user has tweeted what) and followees (which user follows other users). We have a 
    global counter for tweet to see which tweet has been tweeted first and in which order. We then take this tweets and
    heapify it. We use a max heap to efficiently get the top 10 recent tweets and get the tweet IDs.
    
    Instead of heap, we can try to just sort the tweet counts. But sorting is nlogn time operation and using a heap to find 
    the top 10 max value is klogn operation.
    """

    def __init__(self):
        self.tweets = {}
        self.followees = {}
        self.tweet_stack = []  # see if there is a better way and not use this extra memory

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweet_stack.append(tweetId)
        self.tweets[userId].append((-len(self.tweet_stack)-1, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        feed_limit = 10
        # Get all the tweets made the user and the followees
        tweets = self._get_tweets(userId)
        # Retrieve 10 most recent tweets (10 highest tweet IDs)
        heapq.heapify(tweets)
        while tweets and feed_limit > 0:  # O(klogn)
            feed.append(heapq.heappop(tweets)[1])
            feed_limit -= 1
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followees:
            self.followees[followerId] = {followerId}  # set, user is following themself
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followees and followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)

    def _get_tweets(self, userId):
        # Get all the followees of the given userId
        if userId in self.followees:
            followees = [followee for followee in self.followees[userId]]
        else:
            followees = [userId]
        # Get all the tweets that the followees made
        tweets = []
        # Check if the followee has made any tweets
        for followee in followees:
            if followee in self.tweets:
                tweets.extend(self.tweets[followee])
        return [(count, tweet) for count, tweet in tweets]  # since we are using a max heap, the numbers need to be -ve

            
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)