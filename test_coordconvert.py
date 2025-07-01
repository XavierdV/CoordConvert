import unittest
from coordconvert.convert import *
import numpy as np 

class Test_cartesian_and_cylindrical(unittest.TestCase):
    def test_random(self):
        """
        Test it works for one position
        """
        
        result = cartesian_to_cylindrical([1,2,3])
        self.assertEqual(result, [np.float64(2.23606797749979), np.float64(1.1071487177940904), np.int64(3)])


    def test_backcompatibility(self):
        """
        Test for compabitiblity between cartesian_to_cylindrical and cylindrical_to_cartesian
        """
        input = np.random.rand(3)*10
        result_temp = cartesian_to_cylindrical(input)
        input_back = cylindrical_to_cartesian(result_temp)
        np.testing.assert_array_almost_equal(input,input_back)

class Test_cartesian_and_spherical(unittest.TestCase):
    def test_cartesian_to_spherical(self):
        """
        Test it works for one position
        """
        
        result = cartesian_to_spherical([1,2,3])
        self.assertEqual(result, [np.float64(3.7416573867739413), np.float64(0.6405223126794246), np.float64(1.1071487177940904)])

    def test_spherical_to_cartesian(self):
        """
        Test it works for one position
        """
        
        result = spherical_to_cartesian([np.float64(3.7416573867739413), np.float64(0.6405223126794246), np.float64(1.1071487177940904)])
        np.testing.assert_array_almost_equal(result, [1,2,3])


    def test_backcompatibility(self):
        """
        Test for compabitiblity between cartesian_to_cylindrical and cylindrical_to_cartesian
        """
        input = np.random.rand(3)*10
        result_temp = cartesian_to_spherical(input)
        input_back = spherical_to_cartesian(result_temp)
        np.testing.assert_array_almost_equal(input,input_back)

class Test_cylindrical_and_spherical(unittest.TestCase):
    def test_cylindrical_to_spherical(self):
        """
        Test it works for one position
        """
        
        result = cylindrical_to_spherical([1,2,3])
        self.assertEqual(result, [np.float64(3.1622776601683795), np.float64(0.3217505543966422),np.float64(2.0)])

    def test_spherical_to_cylindrical(self):
        """
        Test it works for one position
        """
        
        result = spherical_to_cylindrical([np.float64(3.1622776601683795), np.float64(0.3217505543966422),np.float64(2.0)])
        np.testing.assert_array_almost_equal(result, [1,2,3])


    def test_backcompatibility(self):
        """
        Test for compabitiblity between cartesian_to_cylindrical and cylindrical_to_cartesian
        """
        input = [np.random.rand()*10, np.random.rand()*2*np.pi, np.random.rand()*10]
        
        result_temp = cylindrical_to_spherical(input)
        input_back = spherical_to_cylindrical(result_temp)
        
        self.assertAlmostEqual(input[0],input_back[0])  
        self.assertAlmostEqual(input[1]%(np.pi*2),input_back[1]%(np.pi*2))  
        self.assertAlmostEqual(input[2],input_back[2])
        
if __name__ == '__main__':
    unittest.main()

    
