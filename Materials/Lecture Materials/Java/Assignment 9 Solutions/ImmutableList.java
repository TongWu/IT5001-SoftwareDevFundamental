package it5001.collections.immutable;

import java.util.function.BiFunction;
import java.util.function.Function;
import java.util.function.Predicate;

/**
 * Represents an immutable list.
 * <p>
 * List creation:
 * </p>
 * <pre>
 * jshell&gt; ImmutableList&lt;String&gt; ls = ImmutableList.of("A", "B", "C", "D")
 * ls ==&gt; A : B : C : D
 * jshell&gt; ImmutableList&lt;Integer&gt; r1 = ImmutableList.range(10)
 * r1 ==&gt; 0 : 1 : 2 : 3 : 4 : 5 : 6 : 7 : 8 : 9
 * jshell&gt; ImmutableList&lt;Integer&gt; r2 = ImmutableList.range(0, 10, 3)
 * r2 ==&gt; 0 : 3 : 6 : 9
 * jshell&gt; ImmutableList&lt;Object&gt; r3 = ImmutableList.empty()
 * r3 ==&gt;
 * </pre>
 * <p> These lists can be used in for loops </p>
 * <pre>
 * jshell&gt; for (int i : ImmutableList.range(5))
 *    ...&gt;   System.out.println(i);
 * 0
 * 1
 * 2
 * 3
 * 4
 * </pre>
 * <p>
 * See docs for use case of other methods.
 * </p>
 * <p><code>Author: Foo Yong Qi</code></p>
 * @author Foo Yong Qi
 */
public interface ImmutableList<T> extends Iterable<T> {
    /**
     * Retrieves the element at some nonnegative index of this list.
     * <p> Example: </p>
     * <pre>
     * jshell&gt; ImmutableList&lt;Integer&gt; ls = ImmutableList.of(1, 2, 3, 4, 5);
     * ls ==&gt; 1 : 2 : 3 : 4 : 5
     * jshell&gt; ls.get(3);
     * $1 ==&gt; 4
     * jshell&gt; ImmutableList&lt;String&gt; ls2 = ImmutableList.of("A", "B", "C", "D");
     * ls2 ==&gt; A : B : C : D
     * jshell&gt; ls2.get(0);
     * $2 ==&gt; "A"
     * </pre>
     * @param index the index of the element to retrieve
     * @return the element at that index, <code>null</code> if it doesn't exists
     */
    T get(int index);

    /**
     * Determines if this list is empty.
     * <p> Example: </p>
     * <pre>
     * jshell&gt; ImmutableList&lt;Integer&gt; ls = ImmutableList.of(1, 2, 3, 4, 5);
     * ls ==&gt; 1 : 2 : 3 : 4 : 5
     * jshell&gt; ls.isEmpty();
     * $1 ==&gt; false
     * jshell&gt; ImmutableList&lt;String&gt; ls2 = ImmutableList.of();
     * ls2 ==&gt;
     * jshell&gt; ls2.isEmpty();
     * $2 ==&gt; true
     * </pre>
     * @return whether this list is empty
     */
    boolean isEmpty();

    /**
     * The number of elements of this list
     * <p> Example: </p>
     * <pre>
     * jshell&gt; ImmutableList&lt;Integer&gt; ls = ImmutableList.of(1, 2, 3, 4, 5);
     * ls ==&gt; 1 : 2 : 3 : 4 : 5
     * jshell&gt; ls.size();
     * $1 ==&gt; 5
     * </pre>
     * @return the number of elements of this list
     */
    long size();

    /**
     * Returns the first element of this list, <code>null</code> if it doesn't exist
     * <p> Example: </p>
     * <pre>
     * jshell&gt; ImmutableList&lt;Integer&gt; ls = ImmutableList.of(1, 2, 3, 4, 5);
     * ls ==&gt; 1 : 2 : 3 : 4 : 5
     * jshell&gt; ls.head();
     * $1 ==&gt; 1
     * jshell&gt; ImmutableList&lt;String&gt; ls2 = ImmutableList.of();
     * ls2 ==&gt;
     * jshell&gt; ls2.head();
     * $2 ==&gt; null
     * </pre>
     * @return the first element of this list, <code>null</code> if it doesn't exist
     */
    T head();

