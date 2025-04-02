from stats import get_num_words, get_char_count, sort_dict
import sys

def get_book_text(file_path):
	with open(file_path) as file:
		file_contents = file.read()
		return file_contents

def main():
	if len(sys.argv) <= 1:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	
	file_path = sys.argv[1]
	text = get_book_text(file_path)
	num_words = get_num_words(text)
	char_dict = get_char_count(text)
	sorted_dict = sort_dict(char_dict)
	
	#Printing report
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {file_path}")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")

	for item in sorted_dict:
		
		if item["char"].isalpha():
			print(f"{item['char']}: {item['count']}")
	
	print("============= END ===============")
main()
