const { execFile } = require('child_process');
const path = require('path');

const projectPath = path.resolve(__dirname, 'MaighaInc');
const iconImagePath = path.resolve(__dirname, 'logo.png');
const splashImagePath = path.resolve(__dirname, 'logo.svg');
const binaryPath = path.resolve(__dirname, 'dist', 'IconSplashLib/IconSplashLib');

const runBinary = (args, description) => {
    const child = execFile(binaryPath, args);

    const handleOutput = (data, streamType) => {
        console.log(`Hello + ${description} - ${streamType}: ${data}`);

        const progressMatch = data.match(/Progress:\s*(\d+)%\s*-\s*(.*)/);
        if (progressMatch) {
            const progress = parseInt(progressMatch[1], 10);
            const message = progressMatch[2];
            console.log(`Dude + ${description} - ${message} - Progress: ${progress}%`);
        }
    };

    child.stdout.on('data', (data) => handleOutput(data.toString(), 'Stdout'));
    child.stderr.on('data', (data) => handleOutput(data.toString(), 'Stderr'));

    child.on('close', (code) => {
        console.log(`${description} - Process exited with code ${code}`);
    });
};


// runBinary([projectPath, '--icon', iconImagePath, '--platform', 'android'], 'Icon Android Generation');


// Run the binary for generating the splash screen
runBinary([projectPath, '--splash', splashImagePath], 'Splash Screen Generation');
