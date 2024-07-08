import heapq
from typing import List


class Twitter:

    def __init__(self):
        # we need to get the min tweet's timestamp from the min heap to get the latest
        # the 1st tweet has timestamp 0, 2nd tweet has timestame -1
        self.timestamp = 0

        self.tweet_map = {}  # userId -> list of [count, tweetIds]
        self.follow_map = {}  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweet_map:
            self.tweet_map[userId] = []

        self.tweet_map[userId].append([self.timestamp, tweetId])
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        min_heap = []

        # add userId to follow map to include user's tweets in feed
        if userId not in self.follow_map:
            self.follow_map[userId] = set()

        self.follow_map[userId].add(userId)

        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:

                # get the last user's tweet
                last_tweet_index = len(self.tweet_map[followeeId]) - 1
                timestamp, tweet_id = self.tweet_map[followeeId][last_tweet_index]

                # add to min heap the last tweet and the index of the next latest tweet
                min_heap.append([timestamp, tweet_id, followeeId, last_tweet_index - 1])

        # create min heap
        heapq.heapify(min_heap)

        while min_heap and len(feed) < 10:
            timestamp, tweet_id, followeeId, last_tweet_index = heapq.heappop(min_heap)
            feed.append(tweet_id)

            # add next user's tweet to min heap
            if last_tweet_index >= 0:
                timestamp, tweet_id = self.tweet_map[followeeId][last_tweet_index]
                heapq.heappush(
                    min_heap, [timestamp, tweet_id, followeeId, last_tweet_index - 1]
                )

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_map:
            self.follow_map[followerId] = set()

        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_map and followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)


# Time Complexity: O(10) or O(k)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


twitter = Twitter()
twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1))
twitter.follow(1, 2)
twitter.postTweet(2, 6)
print(twitter.getNewsFeed(1))
twitter.getNewsFeed(1)
twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1))
