const { execFile } = require('child_process');
const path = require('path');
const express = require('express');
const multer = require('multer');
const app = express();
const http = require('http').Server(app);
const io = require('socket.io')(http);

// Set up multer for file uploads
const upload = multer({ dest: 'uploads/' });

app.use(express.static(__dirname));

// Upload endpoint
app.post('/upload', upload.single('file'), (req, res) => {
    console.log('Received file upload request:', req.file);
    if (!req.file) {
        return res.json({ success: false });
    }

    // Respond with the file path
    const filePath = path.join(__dirname, req.file.path);
    console.log('File uploaded successfully. File path:', filePath);
    res.json({ success: true, filePath });
});

io.on('connection', (socket) => {
    console.log('Client connected');

    socket.on('startIconGeneration', (data) => {
        console.log('Received request to start icon generation with data:', data);
        let args = [];

        // Add project path as positional argument
        args.push(toUnixPath(data.projectPath));

        if (data.platform === 'android' || data.platform === 'ios') {
            if (data.iconPath) {
                args.push('--icon', toUnixPath(data.iconPath), '--platform', data.platform);

                if (data.folder) {
                    args.push('--folder', data.folder);
                }

                if (data.iconType) {
                    args.push('--icon-type', data.iconType);
                }
            }
        } else if (data.platform === 'splash') {
            if (data.splashPath) {
                args.push('--splash', toUnixPath(data.splashPath));
            }
        }

        console.log('Arguments for binary:', args);
        runBinary(args, socket);
    });

    socket.on('disconnect', () => {
        console.log('Client disconnected');
    });
});

const runBinary = (args, socket) => {
    // Define the binary path and ensure it's in the correct format
    const binaryPath = path.join(__dirname, 'dist', 'IconSplashLib', 'IconSplashLib.exe');
    const unixBinaryPath = toUnixPath(binaryPath);

    // Create the full command to be executed
    const command = `"${unixBinaryPath}" ${args.map(arg => `"${arg}"`).join(' ')}`;

    console.log('Command to be executed:', command);

    // Execute the command with execFile
    const child = execFile(unixBinaryPath, args, (error, stdout, stderr) => {
        if (error) {
            console.error('Execution failed:', error.message);
            socket.emit('generationComplete', 1);
            return;
        }

        console.log('Execution output:', stdout);
        stdout.split('\n').forEach((line) => {
            const progressMatch = line.match(/Progress:\s*(\d+)%/);
            if (progressMatch) {
                const progress = parseInt(progressMatch[1], 10);
                console.log('Progress:', progress);
                socket.emit('progressUpdate', progress);
            }
        });

        socket.emit('generationComplete', 0);
    });

    child.stderr.on('data', (data) => {
        console.error('Binary stderr:', data.toString());
    });
};


const toUnixPath = (windowsPath) => windowsPath ? windowsPath.replace(/\\/g, '/') : null;

const port = process.env.PORT || 3000;
http.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
