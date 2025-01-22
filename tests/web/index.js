const { execFile } = require('child_process');
const path = require('path');
const express = require('express');
const app = express();
const http = require('http').Server(app);
const io = require('socket.io')(http);

const projectPath = path.resolve(__dirname, 'MaighaInc');
const iconImagePath = path.resolve(__dirname, 'logo.png');
const splashImagePath = path.resolve(__dirname, 'logo.svg');
const binaryPath = path.resolve(__dirname, 'dist', 'IconSplashLib/IconSplashLib');

console.log(projectPath);
console.log(iconImagePath);
console.log(binaryPath);

// Serve static files (like the HTML page)
app.use(express.static(__dirname));

io.on('connection', (socket) => {
    console.log('Client connected');

    socket.on('startIconGeneration', (platform) => {
        let args = [projectPath];
        if (platform === 'android' || platform === 'ios') {
            args.push('--icon', iconImagePath, '--platform', platform);
        } else if (platform === 'splash') {
            args.push('--splash', splashImagePath);
        }
        runBinary(args, socket);
    });

    socket.on('disconnect', () => {
        console.log('Client disconnected');
    });
});

const runBinary = (args, socket) => {
    const child = execFile(binaryPath, args);

    const handleOutput = (data) => {
        const progressMatch = data.match(/Progress:\s*(\d+)%\s*-\s*(.*)/);
        if (progressMatch) {
            const progress = parseInt(progressMatch[1], 10);
            socket.emit('progressUpdate', progress);
        }
    };

    child.stdout.on('data', (data) => handleOutput(data.toString()));
    child.stderr.on('data', (data) => handleOutput(data.toString()));

    child.on('close', (code) => {
        socket.emit('generationComplete', code);
    });
};

http.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});
