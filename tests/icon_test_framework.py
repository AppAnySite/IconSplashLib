import os
import time
import logging
from PIL import Image, ImageChops, ImageDraw, ImageOps
import json
import tempfile

class IconTestFramework:
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    TOOLS_DIR = os.path.join(BASE_DIR, 'tools')
    GENERATED_ICON_DIR_ANDROID = os.path.join("output", "icons", "android")
    GENERATED_ICON_DIR_IOS = os.path.join("output", "icons", "ios")
    LOGO_PATH = os.path.join(TOOLS_DIR, "my-node-cli-tool", "logo.png")
    CONFIG_ANDROID_PATH = os.path.join(TOOLS_DIR, "IconSplashLib", "config", "android_config.json")
    CONFIG_IOS_PATH = os.path.join(TOOLS_DIR, "IconSplashLib", "config", "ios_config.json")
    LOG_LEVEL = logging.INFO

    def __init__(self):
        self.generated_icon_dir_android = self.GENERATED_ICON_DIR_ANDROID
        self.generated_icon_dir_ios = self.GENERATED_ICON_DIR_IOS
        self.logo_path = self.LOGO_PATH
        self.config_android = self.load_config(self.CONFIG_ANDROID_PATH)
        self.config_ios = self.load_config(self.CONFIG_IOS_PATH)
        logging.basicConfig(level=self.LOG_LEVEL)

    def load_config(self, config_file):
        """Load the JSON configuration file."""
        with open(config_file, 'r') as f:
            return json.load(f)

    def is_latest(self, file_path, max_age_seconds=3600):
        """Check if the file is the latest within the last hour."""
        return os.path.getmtime(file_path) >= time.time() - max_age_seconds

    def verify_image_size(self, image_path, expected_size):
        """Verify that the image size matches the expected size."""
        with Image.open(image_path) as img:
            return img.size == expected_size

    def compare_images(self, generated_icon_path, original_image_path, expected_size, icon_type=None):
        """Compare the generated image with the original one, resized to the expected size."""
        with Image.open(original_image_path) as original_img:
            resized_original = original_img.resize(expected_size, Image.LANCZOS).convert("RGBA")
            if icon_type == "round":
                mask = Image.new("L", expected_size, 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0) + expected_size, fill=255)
                rounded_original = ImageOps.fit(resized_original, mask.size, centering=(0.5, 0.5))
                rounded_original.putalpha(mask)
                resized_original = rounded_original

            # Get a dynamic temporary directory
            temp_dir = tempfile.gettempdir()
            resized_logo_path = os.path.join(temp_dir, 'resized_logo.png')
            resized_original.save(resized_logo_path)
           
            with Image.open(generated_icon_path) as generated_img:
                generated_img = generated_img.convert("RGBA")
                difference = ImageChops.difference(resized_original, generated_img)
                diff_bbox = difference.getbbox()
                if diff_bbox:
                    difference_path = os.path.join(temp_dir, 'difference.png')
                    difference.save(difference_path)
                    logging.info(f"Difference image saved to {difference_path}")
                return diff_bbox is None

    def process_icon_validation(self, platform, folder, icon_type, icon_size):
        """Complete validation process for a given icon."""
        if platform == "android":
            icon_dir = self.generated_icon_dir_android
            icon_filename = f"{icon_type}.png"
            generated_icon_path = os.path.join(icon_dir, folder, icon_filename)
        elif platform == "ios":
            icon_dir = self.generated_icon_dir_ios
            icon_filename = f"{icon_type}.png"
            generated_icon_path = os.path.join(icon_dir, icon_filename)

        validation_results = {}
        validation_results['exists'] = os.path.exists(generated_icon_path)
        validation_results['is_latest'] = self.is_latest(generated_icon_path)
        validation_results['size_matches'] = self.verify_image_size(generated_icon_path, (icon_size, icon_size))
        validation_results['content_matches'] = self.compare_images(generated_icon_path, self.logo_path, (icon_size, icon_size), icon_type)

        return validation_results