from trie import Trie

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not strings:
            return ""

        prefix = strings[0]

        for word in strings[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix

if __name__ == "__main__":
    trie = LongestCommonWord()
    assert trie.find_longest_common_word(["flower", "flow", "flight"]) == "fl"
    assert trie.find_longest_common_word(["interspecies", "interstellar", "interstate"]) == "inters"
    assert trie.find_longest_common_word(["dog", "racecar", "car"]) == ""
