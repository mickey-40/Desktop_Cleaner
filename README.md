# Desktop Cleaner

## Overview

**Desktop Cleaner** is a Python-based utility that monitors a designated download directory and automatically moves image files (such as `.jpg`, `.png`, `.gif`, etc.) to a specified folder, helping to keep your download folder clutter-free. It continuously runs in the background and moves image files as soon as they are detected.

## Features

- Automatically monitors the specified download directory.
- Moves image files (e.g., `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, etc.) to a designated folder.
- Lightweight and simple to configure.
- Customizable download and destination directories.

## Prerequisites

To run **Desktop Cleaner**, ensure you have the following:

- Python 3.x installed.
- The following Python libraries installed:
  - `os`
  - `shutil`
  - `time`
  - `watchdog` (for monitoring the directory)

You can install `watchdog` via pip:

```bash
pip install watchdog
```

## Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/DesktopCleaner.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd DesktopCleaner
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configuration:**

   Modify the Python script (`desktop_cleaner.py`) to set your download directory and destination folder for image files.

   ```python
   DOWNLOAD_DIRECTORY = 'path/to/your/download/directory'
   IMAGE_DESTINATION = 'path/to/your/destination/folder'
   ```

## Usage

1. **Run the script:**

   Simply execute the script to start monitoring your download directory.

   ```bash
   python desktop_cleaner.py
   ```

2. **Background Execution (Optional):**

   To run the script in the background, you can use tools like `nohup` on Linux or `Task Scheduler` on Windows.

   Example for running in the background on Linux:

   ```bash
   nohup python desktop_cleaner.py &
   ```

## Supported File Types

The program automatically moves the following image file types:

- `.jpg`
- `.jpeg`
- `.png`
- `.gif`
- `.bmp`
- `.tiff`

You can customize the file types by modifying the list of extensions in the script.

## Contributing

Feel free to contribute to this project by submitting a pull request. Whether it’s a bug fix, feature request, or new feature, all contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions, feel free to open an issue or contact the repository owner at `youremail@example.com`.

---

This structure should cover all the basic details needed in a typical `README.md`. Feel free to customize it based on your project specifics.