    /**
     * Returns the list excluding the head, <code>null</code> if it doesn't exist
     * <p> Example: </p>
     * <pre>
     * jshell&gt; ImmutableList&lt;Integer&gt; ls = ImmutableList.of(1, 2, 3, 4, 5);
     * ls ==&gt; 1 : 2 : 3 : 4 : 5
     * jshell&gt; ls.tail();
     * $1 ==&gt; 2 : 3 : 4 : 5
     * jshell&gt; ImmutableList&lt;String&gt; ls2 = ImmutableList.of();
     * ls2 ==&gt;
     * jshell&gt; ls2.tail();
     * $2 ==&gt; null
     * </pre>
     * @return the list excluding the head, <code>null</code> if it doesn't exist
     */
    ImmutableList<T> tail();

    /**
     * Returns a new <code>ImmutableList<T></code> as if an element has been appended to this list.
     * The original list is not mutated.
     * <p> Example: </p>
     * <pre>
     * jshell&gt; ImmutableList&lt;Integer&gt; ls = ImmutableList.of(1, 2, 3, 4, 5);
     * ls ==&gt; 1 : 2 : 3 : 4 : 5
     * jshell&gt; ls.appended(6);
     * $1 ==&gt; 1 : 2 : 3 : 4 : 5 : 6
     * jshell&gt; ImmutableList&lt;String&gt; ls2 = ImmutableList.of();
     * ls2 ==&gt;
     * jshell&gt; ls2.appended("A").appended("B");
     * $2 ==&gt; A : B
     * jshell&gt; ls2
     * $3 ==&gt;
     * </pre>
     * @param t the element to append to this list
     * @return the resulting list
     */
    ImmutableList<T> appended(T t);

    /**
     * Returns a new <code>ImmutableList<T></code> as if an element has been prepended to this list. The original list is not mutated.
     * <p> Example: </p>
     * <pre>
     * jshell&gt; ImmutableList&lt;Integer&gt; ls = ImmutableList.of(1, 2, 3, 4, 5);
     * ls ==&gt; 1 : 2 : 3 : 4 : 5
     * jshell&gt; ls.prepended(0);
     * $1 ==&gt; 0 : 1 : 2 : 3 : 4 : 5
     * jshell&gt; ImmutableList&lt;String&gt; ls2 = ImmutableList.of();
     * ls2 ==&gt;
     * jshell&gt; ls2.prepended("A").prepended("B");
     * $2 ==&gt; B : A
     * jshell&gt; ls2
     * $3 ==&gt;
     * </pre>
     * @param t the element to prepend to this list
     * @return the resulting list
     */
    ImmutableList<T> prepended(T t);

    /**
     * Concatenates this list with another list (this list comes first). Both lists are not mutated.
     * <p> Example: </p>
     * <pre>
     * jshell&gt; ImmutableList&lt;Integer&gt; ls = ImmutableList.of(1, 2);
     * ls ==&gt; 1 : 2
     * jshell&gt; ImmutableList&lt;Integer&gt; ls2 = ImmutableList.of(3, 4);
     * ls2 ==&gt; 3 : 4
     * jshell&gt; ls.concat(ls2);
     * $1 ==&gt; 1 : 2 : 3 : 4
     * jshell&gt; ls
     * $2 ==&gt; 1 : 2
     * jshell&gt; ls2
     * $3 ==&gt; 3 : 4
     * </pre>
     * @param other the other list to concatenate this list with
     * @return the resulting list
     */
    ImmutableList<T> concat(ImmutableList<T> other);

    /**
     * Maps each element of this list into something else using a function f
     * <p> Example: </p>
     * <pre>
     * jshell&gt; ImmutableList&lt;Integer&gt; ls = ImmutableList.of(1, 2, 3, 4);
     * ls ==&gt; 1 : 2 : 3 : 4
     * jshell&gt; ls.map(x -&gt; "A" + x)
     * $1 ==&gt; A1 : A2 : A3 : A4
     * jshell&gt; ls.map(x -&gt; x * x)
     * $2 ==&gt; 1 : 4 : 9 : 16
     * </pre>
     * @param <R> The type of the elements in the resulting list after mapping
     * @param f The function to map each element with
     * @return the resulting list
     */
    <R> ImmutableList<R> map(Function<T, R> f);

    /**
     * Filters this list using a predicate f
     * <p> Example: </p>
     * <pre>
     * jshell&gt; ImmutableList&lt;Integer&gt; ls = ImmutableList.of(1, 2, 3, 4, 5, 6);
     * ls ==&gt; 1 : 2 : 3 : 4 : 5 : 6
     * jshell&gt; ls.filter(x -&gt; x % 2 == 0)
     * $1 ==&gt; 2 : 4 : 6
     * </pre>
     * @param f the predicate to filter with
     * @return the resulting list
     */
    ImmutableList<T> filter(Predicate<T> f);

