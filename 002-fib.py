    int fib(int N) {
        int curr = 0; 
        int next = 1;
        for (int i = 0; i < N; i++) {
            int next_next = curr + next;
            curr = next;
            next = next_next;
        }
        return curr;
    }
