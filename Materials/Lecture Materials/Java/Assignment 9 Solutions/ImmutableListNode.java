package it5001.collections.immutable;

import java.util.Iterator;
import java.util.function.BiFunction;
import java.util.function.Function;
import java.util.function.Predicate;

class ImmutableListNode<T> implements ImmutableList<T> {
    // the element in this ImmutableListNode
    private final T h;
    // the reference to the next part of the list
    private final ImmutableList<T> t;

    ImmutableListNode(T head, ImmutableList<T> tail) {
        h = head;
        t = tail;
    }

    public T get(int index) {
        // prevent infinite recursion
        if (index < 0)
            return null;
        // return the head element
        if (index == 0)
            return h;
        // recursive call
        return t.get(index - 1);
    }

    public Iterator<T> iterator() {
        // simply return an iterator over this list
        return new ImmutableListIterator<>(this);
    }
    public long size() {
        // size of the tail + 1
        return t.size() + 1;
    }
    
    public T head() {
        // the element in this ImmutableListNode
        return h;
    }

    public ImmutableList<T> tail() {
        // the reference to the next part of the list
        return t;
    }

    // this ImmutableListNode has some value so its obviously not empty
    public boolean isEmpty() { return false; }


    public ImmutableList<T> prepended(T t) {
        // create a new ImmutableListNode containing t who points to this list
        return new ImmutableListNode<T>(t, this);
    }

    public ImmutableList<T> appended(T t) {
        // copy this ImmutableListNode and append to next
        return new ImmutableListNode<T>(h, this.t.appended(t));
    }
    
    public ImmutableList<T> concat(ImmutableList<T> other) {
        // concat the tail with other, then prepend head to it
        return t.concat(other).prepended(h);
    }

    public <R> ImmutableList<R> map(Function<T, R> f) {
        // pass in the head to f, then map the tail
        return new ImmutableListNode<R>(f.apply(h), t.map(f));
    }

    public ImmutableList<T> filter(Predicate<T> f) {
        if (f.test(h))
            // head passes the test, just filter tail
            return new ImmutableListNode<T>(h, t.filter(f));
        // head fails the test, remove head and filter tail
        return t.filter(f);
    }

    public T reduce(BiFunction<T, T, T> f) {
        if (t.isEmpty())
            // base case
            return h;
        // prepend f(head, tail.head) onto tail.tail and reduce further
        return t.tail().prepended(f.apply(h, t.head())).reduce(f);
    }

    public ImmutableList<T> reversed() {
        // prepend the elements from front to back
        ImmutableList<T> res = new ImmutableEmptyList<>();
        for (T i : this) {
            res = res.prepended(i);
        }
        return res;
    }

    @Override
    public boolean equals(Object o) {
        return (o instanceof ImmutableListNode<?>) &&
            h.equals(((ImmutableListNode<?>) o).head()) &&
            t.equals(((ImmutableListNode<?>) o).tail());
    }

    @Override
    public String toString() {
        if (t.isEmpty()) return h.toString();
        return String.format("%s : %s", h, t);
    }
}