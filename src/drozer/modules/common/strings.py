class Strings(object):
    """
    An implementation of the *nix `strings` command, which searches for ASCII
    strings in a specified file.
    """

    def getStrings(self, path):
        """
        Searches a file for Strings, and returns them in an Array.
        """

        StringsKlass = self.klass("com.mwr.jdiesel.util.Strings")
        
        strings = StringsKlass.get(path)

        if strings.__eq__(None):
            return []
        else:
            return strings.split("\n")
            
