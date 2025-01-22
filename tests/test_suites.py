import unittest
import argparse
from tests.test_android import TestAndroidIconGeneration
from tests.test_ios import TestIOSIconGeneration

def run_tests(selected_tests=None, single_test=None):
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    if selected_tests == "android":
        suite.addTests(loader.loadTestsFromTestCase(TestAndroidIconGeneration))
    elif selected_tests == "ios":
        suite.addTests(loader.loadTestsFromTestCase(TestIOSIconGeneration))
    elif single_test:
        suite.addTest(loader.loadTestsFromName(single_test))
    else:
        suite.addTests(loader.loadTestsFromTestCase(TestAndroidIconGeneration))
        suite.addTests(loader.loadTestsFromTestCase(TestIOSIconGeneration))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run icon generation tests.")
    parser.add_argument("--android", action="store_true", help="Run Android icon tests")
    parser.add_argument("--ios", action="store_true", help="Run iOS icon tests")
    parser.add_argument("--single-test", type=str, help="Run a single test by specifying the full path (e.g., tests.test_android.TestAndroidIconGeneration.test_android_mipmap_mdpi_foreground)")

    args = parser.parse_args()

    if args.android:
        run_tests("android", args.single_test)
    elif args.ios:
        run_tests("ios", args.single_test)
    elif args.single_test:
        run_tests(None, args.single_test)
    else:
        run_tests()
