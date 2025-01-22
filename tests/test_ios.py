import unittest
import logging
from icon_test_framework import IconTestFramework

class TestIOSIconGeneration(unittest.TestCase):
    def setUp(self):
        self.framework = IconTestFramework()

    def print_validation_summary(self, results):
        """Helper method to print validation results summary in a table format."""
        print("Validation Summary:")
        print("+------------------+---------+")
        print("| Validation Step   | Result  |")
        print("+------------------+---------+")
        print(f"| File Exists       | {'Passed' if results['exists'] else 'Failed'}  |")
        print(f"| Latest File       | {'Passed' if results['is_latest'] else 'Failed'}  |")
        print(f"| Size Matches      | {'Passed' if results['size_matches'] else 'Failed'}  |")
        print(f"| Content Matches   | {'Passed' if results['content_matches'] else 'Failed'}  |")
        print("+------------------+---------+")

    
    def test_ios_appicon_20x20_2x(self):
        logging.info("Starting test: test_ios_appicon_20x20_2x")
        platform = "ios"
        folder = None
        icon_type = "AppIcon-20x20@2x"
        icon_size = 40
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")

    def test_ios_appicon_20x20_3x(self):
        logging.info("Starting test: test_ios_appicon_20x20_3x")
        platform = "ios"
        folder = None
        icon_type = "AppIcon-20x20@3x"
        icon_size = 60
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")

    def test_ios_appicon_29x29_2x(self):
        logging.info("Starting test: test_ios_appicon_29x29_2x")
        platform = "ios"
        folder = None
        icon_type = "AppIcon-29x29@2x"
        icon_size = 58
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")

    def test_ios_appicon_29x29_3x(self):
        logging.info("Starting test: test_ios_appicon_29x29_3x")
        platform = "ios"
        folder = None
        icon_type = "AppIcon-29x29@3x"
        icon_size = 87
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")

    def test_ios_appicon_40x40_2x(self):
        logging.info("Starting test: test_ios_appicon_40x40_2x")
        platform = "ios"
        folder = None
        icon_type = "AppIcon-40x40@2x"
        icon_size = 80
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")

    def test_ios_appicon_40x40_3x(self):
        logging.info("Starting test: test_ios_appicon_40x40_3x")
        platform = "ios"
        folder = None
        icon_type = "AppIcon-40x40@3x"
        icon_size = 120
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")

    def test_ios_appicon_60x60_2x(self):
        logging.info("Starting test: test_ios_appicon_60x60_2x")
        platform = "ios"
        folder = None
        icon_type = "AppIcon-60x60@2x"
        icon_size = 120
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")

    def test_ios_appicon_60x60_3x(self):
        logging.info("Starting test: test_ios_appicon_60x60_3x")
        platform = "ios"
        folder = None
        icon_type = "AppIcon-60x60@3x"
        icon_size = 180
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")

    def test_ios_appicon_1024x1024_1x(self):
        logging.info("Starting test: test_ios_appicon_1024x1024_1x")
        platform = "ios"
        folder = None
        icon_type = "AppIcon-1024x1024@1x"
        icon_size = 1024
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")




    

    

if __name__ == "__main__":
    unittest.main(verbosity=2)
