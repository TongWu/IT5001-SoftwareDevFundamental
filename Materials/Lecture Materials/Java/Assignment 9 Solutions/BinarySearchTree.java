import it5001.collections.immutable.ImmutableList;

// T must extends Comparable<? super T> so that we can determine if
// an element belongs in the left or right subtree via comparison 
public class BinarySearchTree<T extends Comparable<? super T>> {

    // PART 1: determine if some element t is in the BST.
    public boolean contains(T t) {
        if (value == null) return false; // tree is empty
        if (t.equals(value)) return true; // t is the root
        if (t.compareTo(value) < 0)
            // t < value so search the left subtree
            return left.contains(t);
        // t >= value so search the right subtree
        else return right.contains(t);
    }

    // PART 2: return the in-order traversal of the BST as an ImmutableList<T>
    public ImmutableList<T> inorder() {
        if (value == null)
            // tree is empty, return an empty list
            return ImmutableList.empty();
        // left inorder + [root] + right inorder
        return left.inorder().concat(right.inorder().prepended(value));
    }

    // PART 3: sort some Iterable<T> using the BST, returning the resulting sorted list as an
    // ImmutableList<T>
    public static <T extends Comparable<? super T>> ImmutableList<T> sorted(Iterable<? extends T> ls) {
        // create empty BST
        BinarySearchTree<T> bst = new BinarySearchTree<>();
        // add everything in ls into bst
        bst.addAll(ls);
        // return its inorder
        return bst.inorder();
    }

    ////////// DO NOT EDIT THE CODE BELOW, but feel free to use them //////////

    // value is the root value
    private T value;
    // the left subtree
    private BinarySearchTree<T> left;
    // the right subtree
    private BinarySearchTree<T> right;

    // when this tree has a root value, left and right are also BSTs
    public BinarySearchTree(T rootValue) {
        value = rootValue;
        left = new BinarySearchTree<>();
        right = new BinarySearchTree<>();
    }

    // when this tree does not have a root value, left and right
    // are assigned as null. effectively, if value is null, left and right
    // are also null (making this BST empty).
    // if value is not null, then left and right are BSTs
    //
    // this constructor is private, but feel free to call it within
    // this class (you can see it being used above)
    private BinarySearchTree() { }

    // adds an element into the BST
    public void add(T t) {
        if (value == null) {
            // the tree is empty, so just add t as the root value
            value = t;
            // initialize left and right as empty BSTs
            left = new BinarySearchTree<>();
            right = new BinarySearchTree<>();
        }
        else if (t.compareTo(value) < 0)
            // t < value, so add t to the left subtree
            left.add(t);
        else
            // t >= value, so add t to the right subtree
            right.add(t);
    }

    // adds all elements in the iterable to this BST
    public final void addAll(Iterable<? extends T> it) {
        for (T t : it) {
            add(t);
        }
    }
}