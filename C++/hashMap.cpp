https://leetcode.com/problems/design-hashmap/
//using array method
class MyHashMap {
public:

    int data[1000001];

    MyHashMap()
    {
        //this constructor is used to initialise an array data[]
        // with size 1000001 and sets all elements to -1
        // the data[] will serve as the hash map
        for(int i=0; i<1000001; i++)
        {
            data[i] = -1;
        }
        
    }
    

    /*
    This function put()
    takes a key and value as argument, stores the value in the hash map at the position of index key. 
    */
    void put(int key, int value) 
    {
        data[key] = value;
        
    }
    
    /*
    This function get()
    takes a key as an argument and returns the value associated with the key in hash map.
    If the value is not found which means that it does not exist(array element is at index key -1), then it returns -1

    */

    int get(int key) 
    {
        if(data[key] == -1)
        {
            return -1;
        }
        return data[key];
    }
    
    /*
    This function remove()
    takes a key as an argument and removes the value associated with the key in has map.The valye is removes from the hash map by setting the array element if index key to -1
    */
    void remove(int key) 
    {
        if(data[key] != -1)
        {
            data[key] = -1;
        }
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */