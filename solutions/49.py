from collections import defaultdict
class Solution:
  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    dict = defaultdict(list)

    for str in strs:
      key = "".join(sorted(str))
      dict[key].append(str)
    return list(dict.values())
