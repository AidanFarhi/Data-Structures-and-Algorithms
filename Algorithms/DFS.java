package Algorithms;

public class DFS {
	
	public class Node {
		
		// Every node will have at most 3 neighbors
		private Node[] adjList = new Node[3];
		private byte adjListSize = 0;
		private int data = 0;
		private boolean visited = false; 
		
		// Non default constructor
		public Node(int data) {
			this.data = data;
		}
		
		// Getters and setters
		public int getData() { return data; }
		public void setData(int data) { this.data = data; }
		public boolean isVisited() { return visited; }
		public void setVisited(boolean visited) { this.visited = visited; }
		public byte getAdjListSize() { return adjListSize; }
		public void setAdjListSize(byte adjListSize) { this.adjListSize = adjListSize; }
		public Node[] getAdjList() { return this.adjList; }

		// Method to add node to adjList
		public void addToAdjList(Node node) {
			byte i = this.getAdjListSize();
			Node[] adjListRef = this.getAdjList();
			adjListRef[i] = node;
			i++;
			this.setAdjListSize(i);
		}
	}
	
	// Here is the DFS function
	public static void depthFirstSearch(Node startNode) {
		Node[] stack = new Node[20];
		byte stackSize = 1;
		byte stackEnd = 0;
		stack[0] = startNode;
		startNode.setVisited(true);
		while (stackSize > 0) {
			Node node = stack[stackEnd];
			System.out.println(node.getData());
			stackSize--;
			stackEnd--;
			Node[] nodeAdjList = node.getAdjList();
			for (Node n : nodeAdjList) {
				if (n != null) {
					if (!n.isVisited()) {
						n.setVisited(true);
						stack[stackSize] = n;
						stackSize++;
						stackEnd++;
					}
				}
			}	
		}
	}
	
	public static void main(String args[]) {
		// Initialize our nodes here
		DFS DFS = new DFS();
		Node node1 = DFS.new Node(100);
		Node node2 = DFS.new Node(200);
		Node node3 = DFS.new Node(300);
		Node node4 = DFS.new Node(400);
		Node node5 = DFS.new Node(500);
		Node node6 = DFS.new Node(600);
		Node node7 = DFS.new Node(700);
		Node node8 = DFS.new Node(800);
		Node node9 = DFS.new Node(900);
		Node node10 = DFS.new Node(1000);
		Node node11 = DFS.new Node(1100);
		Node node12 = DFS.new Node(1200);
		Node node13 = DFS.new Node(1300);
		Node node14 = DFS.new Node(1400);
		Node node15 = DFS.new Node(1500);
		Node node16 = DFS.new Node(1600);
		Node node17 = DFS.new Node(1700);
		
		// Now add connections
		node1.addToAdjList(node2);
		node1.addToAdjList(node3);
		node1.addToAdjList(node4);
		node2.addToAdjList(node5);
		node2.addToAdjList(node6);
		node2.addToAdjList(node7);
		node3.addToAdjList(node8);
		node4.addToAdjList(node9);
		node5.addToAdjList(node10);
		node5.addToAdjList(node11);
		node8.addToAdjList(node12);
		node8.addToAdjList(node13);
		node9.addToAdjList(node14);
		node9.addToAdjList(node15);
		node15.addToAdjList(node16);
		node15.addToAdjList(node17);
		
		/*
		 * 			- Representation of Tree -
		 * 					
		 * 						 100 
		 * 				       /  |  \
		 * 					200	 300  400
		 * 				   /  |   |   	 \
		 * 				500  600  800	  900
		 * 				/ |       / \     /  \
		 * 			1000 1100  1200 1300 1400 1500
		 * 									  /   \
		 * 									1600  1700	
		 */
		
		depthFirstSearch(node1);
	}
}
