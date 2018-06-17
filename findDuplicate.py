# -*- coding: utf-8 -*-
# 609. Find Duplicate File in System

class Solution(object):
    def findDuplicate(self, paths):
        import collections
        dic = collections.defaultdict(list)
        res = []

        for i in range(len(paths)):
            dir = paths[i].split(' ', 1)[0]
            tmp = paths[i].split(' ', 1)[1]
            nameContents = tmp.split(' ')

            for j in nameContents:
                idx1 = j.find("(")
                idx2 = j.find(")")
                name = j.split('(', 1)[0]
                content = j[idx1 + 1:idx2]
                dic[content].append(dir + '/' + name)

        for key, val in dic.items():
            if len(val) > 1:
                res.append(val)

        return res

test = Solution()
print test.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])


# 大文件，dict: e2fc714c4727ee9395f324cd2e7f331f => PATH/filename.txt
# 先有一个 file size to files 的 map,然后只针对大于 1 的 list 里面的 files 生成 MD5 hashkey
# 超大文件 generate partial hash chunk by chunk 然后 join 成一个 hashkey
# symlink 直接跳过(或set记录visited)
# 查询过程中死机 定期log
# hash冲突，MD5值相同的情况下，再对两个文件进行逐个byte比较
# 如果 file size 很小, 以及一个 size 对应的 file 很多, generate hash 作为 key
import hashlib

print hashlib.md5('abcd').hexdigest()

class Node:
    def __init__(self, content, type, dir):
        self.content = content
        self.type = type
        self.dir = dir
        self.children = []

class Solution2(object):
    def findDuplicate(self, root):
        # md5 => self.dir
        self.dic = {}

        def helper(node):
            if not node or node.type == 'Directory' and len(node.children) == 0:
                return
            for child in node.children:
                if child.type == 'Directory':
                    helper(child)
                elif child.type == 'File':
                    hashcode = hashlib.md5(child.content).hexdigest()
                    if hashcode in self.dic:
                        self.dic[hashcode].append(node.dir)
                    else:
                        self.dic[hashcode] = [node.dir]

        helper(root)

        return self.dic