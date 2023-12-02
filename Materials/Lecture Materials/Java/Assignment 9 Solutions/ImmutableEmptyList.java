package it5001.collections.immutable;

import java.util.Iterator;
import java.util.function.BiFunction;
import java.util.function.Function;
import java.util.function.Predicate;

class ImmutableEmptyList<T> implements ImmutableList<T> {
    // basically just write all the base cases here
    public ImmutableList<T> reversed() { return this; }

    public T head() { return null; }

    public ImmutableList<T> tail() { return null; }

    public Iterator<T> iterator() { return new ImmutableListIterator<>(this); }

    public long size() { return 0; }

    public T reduce(BiFunction<T, T, T> f) { return null; }

    public boolean isEmpty() { return true; }

    public T get(int index) { return null; }

    public ImmutableList<T> prepended(T t) { return new ImmutableListNode<T>(t, this); }

    public ImmutableList<T> appended(T t) { return new ImmutableListNode<T>(t, this); }

    @Override
    public String toString() { return ""; }

    @Override
    public boolean equals(Object o) {
        return (o instanceof ImmutableEmptyList<?>);
    }

    public ImmutableList<T> concat(ImmutableList<T> other) { return other; }

    public <R> ImmutableList<R> map(Function<T, R> f) { return new ImmutableEmptyList<R>(); }

    public ImmutableList<T> filter(Predicate<T> f) { return this; }
}