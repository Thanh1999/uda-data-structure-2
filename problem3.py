import sys
import heapq

class Node(object):
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


def build_huffman_tree(frequency_dict):
    priority_queue = []
    if(len(frequency_dict) != 0):
        for char, freq in frequency_dict.items():
            heapq.heappush(priority_queue, (freq, Node(char, freq)))

        while len(priority_queue) > 1:
            freq1, node1 = heapq.heappop(priority_queue)
            freq2, node2 = heapq.heappop(priority_queue)
            combined_freq = freq1 + freq2
            combined_node = Node(None, combined_freq)
            combined_node.left = node1
            combined_node.right = node2
            heapq.heappush(priority_queue, (combined_freq, combined_node))

        return priority_queue[0][1]

def build_frequency_dict(data):
    frequency_dict = {}
    for char in data:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

    return frequency_dict

def generate_huffman_codes(root):
    huffman_codes = {}
    if root != None:
        def traverse(node, code):
            if node.character:
                huffman_codes[node.character] = code
            else:
                traverse(node.left, code + '0')
                traverse(node.right, code + '1')

        traverse(root, '')
    return huffman_codes


def huffman_encoding(data):
    encoded_data = ''
    if data != None:
        frequency_dict = build_frequency_dict(data)
        huffman_tree = build_huffman_tree(frequency_dict)
        huffman_codes = generate_huffman_codes(huffman_tree)

        for char in data:
            encoded_data += huffman_codes[char]

        return encoded_data, huffman_tree

def huffman_decoding(data,tree):
    decoded_data = ''
    current_node = tree

    for bit in data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.character:
            decoded_data += current_node.character
            current_node = tree

    return decoded_data

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1 - encode/decode a string has value
encoded_data, tree = huffman_encoding('ABBA')
assert encoded_data == '0110'
assert tree.frequency == 4
decoded_data = huffman_decoding(encoded_data, tree)
assert decoded_data == 'ABBA'

## Test Case 2 - encode an empty string
encoded_data, tree = huffman_encoding('')
assert encoded_data == ''
assert tree == None

## Test Case 3 - encode None object
assert None == huffman_encoding(None)