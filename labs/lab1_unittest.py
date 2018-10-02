import subprocess
import unittest

class TestHelloWorld(unittest.TestCase):

    def test_printHelloWorld(self):
        # Grab standard output from importing module
        proc = subprocess.Popen(["python", "-c", "import hello_world;"], stdout=subprocess.PIPE)
        # Deocde output to string
        out = proc.communicate()[0].decode()
        # Convert to lowercase
        out = out.lower()
        # Check if output contains words 'hello' and 'world'
        result = ((out.find('hello') >= 0) and (out.find('world') >= 0))

        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
