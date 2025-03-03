import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage


class TestHBNBCommand(unittest.TestCase):
    """Test suite for the HBNBCommand console"""

    def setUp(self):
        """Set up test environment"""
        self.console = HBNBCommand()

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        """Test quit command"""
        self.assertTrue(self.console.do_quit(""))
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF(self, mock_stdout):
        """Test EOF command"""
        self.assertTrue(self.console.do_EOF())
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_missing_class(self, mock_stdout):
        """Test create with missing class name"""
        self.console.do_create("")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_invalid_class(self, mock_stdout):
        """Test create with invalid class name"""
        self.console.do_create("InvalidClass")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_show_missing_class(self, mock_stdout):
        """Test show with missing class name"""
        self.console.do_show("")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_show_invalid_class(self, mock_stdout):
        """Test show with invalid class name"""
        self.console.do_show("InvalidClass 1234")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_show_missing_id(self, mock_stdout):
        """Test show with missing ID"""
        self.console.do_show("BaseModel")
        self.assertEqual(mock_stdout.getvalue().strip(), "** instance id missing **")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_missing_class(self, mock_stdout):
        """Test destroy with missing class name"""
        self.console.do_destroy("")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_invalid_class(self, mock_stdout):
        """Test destroy with invalid class name"""
        self.console.do_destroy("InvalidClass 1234")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_missing_id(self, mock_stdout):
        """Test destroy with missing ID"""
        self.console.do_destroy("BaseModel")
        self.assertEqual(mock_stdout.getvalue().strip(), "** instance id missing **")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_all_invalid_class(self, mock_stdout):
        """Test all with an invalid class"""
        self.console.do_all("InvalidClass")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_class(self, mock_stdout):
        """Test update with missing class name"""
        self.console.do_update("")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_update_invalid_class(self, mock_stdout):
        """Test update with invalid class name"""
        self.console.do_update("InvalidClass 1234")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_id(self, mock_stdout):
        """Test update with missing ID"""
        self.console.do_update("BaseModel")
        self.assertEqual(mock_stdout.getvalue().strip(), "** instance id missing **")

if __name__ == '__main__':
    unittest.main()