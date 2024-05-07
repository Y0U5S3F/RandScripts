const express = require('express');
const ytdl = require('ytdl-core');
const ffmpeg = require('fluent-ffmpeg');
const path = require('path');
const app = express();

// Serve static files from the "public" directory
app.use(express.static(path.join(__dirname, 'public')));

app.use(express.json()); // for parsing application/json

app.post('/download', async (req, res) => {
    let url = req.body.url;
    if (!ytdl.validateURL(url)) {
        return res.sendStatus(400);
    }

    let title = 'output';

    try {
        let info = await ytdl.getInfo(url);
        title = info.videoDetails.title.replace(/[^a-zA-Z ]/g, "");
    } catch (e) {
        console.error(e);
    }

    res.header('Content-Disposition', `attachment; filename="${title}.mp3"`);

    ffmpeg(ytdl(url))
        .audioBitrate(128)
        .format('mp3')
        .pipe(res);
});

const port = 3000;
app.listen(port, () => console.log(`Server is running on port ${port}`));