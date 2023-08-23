
//Using chaining method to solve the hashing collision
//define the structure of node for the linked list
type node struct 
{
    key     int
    val     int
    next    *node
}
//define the structure of hashmap with array to store linked list
type MyHashMap struct 
{
    size int
	arr []*node
}

func Constructor() MyHashMap 
{
    return MyHashMap {size: 1000,
        arr: make([]*node, 1000),
    }
}

func (this *MyHashMap) Put(key int, value int)  {
    //% is to find the position in the array aka --> index
    position := key % this.size
   
   //Create a new node with key and value
    newNode := &node 
    {
        key: key,
        val: value,
        next: nil,
    }
    
    //Check if the current position is empty
    //if true, then assign it to newNode 
    // and return
    if this.arr[position] == nil 
    {
        this.arr[position] = newNode
        return
    }
    
    //Check if the new key exist or not
    //Iterate through the chaining 
    //Check if the key matches, if yes then replace the old value with newValue
    head := this.arr[position]

    for head != nil {
        if head.key == key 
	{
            head.val = value
            return
        }

        head = head.next
    }
	
    //if new key does not exist in map
    //insert the new key to the head of the linked list
    //head but not tail as the time complexity of head O(1) while tail is O(n)
    newNode.next = this.arr[position]
    this.arr[position] = newNode
}

func (this *MyHashMap) Get(key int) int 
{
    position := key % this.size
    head := this.arr[position]
    
    //Loop thru the whole linked list 
    //Check if key matched, if yes return value, else return -1
    for head != nil 
	{
        if head.key == key 
	{
            return head.val    
        }
        
        head = head.next
    }
    
    return -1
}

func (this *MyHashMap) Remove(key int) 
{
    //Look for the position to remove
    position := key % this.size
    head := this.arr[position]
    
    // position is empty(key does not exist in the map) 
    if head == nil
    {
        return
    }
       
    //check key is the head of the linked list or not
    //if yes, update the  arr[position] to the next value of head
    if head.key == key 
    {
        head = head.next
        this.arr[position] = head
        return
    }
    
    var prev *node
    
    for head != nil
    {
        if head.key == key 
	{
            prev.next = head.next
            return
        }
        
        prev = head
        head = head.next
    }
}


/**
 * Your MyHashMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Put(key,value);
 * param_2 := obj.Get(key);
 * obj.Remove(key);
 */
