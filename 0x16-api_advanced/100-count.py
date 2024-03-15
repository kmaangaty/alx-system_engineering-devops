#!/usr/bin/python3
"""
    recursive function that queries the Reddit API,
    parses the title of all hot articles, and prints
    a sorted count of given keywords (case-insensitive,
    delimited by spaces. Javascript should count as javascript,
    but java should not).
"""
import requests


def count_words(subreddit, word_list, instances=None, after="", count=0):
    """
        recursive function that queries the Reddit API,
        parses the title of all hot articles, and prints
        a sorted count of given keywords (case-insensitive,
        delimited by spaces. Javascript should count as javascript,
        but java should not).
    """
    if instances is None:
        instances = {}
    rpt = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    hds = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    pms = {
        "after": after,
        "count": count,
        "limit": 100
    }
    rp = requests.get(rpt, headers=hds, params=pms,
                            allow_redirects=False)
    try:
        ntg = rp.json()
        if rp.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    ntg = ntg.get("data")
    after = ntg.get("after")
    count += ntg.get("dist")
    for x in ntg.get("children"):
        ann = x.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in ann:
                cts = len([t for t in ann if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = cts
                else:
                    instances[word] += cts

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda mk: (-mk[1], mk[0]))
        [print("{}: {}".format(m, k)) for m, k in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
