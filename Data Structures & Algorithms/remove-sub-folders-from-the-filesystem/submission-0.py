class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, path):
        path = path.split("/")
        curr = self.root
        for c in path:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True
    
    def isPrefix(self,prefix):
        path = prefix.split("/")
        curr = self.root
        for i in range(len(path)-1):
            curr = curr.children[path[i]]
            if curr.end:
                return True
        return False
        
        



class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        """
        if a folder is located within another folder it is considered a subfolder
        a sub folder ust be followed bby a / /a/b is a subfolder of /a
        /a 
        /a/b
        /c/d
        /c/d/e

        let preform a dfs at eveyr given letter 
        /a 
        """
        trie = Trie()
        for f in folder:
            trie.add(f)

        res = []
        for f in folder:
            if not trie.isPrefix(f):
                res.append(f)
        return res