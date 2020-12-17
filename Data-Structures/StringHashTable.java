public class StringHashTable {
	
	private String[] keys;
	private String[] values;
	private int size;
	
	// Default Constructor size 10
	public StringHashTable() {
		keys = new String[10];
		values = new String[10];
		size = 10;
	}
	
	// Non-Default Constructor when the user wants
	// to set the size of the hash table
	public StringHashTable(int N) {
		keys = new String[N];
		values = new String[N];
		size = N;
	}
	
	// Put a value into the table
	public void put(String key, String value) {
		int index = hashFunction(key);
		// If key and value already exist, update value
		if (keys[index] == key) {
			values[index] = value;
		} else {
			// If index is already taken, do linear probing to find a new one
			while (keys[index] != null) {
				index = (index + 1) % size;
			}
			// Now add key and value to the table
			keys[index] = key;
			values[index] = value;
		}
	}
	
	// Retrieves the value associated with a given key
	public String get(String key) {
		int index = hashFunction(key);
		while (keys[index] != null) {
			if (keys[index] == key) {
				return values[index];
			}
			index = (index + 1) % size;
		}
		return "No Key Found";
	}
	
	// This generates our indexes
	private int hashFunction(String key) {
		int index = 0;
		for (int i = 0; i < key.length(); i++) {
			index += (int) key.charAt(i);
		}
		return index % size;
	}
}