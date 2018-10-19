import unittest
import file

class TestMyServer(unittest.TestCase):

	def test_first(self):
		response = server.hello()
		self.assertIn("Hello", response, "Hello was not found on response")



if __name__ == "__main__":
    app.run()