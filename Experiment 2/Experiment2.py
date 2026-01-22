import heapq

class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_tree(freq):
    priority_queue = []

    for key, val in freq.items():
        priority_queue.append(Node(key, val))

    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged_node = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]


def generate_huffman_codes(node, current_code="", codes=None):
    if codes is None:
        codes = {}
    if node is None:
        return codes

    if node.char is not None:
        codes[node.char] = current_code
        return codes

    generate_huffman_codes(node.left, current_code + "0", codes)
    generate_huffman_codes(node.right, current_code + "1", codes)
    return codes


def huffman_encoding(data):
    if not data:
        return "", None

    freq = {}
    for char in data:
        freq[char] = freq.get(char, 0) + 1

    root = huffman_tree(freq)
    codes = generate_huffman_codes(root)

    encoded_data = "".join(codes[char] for char in data)
    return encoded_data, root, codes


def huffman_decoding(encoded_data, root):
    if not encoded_data or root is None:
        return ""

    decoded_data = []
    current_node = root

    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_data.append(current_node.char)
            current_node = root
            
    return "".join(decoded_data)


string = input("Enter a string: ")

encoded_string, tree_root, codes = huffman_encoding(string)

print(f"Original string: {string}")
print(f"Encoded string: {encoded_string}")

decoded_string = huffman_decoding(encoded_string, tree_root)
print(f"Decoded string: {decoded_string}")
