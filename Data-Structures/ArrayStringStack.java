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

    public void push(String item) {
        if (N == capacity) {
            resize();
        }
        stack[N++] = item;
    }

    public String pop() {
        if (N == 0) {
            return "Empty";
        } else {
            String item = stack[--N];
            stack[N] = null;
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

    private void resize() {
        String[] copy = new String[capacity * 2];
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
