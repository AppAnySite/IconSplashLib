import unittest
import os
import logging
from PIL import Image, ImageChops
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TestIconGeneration(unittest.TestCase):

    def test_android_mipmap_mdpi_foreground(self):
        logging.info("Starting test: test_android_mipmap_mdpi_foreground")
        
        # Path to the generated icon
        generated_icon_path = 'output/icons/android/mipmap-mdpi/ic_launcher_foreground.png'
        
        # Path to the original logo
        original_logo_path = '~/Documents/Github/AppAnySite/Utils/tools/my-node-cli-tool/logo.png'
        
        # Ensure paths are expanded
        generated_icon_path = os.path.expanduser(generated_icon_path)
        original_logo_path = os.path.expanduser(original_logo_path)

        # Check if the file is created
        self.assertTrue(os.path.exists(generated_icon_path), "Generated icon does not exist")
        logging.info("Generated icon exists")

        # Check if the file is the latest (within the last hour)
        one_hour_ago = time.time() - 3600
        icon_mod_time = os.path.getmtime(generated_icon_path)
        self.assertTrue(icon_mod_time > one_hour_ago, "Generated icon is not the latest")
        logging.info("Generated icon is the latest")

        # Check if the size is as specified in android_config.json
        expected_size = (108, 108)
        with Image.open(generated_icon_path) as img:
            self.assertEqual(img.size, expected_size, f"Generated icon size {img.size} does not match the expected size {expected_size}")
        logging.info(f"Generated icon size is correct: {expected_size}")

        # Compare resized original logo with the generated icon
        with Image.open(original_logo_path) as original_img:
            resized_original = original_img.resize(expected_size, Image.LANCZOS)
            resized_original.save('/tmp/resized_logo.png')
            with Image.open(generated_icon_path) as generated_img:
                difference = ImageChops.difference(resized_original.convert('RGBA'), generated_img.convert('RGBA'))
                diff_bbox = difference.getbbox()
                self.assertIsNone(diff_bbox, "Generated icon content does not match the original logo resized")
        logging.info("Generated icon content matches the original logo resized")

if __name__ == '__main__':
    unittest.main()
