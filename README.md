#  LucidaTrackDownloader

A Python script that automates high-quality music search and download from [lucida.su](https://lucida.su) and instantly plays it using VLC.

---

##  DISCLAIMER

This tool interacts with a **third-party website (lucida.su)** that may host copyrighted or premium content.  
**Use at your own risk.** The author is **not responsible** for any misuse or legal consequences.  
Ensure your usage complies with all **local laws** and **platform terms of service**.

---

##  Features

- Automates search and download of `.flac` music files from **lucida.su**
- Uses **Qobuz** as the music source
- Automatically waits for the download to finish
- Launches VLC to play the downloaded track

---

##  Requirements

- Python 3.7+
- VLC media player installed (default path: `C:\Program Files\VideoLAN\VLC\vlc.exe`)
- Google Chrome installed
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) matching your Chrome version

Install dependencies:

```bash
pip install selenium
````

---

##  Configuration

Edit the script if needed:

```python
DOWNLOAD_DIR = r"Enter your preferred download location"  # Set to your preferred download folder
vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"  # Ensure VLC path is correct
```

Ensure:

* VLC is installed in the expected path
* You have a compatible ChromeDriver in your PATH or same folder

---

##  How to Use

1. Make sure `chromedriver.exe` is available and Chrome is installed.
2. Run the script:

```bash
python lucida.py
```

3. Enter a song name when prompted.
4. The script:

   * Searches for the song on `lucida.su`
   * Selects the **Qobuz** service
   * Downloads the `.flac` file
   * Plays it using VLC media player

---

##  License

This project is for **educational** or **personal** use only.
It is **not affiliated with lucida.su, Qobuz, or VLC**.
Use responsibly.

