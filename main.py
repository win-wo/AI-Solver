"""Main module"""
import reader
import cleaner
import process


def main():
    """Main function"""
    raw_data = reader.file_reader("data/test.tsv")
    split_data = cleaner.split_cases(raw_data)
    for entry in split_data:
        process.tagging(entry)


main()
