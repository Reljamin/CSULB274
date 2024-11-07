from SLLStack import SLLStack


class Calculator:
    def __init__(self):
        self.dict = None

    def balanced_parens(self, s: str) -> bool:
        """
        This function checks if the string s contains balanced parentheses
        :param s: str type; the string to be checked
        :return: bool type; True if the string s contains balanced parentheses
        """
        s1 = SLLStack()
 
        for char in s:
            if char == "(":
                s1.push(char)
            if char == ")":
                if s1.size() == 0:
                    return False
                s1.pop()
 
 
        if s1.size() == 0:
            return True
        
        pass #FIXME: remove
