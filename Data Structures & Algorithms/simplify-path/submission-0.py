class Solution:
    def simplifyPath(self, path: str) -> str:
        words = [w for w in path.split("/") if w]
        stack = []
        for w in words:
            if w == "..":
                if stack:

                    stack.pop()
            elif w == ".":
                continue
            else:
                stack.append(w)
        return "/" +("/").join(stack)