import os
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DOWNLOAD_DIR = r"Assign a download directory here"

def wait_for_download(folder, timeout=60):
    print("Waiting for download to complete...")
    elapsed = 0
    while elapsed < timeout:
        files = [f for f in os.listdir(folder) if f.endswith('.flac')]
        downloading = any(f.endswith('.crdownload') for f in os.listdir(folder))

        if files and not downloading:
            # Get the newest .flac file
            latest = max([os.path.join(folder, f) for f in files], key=os.path.getctime)
            return latest

        time.sleep(1)
        elapsed += 1

    raise Exception("Download timed out")


def play_with_vlc(path):
    print("Playing with VLC...")
    vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
    subprocess.run([vlc_path, "--play-and-exit", path])

def main():
    song_name = input("Enter the song name: ")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless=new")
    prefs = {
        "download.default_directory": DOWNLOAD_DIR,
        "download.prompt_for_download": False,
        "directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://lucida.su")

    print("Opening lucida.su...")
    time.sleep(2)

    search_bar = driver.find_element(By.ID, "download")
    search_bar.send_keys(song_name)

    service_select = Select(driver.find_element(By.ID, "service"))
    service_select.select_by_value("qobuz")

    driver.find_element(By.ID, "go").click()

    print("Searching for song...")
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        headers = driver.find_elements(By.TAG_NAME, "h1")
        a=0
        for header in headers:
            a+=1 
            if a==2:
                header.click()
        
        print("Song page loaded.")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "download-button"))
        )

        download_button = driver.find_element(By.CLASS_NAME, "download-button")
        download_button.click()
        print("Downloading track...")

        latest = wait_for_download(DOWNLOAD_DIR)
        print(f"Downloaded: {latest}")

        print("Playing with VLC...")
        while True:
            for i in os.listdir(DOWNLOAD_DIR):
                if ".crdownload" in i:
                    time.sleep(0.5)
                    
        play_with_vlc(latest)

    except Exception as e:
        print("Error during search or download:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
