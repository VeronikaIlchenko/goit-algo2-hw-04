class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def put(self, key, value=None):
        current = self.root
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True


class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise TypeError("Патерн повинен бути рядком")
        
        count = 0
        
        def dfs(node, current_word):
            nonlocal count
            if node.is_end_of_word:
                if current_word.endswith(pattern):
                    count += 1
            for char, child in node.children.items():
                dfs(child, current_word + char)

        dfs(self.root, "")
        return count

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise TypeError("Префікс повинен бути рядком")
        
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True


class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not strings:
            return ""
        
        for s in strings:
            if not isinstance(s, str):
                return ""
            self.put(s)

        current = self.root
        prefix = ""

        while len(current.children) == 1 and not current.is_end_of_word:
            char = list(current.children.keys())[0]
            prefix += char
            current = current.children[char]

        return prefix


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    assert trie.count_words_with_suffix("e") == 1
    assert trie.count_words_with_suffix("ion") == 1
    assert trie.count_words_with_suffix("a") == 1
    assert trie.count_words_with_suffix("at") == 1

    assert trie.has_prefix("app") == True
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True
    assert trie.has_prefix("ca") == True

    trie_lc1 = LongestCommonWord()
    strings1 = ["flower", "flow", "flight"]
    assert trie_lc1.find_longest_common_word(strings1) == "fl"

    trie_lc2 = LongestCommonWord()
    strings2 = ["interspecies", "interstellar", "interstate"]
    assert trie_lc2.find_longest_common_word(strings2) == "inters"

    trie_lc3 = LongestCommonWord()
    strings3 = ["dog", "racecar", "car"]
    assert trie_lc3.find_longest_common_word(strings3) == ""

    print("Усі тести успішно пройдено!")