#operation in a Trie
class Trie:
    head = {}
 
    #function to store String
    def add(self, word):
        #get current node from the head
        cur = self.head
 
        #iterate each character in the word
        for ch in word:
            if ch not in cur:
                #put the character as the node of the head
                cur[ch] = {}
            cur = cur[ch]
 
        # '*' denotes the Trie has this word as item
        # if '*' doesn't exist, Trie doesn't have this word but as a path to longer word
        cur['*'] = True
   
    #function to find a word in the String
    def find(self, word):
        cur = self.head
 
        for ch in word:
            #if the first character is not the same, the word does not exist
            if ch not in cur:
                return False
            cur = cur[ch]
       
        # '*' denotes the Trie has this word as item
        # if '*' doesn't exist, Trie doesn't have this word but as a path to longer word
        if '*' in cur:
            return True
        else:
            return False
   
    #function to delete
 
MyTrie = Trie()
MyTrie.add("algorisfunalgoisgreat")
print(MyTrie.find("fun"))
print(MyTrie.find("algo"))
print(MyTrie.find("algorisfunalgoisgreat"))
