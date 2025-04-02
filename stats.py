def get_num_words(text):
        words = text.split()
        return len(words)

def get_char_count(text):
	char_matrix = {}

	text = text.lower()
	
	for i in text:
		if i in char_matrix:
			char_matrix[i] = char_matrix[i] + 1
		else:
			char_matrix[i] = 1
	
	char_list = [{"char": char, "count": count} for char, count in char_matrix.items()]

	return char_list

def sort_on(dict):
	return dict["count"]

def sort_dict(chars):
	chars.sort(reverse=True, key=sort_on)
	return chars
	