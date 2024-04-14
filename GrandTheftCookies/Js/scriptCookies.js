const fs = require('fs');
const archiver = require('archiver');
const os = require('os');

const username = os.userInfo().username;
const directoryPath = `C:\\Users\\${username}\\AppData\\Local\\Google\\Chrome\\User Data\\Default`; // replace with your directory path

// Create a file to output the archive into
const output = fs.createWriteStream(`C:\\Users\\${username}\\Desktop\\Cookies.zip`);
const archive = archiver('zip', {
    zlib: { level: 9 } // Sets the compression level
});

// Listen for all archive data to be processed
output.on('close', function() {
    console.log(archive.pointer() + ' total bytes');
    console.log('Archiver has been finalized and the output file descriptor has closed.');
});

// Good practice to catch warnings (ie stat failures and other non-blocking errors)
archive.on('warning', function(err) {
    if (err.code === 'ENOENT') {
        // log warning
        console.warn(err);
    } else {
        // throw error
        throw err;
    }
});

// Good practice to catch this error explicitly
archive.on('error', function(err) {
    throw err;
});

// Pipe archive data to the file
archive.pipe(output);

// Append the whole directory with its original structure
archive.directory(directoryPath, false);

// Finalize the archive (ie we are done appending files but streams have to finish yet)
archive.finalize();
