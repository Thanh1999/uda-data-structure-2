# uda-data-structure-2

### Problem 1:
1. Time and space complexities: O(1) since we used key to retreive/set value from map
2. Algorithms: 
- Use dictionary data structure. 
- The "get" method takes a key as input and retrieves the value from the cache. If the key exists in the cache, it is moved to the front of the cache to mark it as the most recently used. If the key does not exist, it returns -1. 
- The "set" method takes a key-value pair as input and sets it in the cache. If the key already exists in the cache, its value is updated, it also is moved to the front of the cache to mark it as the most recently used. If the cache is at its capacity, the least recently used key-value pair is removed from the cache by popping the first item from the dictionary.

### Problem 2:
1. Time and space complexities: O(n), n is the total number of files and directories in the given directory and its subdirectories.
2. Algorithms: 
- Use recursive algorithm. 
- The find_files function uses the os.listdir method to obtain a list of items 
- For each item, it checks if it is a file by using os.path.isfile. If it is a file, it checks if the file name ends with the desired suffix. If it does, it appends the file path (path + '/' + item) to the result list.
- If the item is not a file, the function recursively calls itself with the updated path parameter, which is the current path concatenated with the current item (path + '/' + item). The function then extends the result list with the returned result from the recursive call.
- Finally, the function returns the result list

### Problem 3:
1. Time and space complexities:
- build_huffman_tree: O(n log n), n is the number of unique characters in the input data
- build_frequency_dict: O(1), set frequency value of character into map
- generate_huffman_codes: O(n), n is the number of nodes in the Huffman tree
- huffman_encoding: The big(0) of the above three funciton + O(n), n is the length of characters pass in
- huffman_decoding: O(n), n is the length of the encoded characters pass in
=> Summary: The process is dominated by the building of the Huffman tree, which is O(n log n)
2. Algorithms: 
- Use binary tree and recursive algorithm. 
- build_huffman_tree: uses a priority queue (implemented as a heap) to merge nodes with the lowest frequencies from dictinary map
- build_frequency_dict: builds a frequency dictionary by counting the occurrences of each character in the input data
- generate_huffman_codes: traverses the tree recursively and assigns binary codes to each leaf node.
- huffman_encoding: iterates over each character in the data and retrieves the corresponding Huffman code from the codes dictionary
- huffman_decoding: traverses the tree based on the bits in the encoded data and retrieves the corresponding characters

### Problem 4:
1. Time and space complexities: O(n), n is the total number of subgroups and users in the given groups and its subdgroups.
2. Algorithms: 
- Use recursive algorithm. 
- The is_user_in_group iterates over the given groups to find the user. If it does not find the users but have sub groups it will call recursively itself to find the user in each sub groups, it will return false if the user can not be found

### Problem 5:
1. Time and space complexities: the print_chain big(O) is O(n) - n is the block in the chain. The others has O(1) complexity since it just append the last block hash to be the previous hash of new block
2. Algorithms: 
- Use linked list data structure. 
- When a Block is created its hash is calculated by using the string combine of timestamp, data, previous_hash to be hash by sha-256. The BlockChain will check if the new block's previous_hash is equal the last block's hash before adding it to the chain.

### Problem 6:
1. Time and space complexities:
- The "union" big(O) is O(m + n + k), m is the total elements of list1_node, n is the total elements of list2_node, k is the total elements of the union set 
- The "intersection" big(O) is O(m + n + k), m is the total elements of list1_node, n is the total elements of list2_node, k is the total elements of the result set 
2. Algorithms: 
- Use linked list data structure. 
- The union function iterate through list1_node to add its node value to the element_set and do the same thing to list2_node. Set will remove duplicate value and then we create uninon linked list base on the element_set
- The intersection function iterate through list1_node to add its node value to the element_set then iterate through list2_node to check if its node value exists in the element_set it will be put to the result_set. Set will remove duplicate value and then we create intersection linked list base on the result_set