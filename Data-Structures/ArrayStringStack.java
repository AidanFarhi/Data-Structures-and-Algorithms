import java.util.Arrays;

public class ArrayStringStack {
    
    private String[] stack;
    private int N;
    private int capacity;

    // Constructor - Default size 16
    public ArrayStringStack() {
        capacity = 16;
        stack = new String[16];
        N = 0;
    }

    // Double array size when array is full
    public void push(String item) {
        if (N == capacity) {
            resize(capacity * 2);
        }
        stack[N++] = item;
    }

    // Halve array size when array is 1/4 full
    public String pop() {
        if (N == 0) {
            return "Empty";
        } else {

            String item = stack[--N];
            stack[N] = null;
            if (N > 0 && N == capacity / 4) {
                resize(capacity / 2);
            }
            return item;
        }
    }

    public String[] showStack() {
        String[] result = new String[N];
        for (int i = 0; i < N; i++) {
            result[i] = stack[i];
        }
        return result;
    }

    private void resize(int newCapacity) {
        String[] copy = new String[newCapacity];
        for (int i = 0; i < N; i++) {
            copy[i] = stack[i];
        }
        stack = copy;
    }

    public static void main(String[] args) {
        ArrayStringStack AST = new ArrayStringStack();
        AST.push("First Item");
        AST.push("Second Item");
        AST.push("Third Item");
        AST.push("Fourth Item");
        AST.push("Fifth Item");
        System.out.println(Arrays.toString(AST.showStack()));
        System.out.println(AST.pop());
        AST.pop();
        System.out.println(Arrays.toString(AST.showStack()));
    } 
}
