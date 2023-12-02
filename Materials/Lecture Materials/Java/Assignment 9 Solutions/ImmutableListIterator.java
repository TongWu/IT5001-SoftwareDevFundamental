package it5001.collections.immutable;

import java.util.Iterator;

// an iterator so that ImmutableLists can be used in for loops
class ImmutableListIterator<T> implements Iterator<T> {
    private ImmutableList<T> ls;
    ImmutableListIterator(ImmutableList<T> ls) {
        this.ls = ls;
    }
    public boolean hasNext() {
        return !ls.isEmpty();
    }
    public T next() {
        T t = ls.head();
        ls = ls.tail();
        return t;
    }
}