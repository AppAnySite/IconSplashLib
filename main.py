import multiprocessing
import os
import logging
import sys
import click
from tqdm import tqdm  # Import tqdm for the splash screen progress bar
from utils import ProjectUtils, ConfigLoader, setup_logging, ServiceLocator
from plugins.icon_generator.commands import GenerateIconsCommand, ReplaceFilesCommand
from plugins.splash_screen_generator.commands import (
    GenerateBootsplashCommand, 
    CustomizeIOSBootsplashCommand, 
    CustomizeAndroidBootsplashCommand, 
    InstallPodsCommand, 
    ModifyAppTSXCommand
)

@click.command(context_settings=dict(ignore_unknown_options=True))
@click.argument('project_path', type=click.Path(), required=False)
@click.option('--icon', type=click.Path(exists=True), help='Path to the icon image')
@click.option('--splash', type=click.Path(exists=True), help='Path to the splash screen image')
@click.option('--platform', type=click.Choice(['android', 'ios'], case_sensitive=False), help='Specify the platform (android or ios)')
@click.option('--folder', type=str, multiple=True, help='Specific folders to generate icons for (e.g., mipmap-mdpi, AppIcon-20x20@2x). Can be specified multiple times.')
@click.option('--icon-type', type=str, help='Specify the type of icon to generate (e.g., foreground, round, launcher)')
@click.option('--config', type=click.Path(exists=True), help='Path to a custom configuration file')
@click.option('--dev', is_flag=True, help='Enable tqdm progress bar for splash screen development')
def main(project_path, icon, splash, platform, folder, icon_type, config, dev):
    setup_logging()

    # Define the steps and their progress weight for splash screen
    steps = [
        ('Installing Dependencies', 10),
        ('Generating Bootsplash', 30),
        ('Customizing iOS Bootsplash', 20),
        ('Customizing Android Styles', 15),
        ('Customizing Android Manifest', 10),
        ('Customizing Android MainActivity', 10),
        ('Modifying App.tsx', 15),
        ('Installing Pods', 20)
    ]
    total_steps_weight = sum(weight for _, weight in steps)
    current_progress = 0

    def progress_callback(progress, message):
        if dev:
            progress_bar.set_description(f"Progress: {progress}% - {message}")
            progress_bar.update(progress - current_progress)
        else:
            print(f"Progress: {progress}% - {message}")
        sys.stdout.flush()

    def update_progress(message, step_weight):
        nonlocal current_progress
        current_progress += step_weight
        if dev:
            progress_bar.update(step_weight)
            progress_bar.set_description(f"Progress: {current_progress}% - {message}")
        else:
            print(f"Progress: {current_progress}% - {message}")
        sys.stdout.flush()  # Ensure immediate flushing of stdout

    if not icon and not splash:
        logging.error("You must provide either --icon or --splash argument")
        return

    project_path = os.path.expanduser(project_path or "output")
    if not os.path.exists(project_path):
        os.makedirs(project_path)

    ios_path = os.path.join(project_path, "ios")
    project_name = None
    if os.path.exists(ios_path):
        project_name = ProjectUtils.find_ios_project_name(ios_path)
        if not project_name:
            logging.error("iOS project name not found")
            return

    if config:
        icon_config = ConfigLoader.load_config(config)
    else:
        if platform == 'android':
            icon_config = ConfigLoader.load_config('config/android_config.json')
        elif platform == 'ios':
            icon_config = ConfigLoader.load_config('config/ios_config.json')
        else:
            icon_config = ConfigLoader.load_config('config/default_config.json')

    if 'icon_sizes' not in icon_config:
        logging.error("The configuration file does not contain 'icon_sizes'")
        return

    try:
        splash_config = ConfigLoader.load_config('config/splash_config.json')
    except FileNotFoundError:
        logging.error("splash_config.json not found. Please provide the correct path to the splash configuration file.")
        return

    ServiceLocator.register(GenerateIconsCommand, GenerateIconsCommand)
    ServiceLocator.register(ReplaceFilesCommand, ReplaceFilesCommand)
    ServiceLocator.register(GenerateBootsplashCommand, GenerateBootsplashCommand)
    ServiceLocator.register(CustomizeIOSBootsplashCommand, CustomizeIOSBootsplashCommand)
    ServiceLocator.register(CustomizeAndroidBootsplashCommand, CustomizeAndroidBootsplashCommand)
    ServiceLocator.register(InstallPodsCommand, InstallPodsCommand)
    ServiceLocator.register(ModifyAppTSXCommand, ModifyAppTSXCommand)

    commands = []

    # Handle Icon Generation with progress callback
    if icon:
        if platform == 'android':
            android_output_directory = os.path.join(project_path, 'icons/android')
            os.makedirs(android_output_directory, exist_ok=True)
            generate_icons_command = ServiceLocator.resolve(GenerateIconsCommand)(
                'android', icon, android_output_directory, icon_config, None, folder, icon_type
            )
            generate_icons_command.set_progress_callback(progress_callback)
            generate_icons_command.use_tqdm = dev  # This will be ignored for icons
            commands.append(generate_icons_command)

            if project_path != "output":
                replace_files_command = ServiceLocator.resolve(ReplaceFilesCommand)(
                    'android', project_path, android_output_directory
                )
                replace_files_command.set_progress_callback(progress_callback)
                commands.append(replace_files_command)

        elif platform == 'ios':
            ios_output_directory = os.path.join(project_path, 'icons/ios')
            os.makedirs(ios_output_directory, exist_ok=True)
            generate_icons_command = ServiceLocator.resolve(GenerateIconsCommand)(
                'ios', icon, ios_output_directory, icon_config, None, folder, icon_type
            )
            generate_icons_command.set_progress_callback(progress_callback)
            generate_icons_command.use_tqdm = dev  # This will be ignored for icons
            commands.append(generate_icons_command)

            if project_path != "output" and project_name:
                replace_files_command = ServiceLocator.resolve(ReplaceFilesCommand)(
                    'ios', project_path, ios_output_directory, project_name
                )
                replace_files_command.set_progress_callback(progress_callback)
                commands.append(replace_files_command)

    # Handle Splash Screen with TQDM
    with tqdm(total=total_steps_weight, ncols=100, disable=not dev) as progress_bar:
        if splash and project_path != "output":
            splash_output_directory = project_path

            # Common Steps
            update_progress('Installing Dependencies', 10)

            generate_bootsplash_command = ServiceLocator.resolve(GenerateBootsplashCommand)(
                splash_output_directory, splash
            )
            generate_bootsplash_command.execute()
            update_progress('Generating Bootsplash', 30)

            # Platform-Specific Steps
            if platform == 'ios':
                ios_path = os.path.join(splash_output_directory, "ios", project_name)
                customize_ios_bootsplash_command = ServiceLocator.resolve(CustomizeIOSBootsplashCommand)(
                    ios_path, project_name
                )
                customize_ios_bootsplash_command.execute()
                update_progress('Customizing iOS Bootsplash', 20)

                install_pods_command = ServiceLocator.resolve(InstallPodsCommand)()
                install_pods_command.execute()
                update_progress('Installing Pods', 20)

            elif platform == 'android':
                android_path = os.path.join(splash_output_directory, "android")
                customize_android_bootsplash_command = ServiceLocator.resolve(CustomizeAndroidBootsplashCommand)(
                    android_path, project_name
                )
                customize_android_bootsplash_command.execute()
                update_progress('Customizing Android Styles', 15)
                update_progress('Customizing Android Manifest', 10)
                update_progress('Customizing Android MainActivity', 10)

            # Modify App.tsx (common step)
            app_tsx_path = os.path.join(splash_output_directory, "App.tsx")
            modify_app_tsx_command = ServiceLocator.resolve(ModifyAppTSXCommand)(
                app_tsx_path
            )
            modify_app_tsx_command.execute()
            update_progress('Modifying App.tsx', 15)
        if dev:
            progress_bar.n = total_steps_weight
            progress_bar.set_description("Progress: 100% - Completed")
            progress_bar.update(0)
        else:
            print("Progress: 100% - Completed")



    # Execute all commands
    for command in commands:
        try:
            command.execute()
        except Exception as e:
            logging.error(f"Command {command} failed with error: {e}")

    if project_path == "output":
        logging.info(f"Icons generated in output directory: {project_path}")
        logging.info(f"For keeping project you should add project path also.")

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
