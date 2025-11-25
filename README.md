# File Organizer

A simple yet powerful Python script to organize your files into directories based on their file extensions.

## Features

- **Automatic Organization**: Moves files into categorized folders (Image, Video, Code, Document, Others).
- **Duplicate Handling**: Automatically renames duplicate files to prevent overwriting (e.g., `file(1).txt`).
- **Customizable**: Easily extensible mapping of file extensions to categories.
- **Test Data Generator**: Includes a script to generate dummy files for testing.

## Supported File Types

The script currently supports the following categories and extensions:

- **Image**: `.jpg`, `.jpeg`, `.bmp`, `.png`
- **Video**: `.mp4`, `.avi`, `.mov`, `.mkv`
- **Code**: `.html`, `.htm`, `.css`, `.c`, `.cpp`, `.js`, `.ts`, `.py`
- **Document**: `.csv`, `.txt`
- **Others**: Any other file extension not listed above.

## Usage

### Prerequisites

- Python 3.x installed on your system.

### Running the Organizer

Run the `file_organizer.py` script with the input directory (files to organize) and the output directory (where organized folders will be created).

```bash
python file_organizer.py <input_dir> <output_dir>
```

**Example:**

```bash
python file_organizer.py ./downloads ./organized_downloads
```

### Generating Test Files

You can use `create_files.py` to generate test files in a directory to verify the organizer's functionality.

```bash
python create_files.py <target_dir>
```

**Example:**

```bash
python create_files.py ./test_data
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
