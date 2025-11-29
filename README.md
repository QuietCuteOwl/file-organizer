# File Organizer

Effortlessly organize your files into structured folders based on their extensions.

## Features

- **GUI**: Simple interface to manage organization.
- **Automatic Sorting**: Moves files into categories like Images, Videos, Documents, etc.
- **Safe**: Handles duplicate filenames automatically.
- **Customizable**: Add or remove file mappings.

## Installation

1. Clone the repository.
2. Ensure Python 3.x is installed.

## Usage

### Graphical Interface (Recommended)

1. Run the UI script:
   ```bash
   python ui.py
   ```
2. Select your **Input Directory** (files to organize) and **Output Directory**.
3. Click **Organize**.

### Command Line Interface

Run the script with input and output directories:

```bash
python file_organizer.py <input_dir> <output_dir>
```

Example:
```bash
python file_organizer.py ./downloads ./clean_downloads
```

## Testing

You can generate dummy files to test the tool:

```bash
python create_files.py ./test_data
```

## License

MIT License. See the [LICENSE](LICENSE) file for details.
