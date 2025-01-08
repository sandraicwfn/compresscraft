# CompressCraft

CompressCraft is an advanced file compression tool designed for Windows. It provides a variety of compression options to reduce file sizes, making storage and transfer more efficient.

## Features

- **Multiple Compression Formats**: Compress files using different algorithms: ZIP, BZ2, or LZMA.
- **Ease of Use**: Simple command-line interface to quickly compress files.
- **Efficient Storage**: Reduce the size of files for easier storage and transfer.

## Installation

Ensure you have Python installed on your system. You can download it from the [official website](https://www.python.org/downloads/).

## Usage

Run the script from the command line. You need to specify the input file, the desired output file name, and optionally, the compression format.

```bash
python compress_craft.py <input_file> <output_file> [--format zip|bz2|lzma]
```

### Examples

- Compress a file using the default ZIP format:

  ```bash
  python compress_craft.py document.txt document.zip
  ```

- Compress a file using BZ2 format:

  ```bash
  python compress_craft.py document.txt document.bz2 --format bz2
  ```

- Compress a file using LZMA format:

  ```bash
  python compress_craft.py document.txt document.lzma --format lzma
  ```

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Thank you for using CompressCraft. We hope it makes your file management tasks easier and more efficient!