# -*- coding: utf-8 -*-
# Cut a Magazine to get a note. A magazie is a single-line string (without '\n'), and a note is a target string.
# Now using a sissor to cut the magazine, we need to find the minimum cuts that are imposed on the magazine to get the note.
# For example: Magazine="Hello World", Note="He Wor" -> 8 cuts。Magazine="Hello World", Note="llo Wor" -> 4 cuts
# 想象magazine是真的一行写在纸上的字。你要用剪刀把它剪碎，拼出你想要的note。所以，一个单词至少要剪四刀.

# Need further work
class Solution(object):
    def cutMagazine(self, magazine, note):
        self.mem = {}
        self.res = 0

        def dfs(magazine, note):
            if note in self.mem and self.mem[note]:
                return True

            elif note in magazine:
                self.mem[note] = True
                return True

            for i in range(1, len(note)):
                left = dfs(magazine, note[:i])
                right = dfs(magazine, note[i:])

                if left and right:
                    self.mem[note] = True
                    return True

            self.mem[note] = False
            return False