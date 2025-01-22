import unittest
import logging
from icon_test_framework import IconTestFramework

class TestAndroidIconGeneration(unittest.TestCase):
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

    def test_android_mipmap_mdpi_foreground(self):
        logging.info("Starting test: test_android_mipmap_mdpi_foreground")
        platform = "android"
        folder = "mipmap-mdpi"
        icon_type = "ic_launcher_foreground"
        icon_size = 108
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")

    
    def test_android_mipmap_mdpi_round(self):
        logging.info("Starting test: test_android_mipmap_mdpi_round")
        platform = "android"
        folder = "mipmap-mdpi"
        icon_type = "ic_launcher_round"
        icon_size = 48
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")

    def test_android_mipmap_mdpi_launcher(self):
        logging.info("Starting test: test_android_mipmap_mdpi_launcher")
        platform = "android"
        folder = "mipmap-mdpi"
        icon_type = "ic_launcher"
        icon_size = 48
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")

    def test_android_mipmap_hdpi_foreground(self):
        logging.info("Starting test: test_android_mipmap_hdpi_foreground")
        platform = "android"
        folder = "mipmap-hdpi"
        icon_type = "ic_launcher_foreground"
        icon_size = 162
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")
    
    def test_android_mipmap_hdpi_round(self):
        logging.info("Starting test: test_android_mipmap_hdpi_round")
        platform = "android"
        folder = "mipmap-hdpi"
        icon_type = "ic_launcher_round"
        icon_size = 72
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")

    def test_android_mipmap_hdpi_launcher(self):
        logging.info("Starting test: test_android_mipmap_hdpi_launcher")
        platform = "android"
        folder = "mipmap-hdpi"
        icon_type = "ic_launcher"
        icon_size = 72
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")

    def test_android_mipmap_xhdpi_foreground(self):
        logging.info("Starting test: test_android_mipmap_xhdpi_foreground")
        platform = "android"
        folder = "mipmap-xhdpi"
        icon_type = "ic_launcher_foreground"
        icon_size = 216
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")

    def test_android_mipmap_xhdpi_round(self):
        logging.info("Starting test: test_android_mipmap_xhdpi_round")
        platform = "android"
        folder = "mipmap-xhdpi"
        icon_type = "ic_launcher_round"
        icon_size = 96
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")

    def test_android_mipmap_xhdpi_launcher(self):
        logging.info("Starting test: test_android_mipmap_xhdpi_launcher")
        platform = "android"
        folder = "mipmap-xhdpi"
        icon_type = "ic_launcher"
        icon_size = 96
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")

    def test_android_mipmap_xxhdpi_foreground(self):
        logging.info("Starting test: test_android_mipmap_xxhdpi_foreground")
        platform = "android"
        folder = "mipmap-xxhdpi"
        icon_type = "ic_launcher_foreground"
        icon_size = 324
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")

    def test_android_mipmap_xxhdpi_round(self):
        logging.info("Starting test: test_android_mipmap_xxhdpi_round")
        platform = "android"
        folder = "mipmap-xxhdpi"
        icon_type = "ic_launcher_round"
        icon_size = 144
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")

    def test_android_mipmap_xxhdpi_launcher(self):
        logging.info("Starting test: test_android_mipmap_xxhdpi_launcher")
        platform = "android"
        folder = "mipmap-xxhdpi"
        icon_type = "ic_launcher"
        icon_size = 144
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")

    
    def test_android_mipmap_xxxhdpi_foreground(self):
        logging.info("Starting test: test_android_mipmap_xxxhdpi_foreground")
        platform = "android"
        folder = "mipmap-xxxhdpi"
        icon_type = "ic_launcher_foreground"
        icon_size = 432
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")

    def test_android_mipmap_xxxhdpi_round(self):
        logging.info("Starting test: test_android_mipmap_xxxhdpi_round")
        platform = "android"
        folder = "mipmap-xxxhdpi"
        icon_type = "ic_launcher_round"
        icon_size = 192
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")

    def test_android_mipmap_xxxhdpi_launcher(self):
        logging.info("Starting test: test_android_mipmap_xxxhdpi_launcher")
        platform = "android"
        folder = "mipmap-xxxhdpi"
        icon_type = "ic_launcher"
        icon_size = 192
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")


    
    def test_android_mipmap_ldpi_launcher(self):
        logging.info("Starting test: test_android_mipmap_ldpi_launcher")
        platform = "android"
        folder = "mipmap-ldpi"
        icon_type = "ic_launcher"
        icon_size = 36
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")

    def test_android_playstore_icon_launcher(self):
        logging.info("Starting test: test_android_playstore-icon_launcher")
        platform = "android"
        folder = "playstore-icon"
        icon_type = "playstore_icon"
        icon_size = 512
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")

    def test_android_ic_launcher_web_launcher(self):
        logging.info("Starting test: test_android_ic_launcher_web")
        platform = "android"
        folder = "ic_launcher-web"
        icon_type = "ic_launcher-web"
        icon_size = 512
        results = self.framework.process_icon_validation(platform, folder, icon_type, icon_size)
        self.print_validation_summary(results)

        self.assertTrue(results['exists'], "Generated icon does not exist.")
        self.assertTrue(results['is_latest'], "Generated icon is not the latest.")
        self.assertTrue(results['size_matches'], "Generated icon size does not match expected size.")
        self.assertTrue(results['content_matches'], "Generated icon content does not match the original.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
