from friendsbalt.acs import MinPQ


class HuffmanEncoding:
    def __init__(self, src=None, encoded_text=None, root=None):

        self.text = src
        self.encoded_text = encoded_text
        self.root = root

        if src is None:
            self.decoding()

        else:
            self.build_tree()
            self.encoding()


        """
        Initializes a new Huffman Encoding. Either source text or encoded text and root must be provided.
        If source text is provided, it builds the Huffman tree and dictionary, and encodes the text.
        If encoded text and root are provided, it decodes the text.
        Args:
            src (str, optional): The source text to be encoded.
            encoded_text (str, optional): The encoded text to be decoded.
            root (Node, optional): The root node of the Huffman tree for decoding.
        """
        pass
    
    def build_tree(self):
        leaderboard = {}
        for i in self.text:
            if i not in leaderboard:
                leaderboard[i] = 1
            else:
                leaderboard[i] += 1
        print(leaderboard)
        pq = MinPQ()
        for i in leaderboard:
            node = self.Node(leaderboard[i], char=i)
            pq.insert(node.freq, node)
        while pq.size() > 1:
            child1 = pq.del_min() 
            child2 = pq.del_min()
            root = self.Node((child1.freq + child2.freq), left=child1, right=child2)
            pq.insert(root.freq, root)
        self.root = pq.del_min()



    class Node:
        def __init__(self, freq, char=None, left=None, right=None):
            self.char = char
            self.freq = freq
            self.left = left
            self.right = right
        
        def is_leaf(self):
            return self.char is not None

    def encoding(self):

        huffman_dict = self._build_dictionary()
        print(huffman_dict)
        encoded_text = ""
        for i in self.text:
            encoded_text += huffman_dict[i]
        print(encoded_text)
        return encoded_text

        """
        Returns the encoded text.
        Returns:
            str: The encoded text as a string of 0s and 1s.
        """

    def decoding(self):

        decoded_text = ""
        current_node = self.root
        for i in self.encoded_text:
            if i == "0":
                current_node = current_node.left
            else:
                current_node = current_node.right
            if current_node.is_leaf():
                decoded_text += current_node.char
                current_node = self.root
        print(decoded_text)
        return decoded_text

        """
        Returns the original source text.
        Returns:
            str: The original source text.
        """

    def root(self): # not quite sure what to do with this but it seems to work without it
        # ok actually I think I do know how I could implement this but don't see how it's
        # that advantageous especially because I would have to modify  _build_dictionary
        # and we're not supposed to do that
        
        """
        Returns the root node of the Huffman tree.
        Returns:
            Node: The root node of the Huffman tree.
        """
        return self._root
    
    def _build_dictionary(self, node=None, prefix=''):
        """
        Recursively builds a dictionary that maps characters to their corresponding
        Huffman codes based on the Huffman tree.
        Args:
            node (Node, optional): The current node in the Huffman tree. Defaults to None,
            which means the function will start from the root node.
            prefix (str, optional): The current Huffman code prefix. Defaults to an empty string.
        Returns:
            dict: A dictionary where keys are characters and values are their corresponding
                  Huffman codes.
        """
        if node is None:
            node = self.root
        
        if node.char is not None:
            return {node.char: prefix}
        
        dictionary = {}
        dictionary.update(self._build_dictionary(node.left, prefix + '0'))
        dictionary.update(self._build_dictionary(node.right, prefix + '1'))
        return dictionary

encoding = HuffmanEncoding(src="grud is very very numpy")
decoding = HuffmanEncoding(encoded_text="0010100110101001110111001101111100000100101111110000010010111101011101011110011101", root=encoding.root)