    /**
     * Performs a left-associative reduction on this list.
     * <p> Example: </p>
     * <pre>
     * jshell&gt; ImmutableList&lt;Integer&gt; ls = ImmutableList.of(1, 2, 3, 4, 5, 6);
     * ls ==&gt; 1 : 2 : 3 : 4 : 5 : 6
     * jshell&gt; ls.reduce((x, y) -&gt; x + y)
     * $1 ==&gt; 21
     * </pre>
     * @param f the function to reduce this list with
     * @return the resulting list
     */
    T reduce(BiFunction<T, T, T> f);

    /**
     * Gives the reverse of the list.
     * <p> Example: </p>
     * <pre>
     * jshell&gt; ImmutableList&lt;Integer&gt; ls = ImmutableList.of(1, 2, 3, 4, 5, 6);
     * ls ==&gt; 1 : 2 : 3 : 4 : 5 : 6
     * jshell&gt; ls.reversed()
     * $1 ==&gt; 6 : 5 : 4 : 3 : 2 : 1
     * </pre>
     * @return the reverse of the list
     */
    ImmutableList<T> reversed();

    /**
     * Creates an immutable list from an array of values.
     * <p> Example: </p>
     * <pre>
     * jshell&gt; ImmutableList&lt;Integer&gt; ls = ImmutableList.of(1, 2, 3, 4, 5, 6);
     * ls ==&gt; 1 : 2 : 3 : 4 : 5 : 6
     * jshell&gt; ImmutableList.of('a', 'b', 'c', 'd');
     * $1 ==&gt; a : b : c : d
     * jshell&gt; ImmutableList.of();
     * $2 ==&gt; 
     * jshell&gt; ImmutableList.of(new Integer[] {0, 1, 2});
     * $3 ==&gt; 0 : 1 : 2
     * </pre>
     * @param <T> the type of the elements of the list to create
     * @param values the values of this list
     * @return the resulting list
     */
    @SuppressWarnings("unchecked")
    static <T> ImmutableList<T> of(T... values) {
        ImmutableList<T> res = new ImmutableEmptyList<>();
        for (int i = values.length - 1; i >= 0; --i) {
            res = res.prepended(values[i]);
        }
        return res;
    }

    /**
     * Creates an empty list.
     * <p> Example: </p>
     * <pre>
     * jshell&gt; ImmutableList&lt;String&gt; ls = ImmutableList.empty();
     * ls ==&gt; 
     * jshell&gt; ls.append("A")
     * $1 ==&gt; A
     * </pre>
     * @param <T> the type of the elements of the list
     * @return the resulting list
     */
    static <T> ImmutableList<T> empty() {
        return new ImmutableEmptyList<>();
    }

    /**
     * Creates a range with start 0 and step 1
     * <p> Example: </p>
     * <pre>
     * jshell&gt; ImmutableList.range(10);
     * $1 ==&gt; 0 : 1 : 2 : 3 : 4 : 5 : 6 : 7 : 8 : 9
     * </pre>
     * @param stop the exclusive stop of the range
     * @return the resulting range
     */
    static ImmutableList<Integer> range(int stop) {
        ImmutableList<Integer> res = ImmutableList.empty();
        for (int i = 0; i < stop; ++i) {
            res = res.prepended(i);
        }
        return res.reversed();
    }

    /**
     * Creates a range with step 1
     * <p> Example: </p>
     * <pre>
     * jshell&gt; ImmutableList.range(4, 10);
     * $1 ==&gt; 4 : 5 : 6 : 7 : 8 : 9
     * </pre>
     * @param start the inclusive start of the range
     * @param stop the exclusive stop of the range
     * @return the resulting range
     */
    static ImmutableList<Integer> range(int start, int stop) {
        ImmutableList<Integer> res = ImmutableList.empty();
        for (int i = start; i < stop; ++i) {
            res = res.prepended(i);
        }
        return res.reversed();
    }

    /**
     * Creates a range
     * <p> Example: </p>
     * <pre>
     * jshell&gt; ImmutableList.range(6, -1, -2);
     * $1 ==&gt; 6 : 4 : 2 : 0
     * </pre>
     * @param start the inclusive start of the range
     * @param stop the exclusive stop of the range
     * @param step the step of the range
     * @return the resulting range
     */
    static ImmutableList<Integer> range(int start, int stop, int step) {
        ImmutableList<Integer> res = ImmutableList.empty();
        if (step > 0)
            for (int i = start; i < stop; i += step)
                res = res.prepended(i);
        else if (step < 0)
            for (int i = start; i > stop; i += step)
                res = res.prepended(i);
        return res.reversed();
    }
}
