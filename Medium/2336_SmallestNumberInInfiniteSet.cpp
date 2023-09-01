#include <iostream>

class SmallestInfiniteSet {
private:
    struct Node {
    public:
        Node(int v) {
            value = v;
        }
        int value;
        struct Node* next = nullptr;
    };

    Node* root;
public:
    SmallestInfiniteSet() {
        root = new Node(1);
        Node* currNode = root;
        for (int i = 2; i <= 1000; ++i) {
            currNode->next = new Node(i);
            currNode = currNode->next;
        }
    }

    int popSmallest() {
        Node* smallest = root;
        root = root->next;
        return smallest->value;
    }

    void addBack(int num) {
        // set to this by the problem's constraints
        if (num > 1000) {
            return;
        }
        Node* prevNode = root;
        for (auto n = root;; n = n->next) {
            if (n->value == num) { return; }
            if (n == root && n->value > num) {
                Node* newNode = new Node(num);
                root = newNode;
                newNode->next = n;
                return;
            }
            if (n->value < num) {
                prevNode = n;
                continue;
            }
            Node* newNode = new Node(num);
            prevNode->next = newNode;
            newNode->next = n;
            return;
        }
    }
};

int main() {
    SmallestInfiniteSet* smallestInfiniteSet = new SmallestInfiniteSet();
    std::cout << smallestInfiniteSet->popSmallest() << std::endl;
    smallestInfiniteSet->addBack(1);
    std::cout << smallestInfiniteSet->popSmallest() << std::endl;
    std::cout << smallestInfiniteSet->popSmallest() << std::endl;
    std::cout << smallestInfiniteSet->popSmallest() << std::endl;
    smallestInfiniteSet->addBack(2);
    smallestInfiniteSet->addBack(3);
    std::cout << smallestInfiniteSet->popSmallest() << std::endl;
    std::cout << smallestInfiniteSet->popSmallest() << std::endl;
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet* obj = new SmallestInfiniteSet();
 * int param_1 = obj->popSmallest();
 * obj->addBack(num);
 */