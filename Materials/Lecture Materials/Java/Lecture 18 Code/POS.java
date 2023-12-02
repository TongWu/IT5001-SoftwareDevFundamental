public class POS {
    // just for nice formatting of each item
    private static final String ITEM_FORMAT = "%d. %s: %s\n";

    // just for nice formatting of prices
    private static String formatPrice(int price) {
        return String.format("$%d.%02d", price / 100, price % 100);
    }

    // to allow the number of orders to grow
    private static Order[] expandOrderArray(Order[] arr) {
        Order[] res = new Order[arr.length * 2];
        for (int i = 0; i < arr.length; ++i) {
            res[i] = arr[i];
        }
        return res;
    }

    // for keeping track of the next index to insert the next order
    private int i = 0;
    // start with enough space for 10 orders
    private Order[] orders = new Order[10];

    public void addOrder(Order order) {
        if (i == orders.length)
            orders = expandOrderArray(orders);
        orders[i++] = order;
    }

    public void printOrders() {
        int totalPrice = 0;
        for (int j = 0; j < i; ++j) {
            int p = orders[j].getPrice();
            System.out.printf(ITEM_FORMAT, j + 1, orders[j], formatPrice(p));
            totalPrice += p;
        }
        System.out.printf("Total price: %s\n", formatPrice(totalPrice));
    }
}
