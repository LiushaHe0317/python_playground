class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or any(not x for x in [A, B]):
            return False
        else:
            if A == B:
                return True if len(set(A)) <= len(A)/2 else False
            else:
                if set(A) != set(B):
                    return False
                else:
                    cimap_a, cimap_b = {}, {}
                    for a, b in zip(A, B):
                        if a != b:
                            if a not in cimap_a:
                                cimap_a[a] = 1
                            else:
                                cimap_a[a] += 1
                            if b not in cimap_b:
                                cimap_b[b] = 1
                            else:
                                cimap_b[b] += 1

                            if cimap_a[a] > 1:
                                return False
                            if cimap_b[b] > 1:
                                return False

                        if len(cimap_a) > 2:
                            return False
                        if len(cimap_b) > 2:
                            return False

                    else:
                        return True


if __name__ == '__main__':
    s = Solution()
    assert s.buddyStrings("ab", "ba") == True
    assert s.buddyStrings("ab", "ab") == False
    assert s.buddyStrings("aa", "aa") == True
    assert s.buddyStrings("aaaaaaabc", "aaaaaaacb") == True
    assert s.buddyStrings("abab", "abab") == True
    assert s.buddyStrings("", "") == False
    assert s.buddyStrings("abccccccc", "abccccccc") == True
    assert s.buddyStrings("abcaa", "abcbb") == False
