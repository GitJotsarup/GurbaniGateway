import json

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(41)]
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, ch):
        if 'ੳ' <= ch <= 'ੲ':
            return ord(ch) - ord('ੳ')
        return -1

    def insert(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
        pCrawl.isEndOfWord = True

def search_dharnas(data, search_query):
    t = Trie()

    # Insert all Punjabi words from dharnas into the Trie, this should only be done once
    for entry in data:
        punjabi_text = entry.get("punjabi")
        if punjabi_text:
            words = punjabi_text.split()
            for word in words:
                t.insert(word)

    matching_dharnas = []

    for entry in data:
        punjabi_text = entry.get("punjabi")
        if punjabi_text:
            words = punjabi_text.split()
            matched = True

            for char, word in zip(search_query, words):
                if not word.startswith(char):
                    matched = False
                    break

            if matched:
                matching_dharnas.append(entry.get("title"))

    return matching_dharnas

if __name__ == '__main__':
    with open("dharnas.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    search_query = input("Enter your search query in Punjabi: ")
    search_dharnas(data, search_query)