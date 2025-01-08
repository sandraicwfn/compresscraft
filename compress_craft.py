import os
import zipfile
import bz2
import lzma
import argparse

def compress_file_zip(input_file, output_file):
    """Compress a file using ZIP format."""
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(input_file, os.path.basename(input_file))
    print(f"File '{input_file}' compressed as ZIP to '{output_file}'.")

def compress_file_bz2(input_file, output_file):
    """Compress a file using BZ2 format."""
    with open(input_file, 'rb') as fin, bz2.open(output_file, 'wb') as fout:
        fout.writelines(fin)
    print(f"File '{input_file}' compressed as BZ2 to '{output_file}'.")

def compress_file_lzma(input_file, output_file):
    """Compress a file using LZMA format."""
    with open(input_file, 'rb') as fin, lzma.open(output_file, 'wb') as fout:
        fout.writelines(fin)
    print(f"File '{input_file}' compressed as LZMA to '{output_file}'.")

def main():
    parser = argparse.ArgumentParser(description="CompressCraft: Advanced file compression tool")
    parser.add_argument('input_file', help="The file to compress")
    parser.add_argument('output_file', help="The output file name")
    parser.add_argument('--format', choices=['zip', 'bz2', 'lzma'], default='zip', help="Compression format (default: zip)")
    
    args = parser.parse_args()
    
    if args.format == 'zip':
        compress_file_zip(args.input_file, args.output_file)
    elif args.format == 'bz2':
        compress_file_bz2(args.input_file, args.output_file)
    elif args.format == 'lzma':
        compress_file_lzma(args.input_file, args.output_file)
    else:
        print("Unsupported format specified.")

if __name__ == "__main__":
    main()