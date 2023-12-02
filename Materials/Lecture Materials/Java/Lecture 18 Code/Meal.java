public class Meal implements Order {
    public static final String SMALL = "Small";
    public static final String MEDIUM = "Medium";
    public static final String LARGE = "Large";
    private AlaCarteBurger burger;
    private String size;

    public Meal(AlaCarteBurger b, String size) {
        this.burger = b;
        this.size = size;
    }

    public int getPrice() {
        if (size == LARGE)
            return burger.getPrice() + 300;
        if (size == MEDIUM)
            return burger.getPrice() + 200;
        return burger.getPrice() + 100;
    }

    @Override
    public String toString() {
        return String.format("%s meal with %s", size, burger);
    }
}
