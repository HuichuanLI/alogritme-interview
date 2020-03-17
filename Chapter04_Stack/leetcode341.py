class NestedInteger:
    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    def __init__(self, nestedList):
        def build_generator(nestedList):
            for i in nestedList:
                if i.isInteger():
                    yield i.getInteger()
                else:
                    i = i.getList()
                    for j in build_generator(i):
                        yield j

        self.g = build_generator(nestedList)

    def next(self):
        return self.v

    def hasNext(self):
        try:
            self.v = next(self.g)
            return True
        except:
            return False
